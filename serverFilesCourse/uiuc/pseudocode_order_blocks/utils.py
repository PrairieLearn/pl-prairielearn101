from typing import Dict, Any, List, Optional
import base64
import html


def extract_submitted_pseudocode(data: Dict[str, Any], answer_name: str) -> Optional[List[str]]:
    """
    Extracts the raw text of student's submitted pseudocode block line by line
    """
    if answer_name not in data['submitted_answers']:
        return None
    return [html.unescape(line['inner_html']) for line in data['submitted_answers'][answer_name]]


def submit_translated_code(data: Dict[str, Any], pseudocode: List[str], mapping: Dict[str, str], imports: List[str], function_line: str, setup_lines: List[str], return_line: str) -> None:

    def base64_encode_string(s):
        # do some wonky encode/decode because base64 expects a bytes object
        return base64.b64encode(s.encode('utf-8')).decode('utf-8')

    code = ["import " + imp for imp in imports]
    code.append(function_line)
    code += ["\t" + line for line in setup_lines]
    code += ["\t" + mapping[line] for line in pseudocode]
    code.append("\t" + return_line)

    data['submitted_answers']['_files'] = [
        {
            'name': 'user_code.py',
            'contents': base64_encode_string("\n".join(code))
        }
    ]
