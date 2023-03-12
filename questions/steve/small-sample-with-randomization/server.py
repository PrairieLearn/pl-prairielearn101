import value_gen

names = value_gen.SHORT_FUN_NAMES

SUPERLATIVES = ["largest", "smallest"]
OPS = ["difference (left value minus right value)", "sum", "absolute difference (absolute value of the difference)"]

# For some reason, always producing the first element with a two-element list.
VAL_OR_ZEROS = ["the single element's value", "0", "the single element's value"]

def generate(data):
    name = next(value_gen.shuffled(names, False))
    superlative = next(value_gen.shuffled(SUPERLATIVES, False))
    op = next(value_gen.shuffled(OPS, False))
    valOrZero = next(value_gen.shuffled(VAL_OR_ZEROS, False))
    params = {
        "name": name,
        "superlative": superlative,
        "op": op,
        "valOrZero": valOrZero
    }
    data["params"] = params
