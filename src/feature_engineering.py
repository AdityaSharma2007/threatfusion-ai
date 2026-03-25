from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer


def prepare_features(df):

    # -----------------------
    # Split features/labels
    # -----------------------
    X = df["text"]
    y = df["label"]

    X_train_text, X_test_text, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # -----------------------
    # TF-IDF Vectorizer
    # -----------------------
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),     # unigrams + bigrams
        max_features=5000,
        min_df=3,               # ignore rare words
        max_df=0.9,             # ignore overly common words
        sublinear_tf=True,      # log scaling
        norm=None               # we will normalize manually
    )

    X_train = vectorizer.fit_transform(X_train_text)
    X_test = vectorizer.transform(X_test_text)

    # -----------------------
    # Normalization
    # -----------------------
    normalizer = Normalizer()

    X_train = normalizer.fit_transform(X_train)
    X_test = normalizer.transform(X_test)

    print("Train shape:", X_train.shape)
    print("Test shape:", X_test.shape)

    # return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer
    return X_train, X_test, y_train, y_test, vectorizer, X_test_text