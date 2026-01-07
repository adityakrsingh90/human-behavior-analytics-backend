def check_drift(user_history: list):
    """
    Simple conceptual drift logic
    """
    if len(user_history) < 5:
        return False

    avg_burnout = sum([x["burnout_score"] for x in user_history]) / len(user_history)

    return avg_burnout > 0.6
