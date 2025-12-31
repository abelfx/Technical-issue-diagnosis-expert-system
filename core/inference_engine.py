class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.fired_rules = []
        self.trace_log = []  # Rule tracing

    def compute_rule_score(self, rule):
        
        priority_score = (4 - rule.get("priority", 3)) * 100  # P1=300, P2=200, P3=100
        confidence_score = rule.get("confidence", 1.0) * 50
        specificity_score = len(rule.get("conditions", [])) * 10
        total_score = priority_score + confidence_score + specificity_score
        return total_score

    def forward_chain(self, working_memory):
        self.trace_log.append("Starting Forward Chaining with dynamic conflict resolution...")
        new_fired = []

        while True:
            # Gather all eligible rules
            eligible_rules = [
                rule for rule in self.rules
                if rule not in self.fired_rules
                and all(working_memory.has_fact(cond) for cond in rule["conditions"])
            ]

            if not eligible_rules:
                break  # No more rules can fire

            # Sort rules by dynamic score
            eligible_rules.sort(key=lambda r: self.compute_rule_score(r), reverse=True)

            # Fire the top-scoring rule
            rule_to_fire = eligible_rules[0]
            working_memory.add_fact(rule_to_fire["conclusion"])
            self.fired_rules.append(rule_to_fire)
            new_fired.append(rule_to_fire)
            self.trace_log.append(
                f"FIRED: {rule_to_fire['conclusion']} "
                f"(Priority: {rule_to_fire.get('priority',3)}, "
                f"Confidence: {rule_to_fire.get('confidence',1.0)}, "
                f"Score: {self.compute_rule_score(rule_to_fire)})"
            )

        return new_fired

    def backward_chain(self, goal, working_memory):
        """
        Backward Chaining: Can we prove this goal?
        """
        self.trace_log.append(f"Attempting to prove goal: {goal}")

        # Base case: already known
        if working_memory.has_fact(goal):
            return True

        # Find rules that could produce this goal
        matching_rules = [r for r in self.rules if r["conclusion"] == goal]

        for rule in matching_rules:
            # Try to prove all conditions of this rule
            if all(self.backward_chain(cond, working_memory) for cond in rule["conditions"]):
                working_memory.add_fact(goal)
                if rule not in self.fired_rules:
                    self.fired_rules.append(rule)
                    self.trace_log.append(f"FIRED (Backward): {goal}")
                return True

        return False

    def update_confidence(self, rule, delta):
        old_conf = rule.get("confidence", 1.0)
        new_conf = max(0.0, min(old_conf + delta, 1.0))
        rule["confidence"] = new_conf
        self.trace_log.append(
            f"Updated confidence for '{rule['conclusion']}' from {old_conf:.2f} to {new_conf:.2f}"
        )
