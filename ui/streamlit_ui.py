import streamlit as st
from domain.facts import FACTS
from service.diagnosis_service import DiagnosisService
from core.explanation_engine import explain

def run_ui():
    st.title("🛠 Technical Troubleshooting Expert System")

    selected_facts = set()
    for fact in FACTS:
        if st.checkbox(fact.replace("_", " ").capitalize()):
            selected_facts.add(fact)

    if st.button("Diagnose"):
        service = DiagnosisService()
        results, fired_rules = service.diagnose(selected_facts)

        if results:
            for r in results:
                st.success(f"Issue: {r['issue']} ({int(r['confidence']*100)}%)")
                st.info(f"Solution: {r['solution']}")

            st.subheader("Explanation")
            for e in explain(fired_rules):
                st.write("•", e)
        else:
            st.warning("No diagnosis found.")
