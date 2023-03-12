import random
import value_gen

# Elements neeeded under params:
#
# The name of the type and a bunch of spaces as long as the name of the type:
# {{TypeNameSpaces}}{{TypeName}}
#
# Designated type that must be in every case except one:
# {{SelectedType}} and suitable for identifier: {{SelectedTypeID}}
# and suitable default value for the type: {{DefaultValue}}
#
# Constructor cases for the type:
#   {{#Cases}}{{Constructor}}{{#Types}}{{.}}
#   {{#LastCase}}{{Constructor}}{{#Types}}{{.}}
#
# A constructor name for a case that lacks the selected type:
#   {{NoSTConstructor}}

NORMAL_TYPENAMES = ["Int", "String", "[Bool]", "Double"]
SELECTED_TYPE = random.choice(NORMAL_TYPENAMES)
NORMAL_TYPENAMES.remove(SELECTED_TYPE)
NORMAL_TYPENAMES_SRC = value_gen.shuffled(NORMAL_TYPENAMES)
LONGNAMES_SRC = value_gen.shuffled(value_gen.LONG_VARIABLE_NAMES, False)

TYPE_DEFAULTS = {
    "Int": "0",
    "String": "\"\"",
    "[Bool]": "[]",
    "Double": "0.0",
}

TYPE_IDS = {
    "[Bool]": "BoolList",
}

def getTypeDefault(type):
    return TYPE_DEFAULTS[type]

def getTypeID(type):
    return TYPE_IDS.get(type, type)

def plain_type_name():
    return next(NORMAL_TYPENAMES_SRC)

def fresh_type_name():
    length_options = [1, 1, 2]
    length = random.choice(length_options)
    names = []
    for i in range(length):
        names.append(next(LONGNAMES_SRC).capitalize())
    return "".join(names)

def gen_case(num_types):
    return {
        "Constructor": fresh_type_name(),
        "Types": [plain_type_name() for i in range(num_types)]
    }

def generate(data):
    num_cases_options = [3, 4]
    num_cases = random.choice(num_cases_options)

    num_types_options = [0, 1, 1, 2]

    type_name = fresh_type_name()

    # Generate enough cases.
    cases = [gen_case(random.choice(num_types_options)) for i in range(num_cases)]

    # Add the selected type to all but the last case:
    for i in range(num_cases - 1):
        types = cases[i]["Types"]
        types.insert(random.randrange(len(types) + 1), SELECTED_TYPE)
    no_st_constructor = cases[-1]["Constructor"]

    # Generate the patterns needed for the sample solution:
    default = getTypeDefault(SELECTED_TYPE)
    for case in cases:
        case["Patterns"] = ["x" if type == SELECTED_TYPE else "_" for type in case["Types"]]
        case["Result"] = "x" if (SELECTED_TYPE in case["Types"]) else default

    # Reorder the cases
    random.shuffle(cases)

    # Break off the final case.
    last_case = cases[-1]
    cases = cases[:-1]

    # Store all the needed values:
    params = {
        "TypeName": type_name,
        "TypeNameSpaces": " " * len(type_name),
        "Cases": cases,
        "LastCase": last_case,
        "SelectedType": SELECTED_TYPE,
        "DefaultValue": getTypeDefault(SELECTED_TYPE),
        "SelectedTypeID": getTypeID(SELECTED_TYPE),
        "NoSTConstructor": no_st_constructor,
    }
    data["params"] = {**data["params"], **params}
