def explain(fired_rules):
    explanations = []
    for rule in fired_rules:
        explanation = f"Rule '{rule['conditions']}' was fired because conditions were met: {', '.join(rule['conditions'])}."
        explanations.append(explanation)
    return explanations