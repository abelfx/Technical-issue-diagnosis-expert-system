class WorkingMemory:
    def __init__(self):
        self.facts = set()
    
    def add_fact(self, fact):
        self.facts.add(fact) # adds a fact to the working memory
    
    def remove_fact(self, fact):
        self.facts.discard(fact) # removes a fact from the working memory if it exists
    
    def has_fact(self, fact):
        return fact in self.facts # checks if a fact is in the working memory
    
    def clear(self):
        self.facts.clear() # clears all facts from the working memory
    
    