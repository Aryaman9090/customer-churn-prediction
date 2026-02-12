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
# Visualization
<img width="552" height="441" alt="f0507b4b-eaa7-4e5a-95bc-25520882447d" src="https://github.com/user-attachments/assets/7e0f2903-61d6-46e7-babf-9f341a4c5614" />
<img width="543" height="441" alt="ad7558e4-5cda-432a-ad70-3eaa125a1d7d" src="https://github.com/user-attachments/assets/d09f17d8-e672-4214-97b5-bdfb045e7d12" />
<img width="552" height="494" alt="b6cb63a5-a303-45f5-b5c8-7abde19b0239" src="https://github.com/user-attachments/assets/1aafa451-a14b-40b6-b91b-7d784297fed2" />
<img width="543" height="494" alt="4b7b9e67-d83d-4628-bf2e-861c59411351" src="https://github.com/user-attachments/assets/0b331b50-8366-4e8f-97bc-fc98400ab6cc" />
<img width="543" height="494" alt="caff79d5-67e3-4ea3-84cb-63a978d99de1" src="https://github.com/user-attachments/assets/4f64aa38-0f65-409b-ae6d-37bbb58d80a5" />
<img width="552" height="510" alt="824eedbf-1e62-41f6-81e2-6270d0452e61" src="https://github.com/user-attachments/assets/54aa8f1b-0914-4fc3-ab4b-ffebdab938b6" />
<img width="1209" height="452" alt="80dfcc5e-5334-4151-9f2f-b8b5ba7c2c1b" src="https://github.com/user-attachments/assets/68a11c71-68e1-4599-af16-c61dff5e5952" />

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


