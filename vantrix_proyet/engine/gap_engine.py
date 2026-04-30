def evaluate_opportunity(features):
    """
    Calcula oportunidad base
    """

    score = (
        features["trend_score"] +
        features["demand"] -
        features["competition"]
    )

    return score