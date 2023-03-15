"""Random generation of names, values, etc. intended for use in question variants."""

import random

"""Meaningless variable names longer than one letter (3 to 5 letters).

Based originally on metasyntactic variable names article on Wikipedia and surrounding articles. These
have been manually filtered to be reasonably distinct from each other (e.g., baz is absent because bar
is present) and not likely to be insulting or offensive.

>>> all([3 <= len(s) <= 5 for s in LONG_VARIABLE_NAMES])
True
"""
LONG_VARIABLE_NAMES = ["acme", "bar", "corge", "eggs", "fitch", "flob", "fnord", "foo", "frob", "gizmo", "ham", "hoge", "ipsum",
                       "lorem", "mell", "newco", "octan", "piyo", "plugh", "quux", "smurf", "spam", "stad", "thud", "toto",
                       "waldo", "wug", "xyzzy", "gonk", "ping", "tappa", "shoop", "wow", "lub", "mest", "fizz", "buzz"]


"""One-letter variable names that are reasonably unlikely to be mistaken for something else.

>>> all([len(s) == 1 for s in SHORT_VARIABLE_NAMES)
True
"""
SHORT_VARIABLE_NAMES = ["x", "y", "z", "p", "q", "r", "s", "v", "w"]

"""Short variable names that are reasonable for functions and reasonably unlikely to be mistaken for something else.

>>> all([f not in SHORT_VARIABLE_NAMES for f in SHORT_FUN_NAMES)
True

>>> all([len(f) <= 3 for f in SHORT_FUN_NAMES)
True
"""
SHORT_FUN_NAMES = ["f", "g", "h", "fun", "go"]

LITERAL_SETS = {
    "Int": {
        "[1,50]": [f"{i+1}" for i in range(50)],
    },
    "Char": {
        "lowerAZ": [f"'{chr(i + ord('a'))}'" for i in range(26)],
    },
    "Double": {
        "[0,50) by 0.2": [f"{(x / 5):.1f}" for x in range(50)],
    },
    "String": {
        "les mis": [
            "\"azelma\"",
            "\"bougon\"",
            "\"brevet\"",
            "\"brujon\"",
            "\"cosette\"",
            "\"dahlia\"",
            "\"fameuil\"",
            "\"fantine\"",
            "\"gervais\"",
            "\"hugo\"",
            "\"javert\"",
            "\"joly\"",
            "\"mabeuf\"",
            "\"magnon\"",
            "\"myriel\"",
            "\"valjean\"",
        ]
    },
    "Bool": {
        "all": ["True", "False"],
    }
}

def choose_one(list):
    return next(shuffled(list, False))

def shuffled(lst, endless=True):
    """Returns a generator that produces list values in a random order.

    If endless is True, repeats (with a new random order) each time
    the original list runs out."""
    new_list = list(lst)
    while True:
        random.shuffle(new_list)
        for value in new_list:
            yield value
        if not endless:
            break


__all__ = [LONG_VARIABLE_NAMES, SHORT_VARIABLE_NAMES,
           SHORT_FUN_NAMES, LITERAL_SETS, shuffled]
