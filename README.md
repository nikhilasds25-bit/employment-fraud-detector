# employment-fraud-detector

# 🛡️ Employment Fraud Detector

## Live Demo

🚀 Try the deployed application:

https://employment-fraud-detector-danbudd3v8zz94vx8xkdv9.streamlit.app/

---

## Project Overview

Employment fraud and fake job advertisements have become increasingly common across online job portals. Fraudulent postings often deceive job seekers by promising unrealistic salaries, requiring upfront payments, or offering guaranteed employment without proper recruitment procedures.

The Employment Fraud Detector is a Machine Learning-based web application that analyzes job descriptions and predicts whether a job posting is:

* ✅ Genuine Job Posting
* 🚨 Fraudulent Job Posting

The application is built using Logistic Regression and TF-IDF text vectorization and is deployed using Streamlit Community Cloud.

---

## Features

* Interactive web application using Streamlit
* Real-time job posting analysis
* Fraud detection using Machine Learning
* Confidence score for each prediction
* Simple and user-friendly interface
* Fully deployed and accessible online

---

## Dataset

This project uses the Fake Job Postings Dataset, which contains job advertisements labeled as either genuine or fraudulent.

The dataset includes information such as:

* Job title
* Company profile
* Job description
* Requirements
* Benefits
* Employment type
* Industry information

For training, multiple textual fields were combined into a single feature to improve fraud detection performance.

---

## Machine Learning Pipeline

### Data Preprocessing

* Missing value handling
* Text cleaning
* Feature selection
* Combined text generation

### Feature Extraction

TF-IDF (Term Frequency–Inverse Document Frequency) was used to convert textual job postings into numerical vectors.

### Model Training

Algorithm used:

* Logistic Regression
* Class Weight Balancing

Model and vectorizer were saved using Joblib.

---

## Project Structure

employment-fraud-detector/

├── app/
│   └── app.py

├── models/
│   ├── logistic_fraud_detector.pkl
│   └── tfidf_vectorizer.pkl

├── data/
│   └── fake_job_postings.csv

├── requirements.txt

└── README.md

---

## Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorization

### Deployment

* Streamlit
* Streamlit Community Cloud

### Libraries

* Pandas
* NumPy
* Joblib

---

## Installation

Clone the repository:

git clone https://github.com/nikhilasds25-bit/employment-fraud-detector.git

Navigate to the project folder:

cd employment-fraud-detector

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app/app.py

---

## Example Prediction

### Fraudulent Posting

Input:

"Earn ₹80,000 per month working only 2 hours a day. No experience required. Registration fee refundable after joining."

Prediction:

🚨 Fraudulent Job Posting

Confidence: High

---

## Future Enhancements

This project follows an iterative machine learning development approach where each version improves upon the previous one.

### Version 1 (Current Release)

**Model:** Logistic Regression

**Features:**

* TF-IDF Vectorization
* Combined text feature generation
* Fraud prediction with confidence score
* Streamlit web application deployment

**Status:** Deployed and Operational

### Version 2 (Planned)

**Model:** XGBoost Classifier

**Objectives:**

* Improve classification performance
* Hyperparameter tuning
* Compare results with Logistic Regression
* Evaluate Precision, Recall, F1-Score, and ROC-AUC

### Version 3 (Planned)

**Enhanced Feature Engineering**

Additional structured features:

* has_company_logo
* has_questions
* telecommuting
* employment_type
* required_experience

**Goal:**
Improve detection performance by combining textual and structured information.

### Version 4 (Planned)

**Trust Score System**

Additional verification signals:

* Company website validation
* Domain age analysis
* Domain reputation checks
* Email domain verification

**Goal:**
Generate a trust score that complements machine learning predictions.

### Version 5 (Planned)

**Transformer-Based NLP Models**

Models under consideration:

* DistilBERT
* MiniLM
* BERT

**Objectives:**

* Context-aware language understanding
* Improved semantic analysis
* Better detection of sophisticated fraudulent postings

### Long-Term Goals

* Explainable AI (XAI)
* Model comparison dashboard
* REST API deployment
* Multi-language support
* Real-time job portal integration
* Automated company verification pipeline

---

## Model Versioning Strategy

To support reproducibility and model comparison, each trained model will be stored separately.

Example:

models/

├── logistic_fraud_detector_v1.pkl

├── xgboost_fraud_detector_v2.pkl

├── bert_fraud_detector_v3.pkl

└── tfidf_vectorizer.pkl

This approach allows performance comparison across multiple machine learning models and supports continuous improvement of the Employment Fraud Detector.

---

## Results

Current deployed model:

| Model               | Feature Extraction | Deployment      |
| ------------------- | ------------------ | --------------- |
| Logistic Regression | TF-IDF             | Streamlit Cloud |

The current release serves as the baseline model for future improvements and experimentation.


---

## Author

Nikhil A S

Machine Learning and Data Analytics Enthusiast

GitHub:
https://github.com/nikhilasds25-bit

---

## License

This project is intended for educational and research purposes.
