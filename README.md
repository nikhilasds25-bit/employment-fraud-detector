# 🛡️ Employment Fraud Detector

## Live Demo

🚀 Try the deployed application:

https://employment-fraud-detector-danbudd3v8zz94vx8xkdv9.streamlit.app/

---

# Project Overview

Employment fraud and fake job advertisements have become increasingly common across online job portals. Fraudulent postings often deceive job seekers by promising unrealistic salaries, requiring upfront payments, requesting sensitive personal information, or offering guaranteed employment without a proper recruitment process.

The Employment Fraud Detector is an end-to-end Machine Learning and Natural Language Processing (NLP) project designed to automatically identify potentially fraudulent job advertisements.

The system analyzes job posting content and predicts whether a job advertisement is:

* ✅ Genuine Job Posting
* 🚨 Fraudulent Job Posting

The project evolved through multiple versions, beginning with traditional machine learning algorithms and progressing toward advanced Transformer-based Natural Language Processing models.

The final system incorporates:

* NLP-based text classification
* TF-IDF feature engineering
* Structured feature analysis
* Explainable Trust Score Engine
* Risk Explanation Engine
* Transformer-based Deep Learning (DistilBERT)
* Interactive Streamlit deployment

---

# Features

* Interactive Streamlit web application
* Real-time job posting analysis
* NLP-based fraud detection
* Confidence score generation
* Trust Score Engine
* Risk Explanation System
* Multiple model comparison framework
* Traditional Machine Learning models
* Transformer-based Deep Learning models
* Fully deployed online
* Explainable fraud risk assessment

---

# Dataset

This project uses the Fake Job Postings Dataset containing both legitimate and fraudulent job advertisements.

## Dataset Size

| Category        | Count  |
| --------------- | ------ |
| Total Records   | 17,880 |
| Genuine Jobs    | 17,014 |
| Fraudulent Jobs | 866    |

## Target Variable

fraudulent

* 0 = Genuine Job Posting
* 1 = Fraudulent Job Posting

## Dataset Attributes

The dataset contains multiple structured and textual features including:

* Job Title
* Company Profile
* Job Description
* Requirements
* Benefits
* Industry
* Employment Type
* Experience Level
* Education Requirements
* Company Logo Availability
* Screening Questions
* Remote Work Indicator

To improve text understanding, multiple textual fields were combined into a single NLP feature.

---

# Exploratory Data Analysis (EDA)

EDA was performed to understand the characteristics of fraudulent job postings and identify useful predictive signals.

## Fraud Distribution

| Class           | Percentage |
| --------------- | ---------- |
| Genuine Jobs    | 95.16%     |
| Fraudulent Jobs | 4.84%      |

The dataset is highly imbalanced, making fraud detection a challenging classification problem.

---

## Company Logo Analysis

| Category        | Has Logo |
| --------------- | -------- |
| Genuine Jobs    | 81.9%    |
| Fraudulent Jobs | 32.7%    |

Observation:

Fraudulent postings are significantly less likely to contain a company logo.

---

## Screening Questions Analysis

| Category        | Has Questions |
| --------------- | ------------- |
| Genuine Jobs    | 50.2%         |
| Fraudulent Jobs | 28.8%         |

Observation:

Legitimate employers are more likely to include screening questions.

---

## Remote Job Analysis

| Category        | Remote Jobs |
| --------------- | ----------- |
| Genuine Jobs    | 4.1%        |
| Fraudulent Jobs | 7.4%        |

Observation:

Fraudulent postings appear more frequently among remote job advertisements.

---

# Text Feature Engineering

The following columns were merged into a single NLP feature:

* title
* company_profile
* description
* requirements
* benefits

```python
df["text"] = (
    df["title"].fillna("") + " " +
    df["company_profile"].fillna("") + " " +
    df["description"].fillna("") + " " +
    df["requirements"].fillna("") + " " +
    df["benefits"].fillna("")
)
```

This combined text became the primary input for machine learning and transformer models.

---

# Machine Learning Pipeline

## Data Preprocessing

* Missing value handling
* Text cleaning
* Feature engineering
* Dataset balancing considerations
* Text concatenation

---

## Feature Extraction

### TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual job advertisements into numerical vectors.

Advantages:

* Lightweight
* Fast inference
* Interpretable
* Effective baseline for NLP classification

---

# Model Development

## Version 1 — Logistic Regression

### Objective

Build a baseline fraud detection model using TF-IDF features.

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 97%   |
| Fraud Recall   | 88%   |
| Fraud F1 Score | 73%   |

### Status

✅ Deployed in Streamlit

---

## Version 2 — XGBoost Classifier

