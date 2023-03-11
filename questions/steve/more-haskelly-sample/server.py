import value_gen

OP_VALUES = [
    ("and", "<code>a</code> is true and <code>b</code> is also true", "andLB"),
    ("or", "<code>a</code> is true or <code>b</code> is true (or both)", "orLB"),
]
OPTI_PESSI_VALS = [("optimistic", "True"), ("pessimistic", "False")]

def generate(data):
    (op, expl, main) = next(value_gen.shuffled(OP_VALUES, False))
    (op_istic, op_maybe_val) = next(value_gen.shuffled(OPTI_PESSI_VALS, False))
    params = {
        "main": main,
        "op": op,
        "opABTrueExplanation": expl,
        "optiPessiMistic": op_istic,
        "optiPessiMaybeVal": op_maybe_val,
        "names_from_user": {
            "name": main, 
            "description": f"computes logical {op}, under the interpretation above",
            "type": "takes two [Bool]s and returns a normal Bool"
        }
    }
    data["params"] = params
