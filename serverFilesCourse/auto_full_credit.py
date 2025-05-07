"""Utility library for granting credit to problems. Most common use is to grant full credit automatically.
For that functionality, just create a server.py file with nothing but:

  from auto_full_credit import grade
"""

def grade(data):
    """Import this to automatically grade all parts and the full problem as worth full credit."""
    for part_name in data["partial_scores"]:
        grant_credit(data, part_name)
    recompute_score_from_parts(data)

def recompute_score_from_parts(data, default_if_no_parts = 1):
    """Recompute the weighted overall score for this problem from its parts. If there are no parts, assigns the given default grade."""
    # TODO: replace with pl.set_weighted_score_data(data)?
    total_weight = 0
    total_score = 0
    for part in data["partial_scores"].values():
        total_weight += part["weight"]
        total_score += part["score"] * part["weight"]
    if total_weight != 0:
        data["score"] = total_score / total_weight
    else:
        data["score"] = default_if_no_parts

def grant_credit(data, problem_name, new_credit = 1):
    """Grant the given amount of credit (in [0, 1]) to the named problem.

    Does NOT recompute overall scores. Call recompute_score_from_parts when done!"""
    data["partial_scores"][problem_name]["score"] = new_credit
