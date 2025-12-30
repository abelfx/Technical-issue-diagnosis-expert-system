class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.fired_rules = [] 

    def forward_chain(self, working_memory):
        new_fired_in_this_session = []
        
        while True:
            new_rule_fired_this_cycle = False
            
            for rule in self.rules:
                if rule in self.fired_rules:
                    continue
                
                # Match: Check if all conditions exist in Working Memory
                if all(working_memory.has_fact(cond) for cond in rule["conditions"]):
                    # Add conclusion to memory
                    working_memory.add_fact(rule["conclusion"])
                    self.fired_rules.append(rule)
                    new_fired_in_this_session.append(rule)
                    
                    # Trigger next cycle because we have new knowledge
                    new_rule_fired_this_cycle = True
            
            # If a full pass happens without finding anything new, we are done
            if not new_rule_fired_this_cycle:
                break
                
        return new_fired_in_this_session