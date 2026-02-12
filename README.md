# Customer Churn Prediction

This project predicts whether a telecom customer will leave the company (churn) or stay.

The goal is to help businesses identify customers who may leave so they can take action and reduce revenue loss.

---

# Project Overview

* Problem: Predict customer churn (Yes or No)
* Model Used: Random Forest Classifier
* Total Customers: 949
* Test Samples: 190
* Tools Used: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Joblib

Customer churn is a serious business problem because when customers leave, companies lose money. This model helps identify risky customers early.

---

# Dataset Information

Total Records: 949

Average Age: 44.65 years
Average Tenure: 19.99 months
Average Monthly Charges: 74.23
Average Total Charges: 1479.84

Main Features:

* CustomerID – Unique ID
* Age – Customer age
* Tenure – Months with company
* MonthlyCharges – Monthly cost
* TotalCharges – Total amount paid
* ContractType – Type of contract
* InternetService – Type of internet
* TechSupport – Yes or No
* Gender – Male or Female
* Churn – Target (Yes = Left, No = Stayed)

---

# Exploratory Data Analysis (EDA)

After analyzing the data, we found:

* Some contract types have higher churn.
* Customers without tech support leave more often.
* Higher monthly charges are linked to higher churn.
* Tenure affects customer loyalty.
* Fiber optic internet users are a large part of the data.

We created visual charts such as:

* Churn distribution
* Gender vs churn
* Internet service distribution
* Age vs tenure
* Charges distribution

---

# Data Preprocessing

Before training the model, we cleaned the data:

* Filled missing values in InternetService
* Removed duplicate rows
* Cleaned invalid TotalCharges values
* Converted categorical columns into numeric format
* Split data into 80% training and 20% testing

Clean data improves model accuracy.

---

# Model Development

We used a Random Forest Classifier.

Steps:

1. Split data into train and test sets
2. Applied 5-fold cross validation
3. Trained the model
4. Evaluated performance
5. Saved the model

Random Forest was chosen because it:

* Works well with mixed data
* Reduces overfitting
* Handles complex patterns

---

# Model Evaluation

Classification Results:

* Accuracy: 1.00
* Precision: 1.00
* Recall: 1.00
* F1 Score: 1.00

Confusion Matrix:

[[ 24   0]
[  0 166]]

Total Test Samples: 190

The model correctly predicted all test cases.

Note: In real business situations, perfect accuracy is rare. This result shows strong performance on this dataset.

---

# Key Insights

* Contract type affects churn.
* No tech support increases churn risk.
* High monthly charges increase churn probability.
* Tenure strongly impacts retention.

These insights can help companies improve customer retention strategies.

---

# Deployment

The trained model was saved using:

joblib.dump(rf, "churn_model.pkl")

This file can be used in:

* Streamlit web app
* API
* Business dashboard
* Automation systems

---

# Conclusion

This project shows a complete machine learning process:

* Data Cleaning
* Data Analysis
* Feature Preparation
* Model Training
* Model Evaluation
* Model Saving

This churn prediction model can help businesses reduce customer loss and improve long-term growth.


