import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("models/logistic_fraud_detector.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

st.set_page_config(
    page_title="Employment Fraud Detector",
    page_icon="🛡️"
)

st.title("🛡️ Employment Fraud Detector")

st.write(
    "Enter a job description below to predict whether it is "
    "a Genuine Job Posting or a Fraudulent Job Posting."
)

job_text = st.text_area(
    "Job Description",
    height=250
)

if st.button("Predict"):

    if job_text.strip() == "":
        st.warning("Please enter a job description.")
    else:

        transformed_text = tfidf.transform([job_text])

        prediction = model.predict(transformed_text)

        probability = model.predict_proba(transformed_text)

        if prediction[0] == 1:
            st.error("🚨 Fraudulent Job Posting")
            st.write(
                f"Confidence: {probability[0][1]*100:.2f}%"
            )
        else:
            st.success("✅ Genuine Job Posting")
            st.write(
                f"Confidence: {probability[0][0]*100:.2f}%"
            )
