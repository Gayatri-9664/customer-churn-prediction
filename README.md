# Customer Churn Prediction using Snowflake ML

## 📌 Project Overview

Customer Churn Prediction is a machine learning classification project developed using Snowflake and Streamlit.

The system analyzes customer information such as tenure, contract type, internet service, payment method, monthly charges, and total charges to predict whether a customer is likely to churn.

## 🎯 Objective

The main objective is to build a machine learning model that can identify customers who may be at risk of leaving a service.

## 📊 Dataset

**Dataset:** Telco Customer Churn

**Original Records:** 7,043

**Records after data cleaning:** 7,032

**Features:** 19

**Target Variable:** Churn

## 🛠️ Technologies Used

* Python
* Snowflake
* Snowpark
* Pandas
* Scikit-learn
* Logistic Regression
* Random Forest
* Streamlit
* One-Hot Encoding
* StandardScaler

## 🤖 Machine Learning Models

Two classification models were trained and evaluated:

1. Logistic Regression
2. Random Forest

### Model Results

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| Logistic Regression |   80.38% |    64.76% | 57.49% |   60.91% |   0.836 |
| Random Forest       |   78.39% |    62.32% | 47.33% |   53.80% |   0.814 |

## 🏆 Selected Model

**Logistic Regression**

Test Accuracy: **80.38%**

ROC-AUC: **0.836**

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Selection
   ↓
Categorical Encoding
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Logistic Regression Selection
   ↓
Streamlit Application
   ↓
Customer Churn Prediction
```

## 🖥️ Streamlit Application

The Streamlit application allows users to enter customer information and receive a churn prediction with a churn probability.

### Application Features

* Customer information input
* Automatic feature encoding
* Logistic Regression prediction
* Churn probability
* Prediction result
* Model performance information

## 🚀 Deployed Application

[Customer Churn Prediction – Snowflake Streamlit App](https://stpcxvuymydahyh3zmacrr.awsapsouth1.snowflake.app/lwyayfu/hg09601/)

## 📁 Project Files

```text
customer-churn-prediction/
│
├── Customer_Churn_ML.ipynb
├── streamlit_app.py
└── README.md
```

## 📌 Conclusion

The project demonstrates an end-to-end customer churn prediction workflow using Snowflake for data processing and Streamlit for interactive prediction. Logistic Regression achieved 80.38% accuracy on the test dataset and was used in the deployed application.
