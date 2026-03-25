import pandas as pd
import string
import re

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize tools
lm = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
stop_words.update([
    "escapenumber", "escapelong", "escapeurl",
    "http", "www", "com", "email"
])

stop_words.discard("not")
stop_words.discard("no")

exclude = string.punctuation


def clean_text(text):

    if pd.isna(text):
        return ""

    # Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # Replace URLs
    text = re.sub(r"http\S+|www\S+", " URL ", text)

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", exclude))

    # remove email addresses
    text = re.sub(r'\S+@\S+', ' EMAIL ', text)

    # remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove stopwords + lemmatize
    tokens = []
    for word in text.split():
        if word not in stop_words:
            lemma = lm.lemmatize(word)
            tokens.append(lemma)

    return " ".join(tokens).strip()


def preprocess_dataset():

    df = pd.read_csv("data/processed/final_email_dataset.csv")

    # Apply cleaning
    df["text"] = df["text"].apply(clean_text)

    # Remove empty rows
    df = df[df["text"].str.strip() != ""]

    # Save cleaned dataset
    df.to_csv("data/processed/final_email_cleaned.csv", index=False)

    print("Cleaned dataset saved.")

    return df