### Objective

Improve fraud detection using gradient boosted decision trees.

### Performance

| Metric         | Value |
| -------------- | ----- |
| Accuracy       | 98%   |
| Fraud Recall   | 63%   |
| Fraud F1 Score | 77%   |

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

# Version 4 — Trust Score Engine

## Objective

Traditional machine learning models only provide a prediction.

Version 4 introduces an explainable trust scoring framework that helps users understand why a job posting may be risky.

---

## Risk Signals Used

* Company logo availability
* Presence of screening questions
* Remote work indicator
* Fraud probability generated by the model

---

## Trust Score

The system generates a score between:

0 – 100

Higher Score:

* More trustworthy job posting

Lower Score:

* Higher fraud risk

---

## Risk Explanation Engine

Human-readable explanations include:

* Company logo missing
* No screening questions
* Remote position
* Elevated fraud probability
* Multiple risk indicators detected

---

## Status

✅ Completed

---

# Version 5 — DistilBERT Transformer Model

## Objective

The primary goal of Version 5 was to evaluate whether Transformer-based Natural Language Processing could outperform traditional machine learning approaches.

DistilBERT was selected because it provides most of the performance benefits of BERT while being significantly smaller and faster.

---

## Why DistilBERT?

Traditional models such as TF-IDF + Logistic Regression rely on word frequencies and manually engineered features.

DistilBERT uses contextual language understanding.

This allows the model to understand:

* Semantic meaning
* Context between words
* Sentence structure
* Relationships across long job descriptions

Unlike TF-IDF, DistilBERT can understand that:

"Earn money immediately with no experience required"

may indicate suspicious behavior even if exact keywords vary.

---

## Training Configuration

* Model: distilbert-base-uncased
* Epochs: 3
* Batch Size: 8
* Sequence Length: 256
* Framework: Hugging Face Transformers
* Backend: PyTorch

Training was performed on approximately 17,880 job postings.

Training time:

⏱️ Approximately 5 hours

---

## DistilBERT Performance

### Classification Report

| Metric          | Value |
| --------------- | ----- |
| Accuracy        | 99%   |
| Fraud Precision | 91%   |
| Fraud Recall    | 86%   |
| Fraud F1 Score  | 88%   |

### Confusion Matrix

```text
[[3388   15]
 [  24  149]]
```

---

## Key Result

DistilBERT achieved the highest Fraud F1 Score across all project versions.

The model significantly improved overall fraud classification performance while maintaining strong recall.

---

## Status

✅ Trained

✅ Evaluated

✅ Saved

✅ Best Overall Model

---

# Complete Model Comparison

| Version | Model                                     | Accuracy | Fraud Recall | Fraud F1 |
| ------- | ----------------------------------------- | -------- | ------------ | -------- |
| V1      | Logistic Regression                       | 97%      | 88%          | 73%      |
| V2      | XGBoost                                   | 98%      | 63%          | 77%      |
| V3.1    | XGBoost + Structured Features             | 98%      | 69%          | 81%      |
| V3.2    | Logistic Regression + Structured Features | 96%      | 90%          | 68%      |
| V5      | DistilBERT Transformer                    | 99%      | 86%          | 88%      |

---

# Deployment Status

Current Streamlit Deployment:

✅ Logistic Regression

Reason:

* Lightweight
* Fast inference
* Minimal memory usage

Future Deployment Candidate:

🏆 DistilBERT

Reason:

* Best overall performance
* Highest Fraud F1 Score
* Context-aware language understanding

---

# Project Structure

```text
employment-fraud-detector/

├── app/
│   └── app.py

├── data/
│   └── fake_job_postings.csv

├── models/
│   ├── logistic_fraud_detector.pkl
│   ├── xgboost_fraud_detector.pkl
│   ├── xgboost_structured_v3_1.pkl
│   ├── logistic_structured_v3_2.pkl
│   ├── tfidf_vectorizer.pkl
│   └── distilbert_v5/

├── notebooks/
│   ├── eda.ipynb
│   ├── version4_trust_score.ipynb
│   └── version5_distilbert.ipynb

├── requirements.txt

└── README.md
```

---

# Future Enhancements

* DistilBERT deployment in Streamlit
* Explainable AI (XAI)
* SHAP-based model interpretation
* REST API deployment
* Multi-language fraud detection
* Ensemble learning approaches
* Automated company verification
* Real-time job portal integration

---

# Author

Nikhil A S

MSc Data Science with Bio AI

GitHub:

https://github.com/nikhilasds25-bit

---

# License

This project is intended for educational, research, and learning purposes.

This project is intended for educational and research purposes.

