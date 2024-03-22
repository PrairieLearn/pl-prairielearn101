def generate(data):
    data['params']['names_for_user'] = []
    data["params"]["names_from_user"] = [
  {
    "name": "dict_bully",
    "description": "A function that, given a dictionary, has \"b\" take the value of \"a\" and sets \"a\" to \"<stolen>\".",
    "type": "function"
  },
  {
    "name": "dict_AB",
    "description": "A function that, given a dictionary, concatenates the values of keys \"a\" and \"b\" into a new key \"ab\".",
    "type": "function"
  },
  {
    "name": "topping_1",
    "description": "A function that, given a dictionary, sets \"ice cream\" to \"cherry\" (if present) and \"bread\" to \"butter\".",
    "type": "function"
  },
  {
    "name": "topping_2",
    "description": "A function that, given a dictionary, sets \"yogurt\" to match the value of \"ice cream\" (if present) and changes the value of \"spinach\" to \"nuts\" (if present).",
    "type": "function"
  },
  {
    "name": "dict_AB2",
    "description": "A function that, given a dictionary, removes both \"a\" and \"b\" keys if they have equal values.",
    "type": "function"
  },
  {
    "name": "dict_AB3",
    "description": "A function that, given a dictionary, sets the value of \"a\" to match the value of \"b\".",
    "type": "function"
  },
  {
    "name": "dict_AB4",
    "description": "A function that adjusts values in a dictionary based on their lengths.",
    "type": "function"
  }
]