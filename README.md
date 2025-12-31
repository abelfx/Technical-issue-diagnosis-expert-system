# Hybrid Expert System – Technical Diagnosis Engine

**Author:** Abel Tesfa  
**Repository:** Technical Diagnosis Expert System  

---

## Overview

This project implements a **Hybrid Expert System for Technical Diagnosis**, designed to troubleshoot computer hardware and software failures using a **Symbolic AI approach**.

Unlike modern machine learning systems that rely on large datasets and operate as opaque *black boxes*, this system uses **explicit domain knowledge encoded as rules**, enabling deterministic, explainable, and auditable diagnoses.

The system integrates:
- Fuzzy logic for uncertainty handling  
- Priority-aware reasoning  
- A hybrid inference engine (forward + backward chaining)  

It produces not only diagnoses, but also **confidence scores**, **urgency prioritization**, and **human-readable explanations**, making it suitable for professional IT support, education, and safety-critical environments.

---

## Problem Definition

Modern IT troubleshooting depends heavily on human expertise, undocumented heuristics, and trial-and-error workflows. This results in:

- Inconsistent diagnoses across technicians  
- Slow resolution of complex or multi-layered faults  
- Poor knowledge transfer from senior experts to juniors  
- Difficulty auditing or justifying diagnostic decisions  

### Project Goal

To formalize expert troubleshooting knowledge into a system that can:

- Reason over explicit symptoms  
- Handle uncertainty in user-reported facts  
- Identify root causes through multi-step reasoning  
- Prioritize issues based on real-world risk  
- Provide transparent explanations for every conclusion  

---

## Why Expert Systems for Technical Diagnosis?

Expert Systems are particularly well-suited for IT diagnostics because technical faults are:

- **Causal** – symptoms map to underlying failures  
- **Rule-governed** – experts reason using IF–THEN logic  
- **High-risk** – incorrect actions can cause downtime or data loss  
- **Explainability-critical** – administrators must justify decisions  

Unlike perception-based domains (vision, speech, NLP), IT troubleshooting benefits from **structured symbolic reasoning** rather than statistical pattern recognition.

> *“If the machine shuts down under load AND the fan spins at maximum, suspect power supply instability.”*

---

## System Architecture

The system follows the **Classical Expert System Architecture**:

- **Knowledge Base** – Encoded expert knowledge  
- **Working Memory** – Current known facts with uncertainty  
- **Inference Engine** – Hybrid reasoning mechanism  

Each component is designed to support uncertainty handling, explainability, and priority-aware decision making.

---

## Knowledge Acquisition

Domain knowledge was **manually engineered** using:

- Real-world IT troubleshooting practices  
- Hardware and software diagnostic guides  
- Expert heuristics used by system administrators

## ⚡ Installation & Usage

Follow these steps to set up and run the **Hybrid Expert System – Technical Diagnosis Engine**.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Technical-Diagnosis-Expert-System.git
cd Technical-Diagnosis-Expert-System
```

### 2. Create a Virtual Environment (Recommended)

It is best to isolate dependencies using a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app.py
```

### 5. Using the System

Input system symptoms in the UI

- The engine provides:
- Diagnoses
- Confidence scores
- Priority-based alerts
- Human-readable explanations



