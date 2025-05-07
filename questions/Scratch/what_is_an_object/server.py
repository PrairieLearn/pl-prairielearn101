def check_values(data):
    value_1 = data["submitted_answers"]["string_value_1"].lower()
    value_2 = data["submitted_answers"]["string_value_2"].lower()
    values = {value_1, value_2}
    if values == {"properties", "behavior"}:
        return 1
    elif "properties" in values or "behavior" in values:
        return 0.5
    else:
        return 0

def grade(data):
    data["score"] = check_values(data)
