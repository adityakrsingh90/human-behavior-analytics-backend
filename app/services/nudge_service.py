def generate_nudge(prediction: dict):
    burnout = prediction["burnout_score"]
    productivity = prediction["productivity_score"]

    if burnout > 0.7:
        return "You seem mentally overloaded. Consider taking a short break or reducing screen time."
    elif productivity < 0.4:
        return "Try a focused 25-minute deep work session with notifications off."
    else:
        return "You're doing well. Maintain your current routine."
