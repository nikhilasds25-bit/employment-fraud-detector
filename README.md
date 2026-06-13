# 🛡️ Employment Fraud Detector

## Live Demo

🚀 Try the deployed application:

https://employment-fraud-detector-danbudd3v8zz94vx8xkdv9.streamlit.app/

---

# Project Overview

Employment fraud and fake job advertisements have become increasingly common across online job portals. Fraudulent postings often deceive job seekers by promising unrealistic salaries, requiring upfront payments, or offering guaranteed employment without proper recruitment procedures.

The Employment Fraud Detector is a Machine Learning-based web application that analyzes job descriptions and predicts whether a job posting is:

* ✅ Genuine Job Posting
* 🚨 Fraudulent Job Posting

The system uses Natural Language Processing (NLP), TF-IDF feature extraction, structured feature engineering, and machine learning models to classify job advertisements.

---

# Features

* Interactive Streamlit web application
* Real-time job posting analysis
* NLP-based fraud detection
* Confidence score generation
* Model comparison framework
* Fully deployed online
* Multiple trained models stored for experimentation

---

# Dataset

This project uses the Fake Job Postings Dataset containing both legitimate and fraudulent job advertisements.

Dataset Size:

* Total Records: 17,880
* Genuine Jobs: 17,014
* Fraudulent Jobs: 866

Dataset Attributes:

* Job Title
* Company Profile
* Description
* Requirements
* Benefits
* Industry
* Employment Type
* Experience Level
* Education Requirements

Multiple textual columns were combined into a single feature to improve fraud detection performance.

---

# Exploratory Data Analysis (EDA)

## Fraud Distribution

* Genuine Jobs: 95.16%
* Fraudulent Jobs: 4.84%

## Company Logo Analysis

* Genuine Jobs: 81.9%
* Fraudulent Jobs: 32.7%

## Screening Questions

* Genuine Jobs: 50.2%
* Fraudulent Jobs: 28.8%

## Remote Jobs

* Genuine Jobs: 4.1%
* Fraudulent Jobs: 7.4%

These observations motivated the inclusion of structured features in later model versions.

---

# Machine Learning Pipeline

## Data Preprocessing

* Missing value handling
* Text cleaning
* Feature selection
* Combined text generation

## Feature Extraction

### TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual job postings into numerical vectors suitable for machine learning algorithms.

---

# Model Development

## Version 1 — Logistic Regression

### Model

* Logistic Regression
* Class Weight Balancing

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 97%   |
| Fraud Recall   | 88%   |
| Fraud F1 Score | 73%   |

### Confusion Matrix

|                | Predicted Genuine | Predicted Fraud |
| -------------- | ----------------- | --------------- |
| Actual Genuine | 3310              | 93              |
| Actual Fraud   | 20                | 153             |

### Status

✅ Deployed in Streamlit

---

## Version 2 — XGBoost Classifier

### Model

* XGBoost Classifier

Parameters:

* n_estimators = 100
* max_depth = 6
* learning_rate = 0.1
* random_state = 42

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 98%   |
| Fraud Recall   | 63%   |
| Fraud F1 Score | 77%   |

### Confusion Matrix

|                | Predicted Genuine | Predicted Fraud |
| -------------- | ----------------- | --------------- |
| Actual Genuine | 3403              | 0               |
| Actual Fraud   | 64                | 109             |

### Status

✅ Trained and Saved

---

## Version 3.1 — XGBoost + Structured Features

### Additional Features

* has_company_logo
* has_questions
* telecommuting

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 98%   |
| Fraud Recall   | 69%   |
| Fraud F1 Score | 81%   |

### Confusion Matrix

|                | Predicted Genuine | Predicted Fraud |
| -------------- | ----------------- | --------------- |
| Actual Genuine | 3401              | 2               |
| Actual Fraud   | 53                | 120             |

### Status

✅ Trained and Saved

---

## Version 3.2 — Logistic Regression + Structured Features

### Additional Features

* has_company_logo
* has_questions
* telecommuting

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 96%   |
| Fraud Recall   | 90%   |
| Fraud F1 Score | 68%   |

### Status

✅ Trained and Saved

---

# Extended Model Comparison

| Version | Model                                     | Accuracy | Fraud Recall | Fraud F1 |
| ------- | ----------------------------------------- | -------- | ------------ | -------- |
| V1      | Logistic Regression                       | 97%      | 88%          | 73%      |
| V2      | XGBoost                                   | 98%      | 63%          | 77%      |
| V3.1    | XGBoost + Structured Features             | 98%      | 69%          | 81%      |
| V3.2    | Logistic Regression + Structured Features | 96%      | 90%          | 68%      |

---

# Final Deployment Decision

Although newer models achieved improvements in specific metrics, Version 1 Logistic Regression remains the deployed model because it provides a strong balance between fraud detection performance, stability, and simplicity.

The project continues to explore alternative models and feature engineering approaches for future deployment candidates.

---

# Important Fraud Indicators Discovered

Top fraud-associated keywords identified by Logistic Regression:

* link
* aptitude
* entry
* money
* financing
* earn
* clerk
* administrative
* gas
* optical
* offshore
* engineering
* hospital
* oil
* cash
* assistant
* accountant

These terms were identified through coefficient analysis.

---

# Project Structure

employment-fraud-detector/

├── app/

│ └── app.py

├── data/

│ └── fake_job_postings.csv

├── models/

│ ├── logistic_fraud_detector.pkl

│ ├── xgboost_fraud_detector.pkl

│ ├── xgboost_structured_v3_1.pkl

│ ├── logistic_structured_v3_2.pkl

│ └── tfidf_vectorizer.pkl

├── notebooks/

│ └── eda.ipynb

├── requirements.txt

└── README.md

---

# Technologies Used

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* Logistic Regression
* XGBoost

## NLP

* TF-IDF Vectorization

## Deployment

* Streamlit
* Streamlit Community Cloud

## Libraries

* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Streamlit

---

# Future Enhancements

## Version 4 — Trust Score Engine

Additional verification signals:

* Company website validation
* Domain reputation checks
* Email verification
* Company authenticity scoring

Goal:

Generate a trust score alongside machine learning predictions.

---

## Version 5 — Transformer-Based NLP Models

Models under consideration:

* DistilBERT
* MiniLM
* BERT

Objectives:

* Context-aware language understanding
* Improved semantic analysis
* Better fraud detection performance

---

# Long-Term Goals

* Explainable AI (XAI)
* REST API deployment
* Multi-language support
* Ensemble learning approaches
* Real-time job portal integration
* Automated company verification pipeline

---

# Author

Nikhil A S

MSc Data Science with Bio AI

GitHub:

https://github.com/nikhilasds25-bit

---

## License

This project is intended for educational and research purposes.

