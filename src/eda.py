import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud


def run_eda(df_final):

    # -------------------------
    # Word count
    # -------------------------
    df_final["word_count"] = df_final["text"].apply(lambda x: len(x.split()))

    # Remove very short emails
    df_final = df_final[df_final["word_count"] > 3]

    # Remove extreme outliers
    df_final = df_final[df_final["word_count"] < 1000]

    # -------------------------
    # Word Count Distribution
    # -------------------------
    plt.figure(figsize=(10,6))

    df_final["word_count"].hist(bins=50)

    plt.title("Word Count Distribution")
    plt.xlabel("Words per Email")
    plt.ylabel("Frequency")

    plt.xlim(0, 300)  # zoom for readability

    plt.show()

    # -------------------------
    # Text Length Distribution
    # -------------------------
    df_final["text_length"] = df_final["text"].apply(len)

    plt.figure(figsize=(10,6))

    df_final["text_length"].hist(bins=50)

    plt.title("Text Length Distribution")
    plt.xlabel("Characters per Email")
    plt.ylabel("Frequency")

    plt.xlim(0, 2000)

    plt.show()

    # -------------------------
    # Spam vs Safe Word Count
    # -------------------------
    plt.figure(figsize=(10,6))

    df_final[df_final["label"] == 1]["word_count"].hist(
        bins=50, alpha=0.5, label="Threat"
    )

    df_final[df_final["label"] == 0]["word_count"].hist(
        bins=50, alpha=0.5, label="Safe"
    )

    plt.legend()

    plt.title("Spam vs Safe Email Word Distribution")

    plt.xlim(0, 300)

    plt.show()

    # -------------------------
    # Class Distribution
    # -------------------------
    plt.figure(figsize=(6,6))

    df_final["label"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        labels=["Safe", "Threat"]
    )

    plt.title("Spam vs Safe Email Ratio")
    plt.ylabel("")

    plt.show()

    # -------------------------
    # Top 20 Spam Words
    # -------------------------
    spam_words = " ".join(df_final[df_final["label"] == 1]["text"]).split()

    spam_freq = Counter(spam_words)

    common_spam = spam_freq.most_common(20)

    words = [w[0] for w in common_spam]
    counts = [w[1] for w in common_spam]

    plt.figure(figsize=(10,6))

    plt.bar(words, counts)

    plt.xticks(rotation=45)

    plt.title("Top 20 Words in Spam Emails")

    plt.show()

    # -------------------------
    # Word Cloud (Spam)
    # -------------------------
    spam_text = " ".join(df_final[df_final["label"] == 1]["text"])

    wordcloud_spam = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(spam_text)

    plt.figure(figsize=(10,5))

    plt.imshow(wordcloud_spam)

    plt.axis("off")

    plt.title("Spam Word Cloud")

    plt.show()

    return df_final


# # Run EDA
# print(run_eda(pd.read_csv("../data/processed/final_email_cleaned.csv")))