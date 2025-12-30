from core.working_memory import WorkingMemory
from core.inference_engine import InferenceEngine
from domain.rules import RULES
from domain.solutions import SOLUTIONS

class DiagnosisService:
    def diagnose(self, selected_facts):
        from core.working_memory import WorkingMemory
        from core.inference_engine import InferenceEngine
        from domain.rules import RULES
        
        wm = WorkingMemory()
        for fact in selected_facts:
            wm.add_fact(fact)
        
        engine = InferenceEngine(RULES)
        fired = engine.forward_chain(wm)

        # Sort by Priority (1=High, 3=Low) then by Confidence (High to Low)
        fired_sorted = sorted(
            fired, 
            key=lambda x: (x.get("priority", 3), -x.get("confidence", 0))
        )

        results = []
        for rule in fired_sorted:
            results.append({
                "issue": rule["conclusion"],
                "solution": SOLUTIONS.get(rule["conclusion"], "Consult technical manual."),
                "confidence": rule.get("confidence", 1.0),
                "priority": rule.get("priority", 3)
            })

        return results, engine.fired_rules