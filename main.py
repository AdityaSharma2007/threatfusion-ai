import pandas as pd
import joblib

from src.data_loader import load_datasets
from src.preprocessing import preprocess_dataset
from src.eda import run_eda
from src.feature_engineering import prepare_features
from src.model_making import train_models
from src.model_evaluation import *
from src.visualization import threat_fusion_analysis


def main():

    print("\n========== Threat Fusion Pipeline Started ==========\n")

    # ==============================
    # Load dataset
    # ==============================
    print("Loading datasets...")
    df_merged = load_datasets()
    print("Data loaded successfully.\n")

    # ==============================
    # Preprocess dataset
    # ==============================
    print("Preprocessing datasets...")
    df_preprocessed = preprocess_dataset()
    print("Data preprocessing completed.\n")

    # ==============================
    # Load processed dataset
    # ==============================
    print("Loading cleaned dataset...")
    df = pd.read_csv("data/processed/final_email_cleaned.csv")
    print("Clean dataset loaded.\n")

    # ==============================
    # EDA
    # ==============================
    print("Running Exploratory Data Analysis (EDA)...")
    df = run_eda(df)
    print("EDA completed.\n")

    # ==============================
    # Feature Engineering
    # ==============================
    print("Preparing features (TF-IDF vectorization)...")
    X_train, X_test, y_train, y_test, vectorizer, X_test_text = prepare_features(df)
    print("Feature engineering completed.\n")

    # ==============================
    # Train Models
    # ==============================
    print("Training machine learning models...")
    model_lr, model_nb, model_svm, soft_voting_model, stack_model = train_models(
        X_train,
        y_train
    )
    print("Model training completed.\n")

    # ==============================
    # Model Creation
    # ==============================
    print("Saving trained models")

    joblib.dump(stack_model, "models/spam_detector.pkl")
    joblib.dump(model_svm, "models/spam_detector(svm).pkl")
    joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")

    print("Model ready.\n")

    # ==============================
    # Model Evaluation
    # ==============================
    print("Evaluating models...\n")

    evaluate_model("Logistic Regression", model_lr, X_test, y_test)
    evaluate_model("Naive Bayes", model_nb, X_test, y_test)
    evaluate_model("SVM", model_svm, X_test, y_test)
    evaluate_model("Hard Voting Ensemble", soft_voting_model, X_test, y_test)
    evaluate_model("Stack Voting Ensemble", stack_model, X_test, y_test)

    # ==============================
    # ROC Curve
    # ==============================
    print("\nGenerating ROC Curve...")
    plot_roc({
        "Logistic Regression": model_lr,
        "Naive Bayes": model_nb
    }, X_test, y_test)

    # ==============================
    # Cross Validation
    # ==============================
    print("\nRunning cross-validation...")
    run_cross_validation(soft_voting_model, X_train, y_train)

    # ==============================
    # Error Analysis
    # ==============================
    print("\nPerforming error analysis...")
    errors = error_analysis(
        soft_voting_model,
        X_test,
        y_test,
        X_test_text
    )

    print("\nMisclassified Emails:")
    print(errors.head(10))

    # ==============================
    # Important Spam Words
    # ==============================
    print("\nExtracting important spam words...")
    show_top_spam_words(model_lr, vectorizer)

    # ==============================
    # Threat Fusion Analysis
    # ==============================
    print("\nRunning Threat Fusion trend analysis...")
    analysis_df = threat_fusion_analysis(
        soft_voting_model,
        vectorizer,
        X_test,
        y_test,
        X_test_text
    )

    print("\n========== Pipeline Completed Successfully ==========\n")

    return analysis_df


if __name__ == "__main__":
    main()
#
#
#
#
# # ThreatFusion/
# # │
# # ├── data/
# # │   ├── raw/                 # original datasets
# # │   └── processed/           # cleaned datasets
# # │
# # ├── models/                  # saved ML models
# # │
# # ├── src/
# # │   ├── data_loader.py
# # │   ├── eda.py
# # │   ├── preprocessing.py
# # │   ├── feature_engineering.py
# # │   ├── model_making.py
# # │   ├── model_evaluation.py
# # │   └── visualization.py
# # │
# # ├── main.py
# # │
# # ├── app.py
# # │
# # ├── prediction.py
# # │
# # ├── requirements.txt
# # ├── README.md
# # └── .gitignore
#
