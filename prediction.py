import joblib
import re
from src.preprocessing import clean_text

model = joblib.load("models/spam_detector.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_email(text):

    text = clean_text(text)
    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]
    prob = model.predict_proba(text_vector)[0][1]

    label = "THREAT / SPAM" if prediction == 1 else "SAFE EMAIL"

    score = int(prob * 100)

    if score > 80:
        level = "HIGH"
    elif score > 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    suspicious_words_list = [
        "verify",
        "password",
        "bank",
        "login",
        "account",
        "urgent",
        "click",
        "secure",
        "update"
    ]

    found_words = []

    for word in suspicious_words_list:
        if word in text.lower():
            found_words.append(word)

    urls = re.findall(r'http[s]?://\S+', text)

    explanation = []

    if urls:
        explanation.append("Email contains suspicious links")

    if found_words:
        explanation.append("Contains phishing keywords")

    if prob > 0.8:
        explanation.append("Model strongly confident email is malicious")

    return {
        "prediction": label,
        "probability": round(prob,3),
        "threat_score": score,
        "threat_level": level,
        "suspicious_words": found_words,
        "urls": urls,
        "explanation": explanation
    }