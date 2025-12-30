# core/inference_engine.py

class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.fired_rules = []  # Track fired rules

    def forward_chain(self, working_memory):
        fired = []

        for rule in self.rules:
            if all(working_memory.has_fact(condition) for condition in rule["conditions"]):
                # Prevent firing the same rule twice
                if rule not in self.fired_rules:
                    fired.append(rule)                 # ✅ return full rule
                    self.fired_rules.append(rule)
                    working_memory.add_fact(rule["conclusion"])

        return fired
