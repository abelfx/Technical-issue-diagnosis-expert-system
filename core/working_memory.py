class WorkingMemory:
    def __init__(self):
        self.facts = {} # {fact: certainty}
    
    def add_fact(self, fact, certainty=1.0):
        # Fuzzy 'OR': keep the highest certainty found
        self.facts[fact] = max(self.facts.get(fact, 0.0), certainty)
    
    def has_fact(self, fact):
        return self.facts.get(fact, 0.0) > 0.5 # Threshold for "Truth"