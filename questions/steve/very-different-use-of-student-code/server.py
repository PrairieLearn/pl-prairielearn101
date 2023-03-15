import value_gen
import re

PROBLEMS = [
    {
        "scenario": """about a hedge maze. Because of the way you 
create the design, a path in the maze can either be a dead-end (no exit) or a split from which
either two paths or three paths lead out. Also, every
point (dead-end or split) has a plaque on it indicating the donor name who sponsored that part 
of the maze (just text). Information about the plaque must go <em>first</em> in your data type's cases.""",
        "type": "HedgeMaze",
        "constructors": [
            {"name": "DeadEnd", "types": ["String"]},
            {"name": "Split2", "types": ["String", "HedgeMaze", "HedgeMaze"]},
            {"name": "Split3", "types": ["String", "HedgeMaze", "HedgeMaze", "HedgeMaze"]},
        ],
        "difficulty": 4,
    },
]

def extract_words(soln):
    # Hmm.. split on:
    # + \s+
    # + (?<=(:special:))\s*(?=(:special:))
    # + the same for special -> op, special -> normal, op -> normal, op -> special, normal -> special, normal -> op
    haskell_special_class = r"[(),;\[\]`{}]"
    haskell_op_class = r"[!#$%&*+./<=>?@\\^|-~:]"
    haskell_normal_class = r"""[A-Za-z0-9_"']"""

    boundary_pairs = [(left, right) 
                      for left in [haskell_special_class, haskell_normal_class, haskell_op_class]
                      for right in [haskell_special_class, haskell_normal_class, haskell_op_class]
                      if left != right] + \
                     [(haskell_special_class, haskell_special_class)]
    # Find the left thing just before the match, the right thing just after, and 0+ whitespace in the middle.
    # Also includes plain old whitespace (though that is perhaps not necessary since we strip whitespace
    # at start/end).
    boundary_res = [r"\s+"] + [f"(?<={re_left})\\s*(?={re_right})" 
                               for (re_left, re_right)
                               in boundary_pairs]

    # Non-matching "find any of those above"
    boundary_re = f"(?:{'|'.join(boundary_res)})"

    # Split, stripping start/end whitespace to avoid empty groups.
    return re.split(boundary_re, soln.strip())

def gen_one(problem):
    caseTexts = [f"{c['name']} {' '.join(c['types'])}" for c in problem["constructors"]]
    caseWords = [[c['name'], *c['types']] for c in problem["constructors"]]
    cases = [{"words": caseWords[i], "number": i+1} for i in range(len(caseTexts))]
    solution = f"data {problem['type']} = {'|'.join(caseTexts)}"
    words = extract_words(solution)
    constructors = problem["constructors"][:]

    return {
        "scenario": problem["scenario"],
        "solution": solution,
        "randomOrder": list(value_gen.shuffled(words, False)),
        "alphaOrder": sorted(words),
        "type": problem["type"],
        "constructors": constructors,
        "cases": cases
    }

def generate(data):
    problem = next(value_gen.shuffled(PROBLEMS))
    data["params"] = gen_one(problem)
