from core.working_memory import WorkingMemory
from core.inference_engine import InferenceEngine
from domain.rules import RULES
from domain.solutions import SOLUTIONS

class DiagnosisService:
    def diagnose(self, selected_facts):
        wm = WorkingMemory()
        for fact in selected_facts:
            wm.add_fact(fact)
        
        engine = InferenceEngine(RULES)
        fired = engine.forward_chain(wm)

        results = []

        for rule in fired:
            results.append({
                "issue": rule["conclusion"],
                "solution": SOLUTIONS.get(rule["conclusion"], "No solution available."),
                "confidence": rule.get("confidence", 1.0)
            })

        return results, engine.fired_rules