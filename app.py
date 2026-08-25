import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Credit Risk Assessment", page_icon="🏦", layout="centered")
model = joblib.load("credit_default_model.pkl")

st.title("🏦 Credit Risk Assessment")
st.caption("Prototype — trained on public/synthetic data. Replace with Nashik Urban historical data before operational use.")

with st.form("borrower"):
    st.subheader("Borrower Information")
    cols = st.columns(2)
    vals = {}
    for i, field in enumerate(['Age', 'Income', 'LoanAmount', 'CreditScore', 'EmploymentYears', 'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 'PreviousDefault', 'Dependents', 'HasMortgage', 'HasCoSigner']):
        with cols[i % 2]:
            if field.lower() in ["previousdefault","hasmortgage","hacosigner","hascosigner"]:
                vals[field] = st.selectbox(field, [0,1], format_func=lambda x: "Yes" if x else "No")
            else:
                vals[field] = st.number_input(field, value=0.0)
    submitted = st.form_submit_button("Assess Credit Risk")

if submitted:
    row = pd.DataFrame([vals])
    pd_score = float(model.predict_proba(row)[:,1][0])
    risk = "LOW" if pd_score < .10 else ("MEDIUM" if pd_score < .25 else "HIGH")
    score = max(0, min(1000, round(1000*(1-pd_score))))
    st.metric("Probability of Default", f"{pd_score:.1%}")
    st.metric("Risk Score", f"{score} / 1000")
    st.subheader(f"Risk Category: {risk}")
    if risk == "LOW":
        st.success("Proceed subject to normal credit appraisal and Society policy.")
    elif risk == "MEDIUM":
        st.warning("Further credit assessment is recommended.")
    else:
        st.error("Enhanced due diligence / credit review is recommended.")
    st.info("This is a decision-support prototype, not an autonomous loan approval/denial system.")
