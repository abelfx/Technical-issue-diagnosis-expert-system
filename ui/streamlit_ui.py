import streamlit as st
from domain.facts import FACTS
from services.diagnosis_service import DiagnosisService
from core.explanation_engine import explain

def run_ui():
    # Page Config for a professional look
    st.set_page_config(page_title="Pro-Tech Diagnostic", page_icon="🛠", layout="wide")
    
    st.title("Professional IT Diagnostic System")
    st.markdown("---")

    # Sidebar for instructions or history
    with st.sidebar:
        st.header("Instructions")
        st.info("Select the symptoms you are observing. The engine will use forward-chaining logic to determine the root cause.")
        if st.button("Reset Session"):
            st.rerun()

    # Organized Input Section
    st.subheader("Step 1: Identify Symptoms")
    
    # Using a multiselect is cleaner than many checkboxes
    # You can also group FACTS if you update your FACTS file to a dictionary
    selected_symptoms = st.multiselect(
        "Search or select symptoms below:",
        options=FACTS,
        format_func=lambda x: x.replace("_", " ").capitalize(),
        help="Select all conditions that apply to the current state of the hardware."
    )

    st.markdown("---")

    # Execution Section
    if st.button("Run System Diagnostic", type="primary"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom to begin.")
        else:
            service = DiagnosisService()
            # Passing set for efficient lookups in your forward_chain
            results, fired_rules = service.diagnose(set(selected_symptoms))

            if results:
                st.subheader("Step 2: Analysis Results")
                
                # Layout results in columns if multiple exist
                for r in results:
                    with st.container():
                        col1, col2 = st.columns([1, 3])
                        
                        with col1:
                            # Displaying confidence as a metric
                            st.metric(label="Confidence", value=f"{int(r['confidence']*100)}%")
                        
                        with col2:
                            st.error(f"**Detected Issue:** {r['issue'].replace('_', ' ').title()}")
                            
                        # Use an expander for the solution to keep things tidy
                        with st.expander("View Recommended Solution"):
                            st.write(r['solution'])
                    st.divider()

                # Explanation Engine Section
                st.subheader("Step 3: Logical Explanation")
                with st.expander("Show Inference Path"):
                    explanations = explain(fired_rules)
                    for e in explanations:
                        st.write(f"{e}")
            else:
                st.error("Inconclusive: No rules matched the provided symptoms.")