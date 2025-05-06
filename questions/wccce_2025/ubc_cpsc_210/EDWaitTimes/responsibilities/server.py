from prairielearn import set_weighted_score_data

def grade(data):
    # give everyone a full score for cohesive question
    data["partial_scores"]["cohesive"]["score"] = 1

    set_weighted_score_data(data)
