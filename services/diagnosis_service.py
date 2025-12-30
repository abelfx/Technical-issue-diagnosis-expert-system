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
        
        # Run Forward Chaining
        engine.forward_chain(wm)
        
        # Proactively check for Critical issues (Backward Chaining)
        critical_goals = [r["conclusion"] for r in RULES if r.get("priority") == 1]
        for goal in critical_goals:
            engine.backward_chain(goal, wm)

        # Sort and return
        fired_sorted = sorted(engine.fired_rules, key=lambda x: (x.get("priority", 3), -x.get("confidence", 0)))
        
        results = []
        for rule in fired_sorted:
            results.append({
                "issue": rule["conclusion"],
                "solution": SOLUTIONS.get(rule["conclusion"], "Consult manual."),
                "confidence": rule.get("confidence", 1.0),
                "priority": rule.get("priority", 3)
            })

        return results, engine.fired_rules, engine.trace_log