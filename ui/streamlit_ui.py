import streamlit as st
from domain.facts import FACTS
from services.diagnosis_service import DiagnosisService
from core.explanation_engine import explain
import copy
from domain.rules import RULES as BASE_RULES

def run_ui():
    # Page Config for a professional look
    st.set_page_config(page_title="Pro-Tech Diagnostic", page_icon="🛠", layout="wide")
    
    st.title("Professional IT Diagnostic System")
    st.markdown("---")

    # Sidebar for instructions
    with st.sidebar:
        st.header("Instructions")
        st.info("Select symptoms. The Hybrid Engine uses Forward and Backward chaining with Fuzzy logic to diagnose.")
        if st.button("Reset Session"):
            st.rerun()

    # Organized Input Section
    st.subheader("Identify Symptoms")
    
    selected_symptoms = st.multiselect(
        "Search or select symptoms below:",
        options=FACTS,
        format_func=lambda x: x.replace("_", " ").capitalize(),
        help="Select all conditions that apply to the current hardware state."
    )

    st.markdown("---")

    # Execution Section
    if st.button("Run System Diagnostic", type="primary"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom to begin.")
        else:
            # Ensure rules are initialized in session state
            if "rules" not in st.session_state:
              
                st.session_state.rules = copy.deepcopy(BASE_RULES)
            service = DiagnosisService(st.session_state.rules)
            # Updated to receive results, fired_rules, and the new trace_log
            results, fired_rules, trace_log = service.diagnose(set(selected_symptoms))

            if results:
                st.subheader("Diagnosis Complete")
                
                for r in results:
                    with st.container():
                        col1, col2 = st.columns([1, 3])
                        
                        # PRIORITY & CONFIDENCE COLUMN
                        with col1:
                            # Fuzzy Logic Score visualization
                            conf_val = r['confidence']
                            st.metric(label="Certainty Factor", value=f"{int(conf_val*100)}%")
                            
                            # Visual Priority Label
                            p_val = r.get('priority', 3)
                            p_map = {1: "🔴 P1: Critical", 2: "🟠 P2: Moderate", 3: "🔵 P3: Low"}
                            st.write(f"**Priority:** {p_map.get(p_val, 'P3')}")
                        
                        # ISSUE DISPLAY COLUMN
                        with col2:
                            if p_val == 1:
                                st.error(f"**Detected Issue:** {r['issue'].replace('_', ' ').title()}")
                            elif p_val == 2:
                                st.warning(f"**Detected Issue:** {r['issue'].replace('_', ' ').title()}")
                            else:
                                st.info(f"**Detected Issue:** {r['issue'].replace('_', ' ').title()}")
                            
                        with st.expander("View Recommended Solution", expanded=(p_val == 1)):
                            st.markdown(r['solution'])
                    st.divider()

                # --- IMPROVEMENT: LOGGING & RULE TRACING ---
                st.subheader("Intelligence & Trace Report")
                
                col_exp, col_log = st.columns(2)
                
                with col_exp:
                    with st.expander("Show Logical Inference Path"):
                        explanations = explain(fired_rules)
                        for e in explanations:
                            st.write(f"{e}")
                
                with col_log:
                    with st.expander("Show Raw Engine Trace (Debugging)"):
                        # This shows your Backward Chaining and Fuzzy evaluations
                        for entry in trace_log:
                            st.code(entry, language="bash")
                            
            else:
                st.error("Inconclusive: No rules matched. The Engine could not prove any critical hypothesis.")

if __name__ == "__main__":
    run_ui()