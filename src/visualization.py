import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re


def threat_fusion_analysis(model, vectorizer, x_test, y_test, X_test_text):

    # -----------------------
    # Predictions
    # -----------------------
    y_pred = model.predict(x_test)

    df = pd.DataFrame({
        "text": X_test_text,
        "actual": y_test,
        "predicted": y_pred
    })

    # -----------------------
    # Word count
    # -----------------------
    df["word_count"] = df["text"].apply(lambda x: len(x.split()))

    # -----------------------
    # URL count
    # -----------------------
    df["url_count"] = df["text"].apply(
        lambda x: len(re.findall(r'http\S+|www\S+', x))
    )

    # -----------------------
    # Email count
    # -----------------------
    df["email_count"] = df["text"].apply(
        lambda x: len(re.findall(r'\S+@\S+', x))
    )

    # -----------------------
    # Threat Score
    # -----------------------
    df["threat_score"] = (
        df["word_count"] * 0.2 +
        df["url_count"] * 5 +
        df["email_count"] * 3 +
        df["predicted"] * 10
    )

    print("\nSample Analysis Data:")
    print(df.head())


    # ===================================
    # 📊 1 Prediction Distribution
    # ===================================
    plt.figure(figsize=(6,4))

    df["predicted"].value_counts().plot(kind="bar")

    plt.title("Prediction Distribution")
    plt.xlabel("Label (0 = Safe, 1 = Threat)")
    plt.ylabel("Count")

    plt.show()


    # ===================================
    # 📊 2 Email Length Trend
    # ===================================
    plt.figure(figsize=(10,6))

    sns.histplot(
        data=df,
        x="word_count",
        hue="predicted",
        bins=50
    )

    plt.xlim(0,200)

    plt.title("Email Length Distribution by Prediction")

    plt.show()


    # ===================================
    # 📊 3 Threat Score Distribution
    # ===================================
    plt.figure(figsize=(10,6))

    sns.histplot(df["threat_score"], bins=50)

    plt.title("Threat Score Distribution")

    plt.show()


    # ===================================
    # 📊 4 URL Usage Trend
    # ===================================
    plt.figure(figsize=(8,5))

    sns.boxplot(x="predicted", y="url_count", data=df)

    plt.title("URLs in Spam vs Safe Emails")

    plt.show()


    # ===================================
    # 📊 5 Top Words in Predicted Spam
    # ===================================
    spam_text = " ".join(df[df["predicted"]==1]["text"])

    spam_words = spam_text.split()

    word_freq = Counter(spam_words)

    common = word_freq.most_common(20)

    words = [w[0] for w in common]
    counts = [w[1] for w in common]

    plt.figure(figsize=(10,6))

    plt.bar(words, counts)

    plt.xticks(rotation=45)

    plt.title("Top Words in Predicted Spam")

    plt.show()


    return df
