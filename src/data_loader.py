import pandas as pd

def load_datasets():

    df_email = pd.read_csv("data/raw/phishing_email.csv")

    df_spam = pd.read_csv(
        "data/raw/spam.csv",
        encoding="latin-1",
    )

    df_phishing = pd.read_csv("data/raw/combined_data.csv")

    df_enron = pd.read_csv("data/raw/enron_data_fraud_labeled.csv",low_memory=False )

    df_email.columns = ['text', 'label']

    df_spam = df_spam[['v1', 'v2']]
    df_spam.columns = ['label', 'text']

    df_spam['label'] = df_spam['label'].map({'ham': 0, 'spam': 1})

    # Combine subject + message
    df_enron["text"] = df_enron["Subject"].fillna('') + " " + df_enron["Body"].fillna('')

    # Keep only required columns
    df_enron = df_enron[["Label","text"]]
    df_enron.columns = ['label', 'text']

    # -------------------------
    # Merge all datasets
    # -------------------------
    df_final = pd.concat(
        [df_email, df_spam, df_phishing, df_enron],
        ignore_index=True
    )

    # Remove missing values
    df_final = df_final.dropna()

    # Save processed dataset
    df_final.to_csv(
        "data/processed/final_email_dataset.csv",
        index=False
    )

    print("Final dataset saved.")


    return df_final