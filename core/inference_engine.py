class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.fired_rules = []
        self.trace_log = [] # 3️⃣ Adding Rule Tracing

    def forward_chain(self, working_memory):
        self.trace_log.append("Starting Forward Chaining...")
        new_fired = []
        while True:
            fired_in_cycle = False
            for rule in self.rules:
                if rule in self.fired_rules: continue
                
                if all(working_memory.has_fact(c) for c in rule["conditions"]):
                    working_memory.add_fact(rule["conclusion"])
                    self.fired_rules.append(rule)
                    new_fired.append(rule)
                    self.trace_log.append(f"FIRED: {rule['conclusion']} (Conditions met)")
                    fired_in_cycle = True
            if not fired_in_cycle: break
        return new_fired

    def backward_chain(self, goal, working_memory):
        """1️⃣ Backward Chaining: Can we prove this goal?"""
        self.trace_log.append(f"Attempting to prove goal: {goal}")
        
        # Base case: we already know it
        if working_memory.has_fact(goal):
            return True
            
        # Find rules that could result in this goal
        matching_rules = [r for r in self.rules if r["conclusion"] == goal]
        
        for rule in matching_rules:
            # Try to prove all conditions of this rule
            if all(self.backward_chain(cond, working_memory) for cond in rule["conditions"]):
                working_memory.add_fact(goal)
                if rule not in self.fired_rules:
                    self.fired_rules.append(rule)
                return True
        
        return False