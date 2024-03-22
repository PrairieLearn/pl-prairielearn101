from typing import Dict
from lib.tokens import Tokens, Token, TokenType, regex_chunk_lines
from collections import defaultdict
from enum import IntEnum
from re import match as test
from lib.consts import *
import lib.io_helpers as io


def parse_blanks(source_path: str, tkn: Token, blank_re: Pattern):

    itr = regex_chunk_lines(blank_re, tkn.text, line_number=tkn.lineno)
    # (exclusive) end of the last match
    for line_number, found, chunk in itr:
        if found:
            # non-None
            blank, = chunk.groups()
            if not blank:
                # only possible with custom regexes.
                raise SyntaxError(
                    'blankDelimiter Regex captured empty text at '
                        + io.format_ln(source_path, line_number))

            yield (blank, BLANK_SUBSTITUTE)
        else:
            yield (chunk, chunk)

def parse_fpp_regions(tokens: Tokens) -> Dict[str, str]:
    """Transform a lexed collection of Tokens into a dictionary where
       keys are region names and values are data contained.
    """
    if 'blankDelimiter' in tokens.metadata:
        blank_re = io.make_blank_re(tokens.metadata['blankDelimiter'])
    else:
        blank_re = DEFAULT_BLANK_PATTERN

    r_texts: dict[str, list[str]] = defaultdict(list)
    answer, prompt = r_texts['answer_code'], r_texts['prompt_code']

    class DocstringState(IntEnum):
        Accepting = 0
        FollowWithNewline = 1
        Finished = 2
        Skipped = 3

    docstring_state = DocstringState.Accepting
    for tkn in tokens.data:
        if not tkn.text: continue

        if tkn.region:
            if tkn.region == 'question_text' and docstring_state == DocstringState.FollowWithNewline:
                r_texts[tkn.region].append('\n')
                docstring_state = DocstringState.Finished
            elif tkn.region == 'prompt_code':
                for ans, prmpt in parse_blanks(tokens.source_path, tkn, blank_re):
                    answer.append(ans)
                    prompt.append(prmpt)
                continue
            r_texts[tkn.region].append(tkn.text)
            continue

        if tkn.type == TokenType.DOCSTRING:
            if docstring_state == DocstringState.Accepting:
                qs = r_texts['question_text']
                if qs:
                    qs.append('\n')
                    docstring_state = DocstringState.Finished
                else:
                    docstring_state = DocstringState.FollowWithNewline
                qs.append(tkn.text[3:-3])
            else:
                prompt.append(tkn.text)
                answer.append(tkn.text)
        elif tkn.type == TokenType.COMMENT:
            target = prompt if test(SPECIAL_COMMENT_PATTERN, tkn.text) \
                else answer
            target.append(tkn.text)
        elif tkn.type == TokenType.STRING:
            prompt.append(tkn.text)
            answer.append(tkn.text)
        elif tkn.type == TokenType.UNMATCHED:
            for ans, prmpt in parse_blanks(tokens.source_path, tkn, blank_re):
                answer.append(ans)
                prompt.append(prmpt)
        else:
            raise Exception("Unreachable! Inexhaustive token types: " + str(tkn.type))

        docstring_state = docstring_state or DocstringState.Skipped

    out = { 'metadata': tokens.metadata }
    for k, region_list in r_texts.items():
        ls = ''.join(region_list)
        ls = map(str.rstrip, ls.splitlines())
        if k == 'prompt_code':
            ls = filter(bool, ls)
        out[k] = '\n'.join(ls).strip()

    return out

