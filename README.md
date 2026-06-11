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

The system uses Natural Language Processing (NLP), TF-IDF feature extraction, and machine learning models to classify job advertisements.

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

Dataset size:

* Total Records: 17,880
* Genuine Jobs: 17,014
* Fraudulent Jobs: 866

The dataset contains:

* Job Title
* Company Profile
* Description
* Requirements
* Benefits
* Industry
* Employment Type
* Experience Level
* Education Requirements

Multiple textual columns were combined into a single text feature to improve fraud detection performance.

---

# Exploratory Data Analysis (EDA)

Key findings from the dataset:

### Fraud Distribution

* Genuine Jobs: 95.16%
* Fraudulent Jobs: 4.84%

### Company Logo Analysis

Average company logo presence:

* Genuine Jobs: 81.9%
* Fraudulent Jobs: 32.7%

### Screening Questions

Average presence of screening questions:

* Genuine Jobs: 50.2%
* Fraudulent Jobs: 28.8%

### Remote Jobs

Average telecommuting rate:

* Genuine Jobs: 4.1%
* Fraudulent Jobs: 7.4%

These insights were later used to design future feature engineering improvements.

---

# Machine Learning Pipeline

## Data Preprocessing

* Missing value handling
* Text cleaning
* Feature selection
* Combined text feature generation

## Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency)

Used to transform job postings into numerical feature vectors suitable for machine learning models.

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

Confusion Matrix:

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

Confusion Matrix:

|                | Predicted Genuine | Predicted Fraud |
| -------------- | ----------------- | --------------- |
| Actual Genuine | 3403              | 0               |
| Actual Fraud   | 64                | 109             |

### Status

✅ Trained and Saved

---

# Model Comparison

| Metric         | Logistic Regression | XGBoost |
| -------------- | ------------------- | ------- |
| Accuracy       | 97%                 | 98%     |
| Fraud Recall   | 88%                 | 63%     |
| Fraud F1 Score | 73%                 | 77%     |

## Final Deployment Decision

Although XGBoost achieved slightly higher overall accuracy and F1-score, Logistic Regression achieved significantly higher fraud recall.

Since the primary goal of this project is detecting fraudulent job advertisements, Logistic Regression was selected as the deployed model because missing fraudulent jobs is more costly than incorrectly flagging legitimate ones.

---

# Important Fraud Indicators Discovered

Top fraud-associated keywords identified by the Logistic Regression model:

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

These terms were identified through model coefficient analysis.

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

# Installation

Clone the repository:

git clone https://github.com/nikhilasds25-bit/employment-fraud-detector.git

Navigate to the project folder:

cd employment-fraud-detector

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app/app.py

---

# Future Enhancements

## Version 3

Feature Engineering

Additional structured features:

* has_company_logo
* has_questions
* telecommuting
* employment_type
* required_experience
* required_education

Goal:

Combine structured and textual information to improve fraud detection.

---

## Version 4

Trust Score Engine

Additional verification signals:

* Company website validation
* Domain reputation checks
* Email verification
* Company authenticity scoring

Goal:

Generate a trust score alongside machine learning predictions.

---

## Version 5

Transformer-Based NLP Models

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
