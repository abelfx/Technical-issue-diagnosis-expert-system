
from core.working_memory import WorkingMemory
from core.inference_engine import InferenceEngine
from domain.solutions import SOLUTIONS


class DiagnosisService:
    def __init__(self, rules):
        self.rules = rules

    def diagnose(self, selected_facts, feedback=None):
        wm = WorkingMemory()
        for fact in selected_facts:
            wm.add_fact(fact)

        engine = InferenceEngine(self.rules)

        # Run Forward Chaining
        engine.forward_chain(wm)

        # Proactively check for Critical issues (Backward Chaining)
        critical_goals = [r["conclusion"] for r in self.rules if r.get("priority") == 1]
        for goal in critical_goals:
            engine.backward_chain(goal, wm)

        # Sort and return
        fired_sorted = sorted(
            engine.fired_rules, key=lambda x: (x.get("priority", 3), -x.get("confidence", 0))
        )

        results = []
        for rule in fired_sorted:
            results.append({
                "issue": rule["conclusion"],
                "solution": SOLUTIONS.get(rule["conclusion"], "Consult manual."),
                "confidence": rule.get("confidence", 1.0),
                "priority": rule.get("priority", 3)
            })

        # --- Update confidence based on feedback if provided ---
        if feedback:
            for r in fired_sorted:
                issue = r["conclusion"]
                if issue in feedback:
                    if feedback[issue]:
                        engine.update_confidence(r, delta=0.05)  # increase confidence
                    else:
                        engine.update_confidence(r, delta=-0.05) # decrease confidence

        return results, engine.fired_rules, engine.trace_log
