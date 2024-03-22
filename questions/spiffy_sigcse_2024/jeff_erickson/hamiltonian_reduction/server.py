from typing import Dict, Any, List
from uiuc.pseudocode_order_blocks.utils import extract_submitted_pseudocode, submit_translated_code

mapping = {
    "Let $G'$ be a copy of $G$": "G_prime = copy.deepcopy(G)",
    "Let $v$ be an arbitrary vertex in $G'$": "v='v'; networkx.relabel_nodes(G_prime, {0:v}, copy=False)",
    "Add a new vertex $w$ to $G'$": "w='w'; G_prime.add_node(w)",
    "Connect $w$ to every neighbor of $v$": "for i in G_prime.neighbors(v): G_prime.add_edge(w, i)",
    "Add a new vertex $s$ to $G'$": "s='s'; G_prime.add_node(s)",
    "Add a new vertex $t$ to $G'$": "t='t'; G_prime.add_node(t)",
    "Connect $s$ to $v$": "G_prime.add_edge(s, v)",
    "Connect $t$ to $w$": "G_prime.add_edge(t, w)",
    "Connect $s$ to $w$": "G_prime.add_edge(s, w)",
    "Connect $s$ to $t$": "G_prime.add_edge(s, t)",
    "Connect $v$ to $w$": "G_prime.add_edge(v, w)",
    "Connect $t$ to $v$": "G_prime.add_edge(t, v)",
    "Connect $w$ to every other vertex in $G'$": "for i in list(G_prime):\n\t\tif i != w:\n\t\t\tG_prime.add_edge(w, i)",
    "Remove an arbitrary edge from $G'$": "e = list(G_prime.edges)[0]; G_prime.remove_edge(*e)"
}


def generate(data: Dict[str, Dict[str, Any]]) -> None:

    data['params']['pseudocode_lines'] = list(mapping.keys())

    data['params']['names_for_user'] = []
    data['params']['names_from_user'] = [
        {'name': 'f', 'description': 'Performs graph reduction', 'type': 'Function'}
    ]


def parse(data: Dict[str, Dict[str, Any]]) -> None:
    pseudocode = extract_submitted_pseudocode(data, "pseudocode")

    if pseudocode is None:
        data["format_errors"]["pseudocode"] = "You did not submit any pseudocode."
    else:
        imports = ["networkx", "copy"]
        function_line = "def f(G):"
        return_line = "return G_prime"
        setup_lines: List[str] = []
        submit_translated_code(data, pseudocode, mapping,
                               imports, function_line, setup_lines, return_line)
