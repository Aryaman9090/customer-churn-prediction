import streamlit as st
import pandas as pd
import joblib as jl
import matplotlib.pyplot as plt
import seaborn as sns

model = jl.load("churn_model.pkl")
df = pd.read_csv("C:\working office\customer_churn_data.csv")

st.header("Churn prediction")

tab1,tab2,tab3 = st.tabs(["Data","performace","predict"])

with tab1:
    st.subheader("Data used to build this model")
    df["InternetService"].fillna("Other",inplace = True)
    df.drop_duplicates(inplace = True)
    df = df[df["TotalCharges"]>0]
    st.dataframe(df)


with tab2:
    st.subheader("performace metric")
    pr = 1.00
    recall = 1.00
    accuracy = 1.00
    churn = "54.56%"
    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Precision",f"{pr:.2f}")
    col2.metric("Accuracy",f"{accuracy:.2f}")
    col3.metric("Recall",f"{recall:.2f}")
    col4.metric("Churn Rate",churn)

with tab3:
    st.subheader("Predict")

    # Inputs
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)
    contract_type = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "Other"])
    total_charges = st.number_input("Total Charges", min_value=0.0, value=600.0)
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

    # Encoding maps (must match training!)
    gender_map = {"Male": 0, "Female": 1, "Other": 2}
    contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
    internet_map = {"DSL": 0, "Fiber optic": 1, "Other": 2}
    tech_map = {"Yes": 1, "No": 0}

    # Button to trigger prediction
    if st.button("Predict Churn"):
        input_data = pd.DataFrame({
            "Age": [age],
            "Gender": [gender_map[gender]],
            "Tenure": [tenure],
            "MonthlyCharges": [monthly_charges],
            "ContractType": [contract_map[contract_type]],
            "InternetService": [internet_map[internet_service]],
            "TotalCharges": [total_charges],
            "TechSupport": [tech_map[tech_support]]
        })

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("⚠️ Customer predicted to CHURN")
        else:
            st.success("✅ Customer predicted to STAY")