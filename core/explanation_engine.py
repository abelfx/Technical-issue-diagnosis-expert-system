def explain(fired_rules):
    explanations = []
    for rule in fired_rules:
        conds = ", ".join([c.replace('_', ' ') for c in rule['conditions']])
        conc = rule['conclusion'].replace('_', ' ').title()
        
        explanation = f"Because **{conds}** were observed, the system concluded: **{conc}**."
        explanations.append(explanation)
    return explanations