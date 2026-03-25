import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc
)

from sklearn.model_selection import cross_val_score


# ==============================
# Model Evaluation
# ==============================
def evaluate_model(name, model, x_test, y_test):

    print(f"\n{'='*50}")
    print(f"Model: {name}")
    print(f"{'='*50}")

    y_pred = model.predict(x_test)

    acc = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy : {acc:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    cm = confusion_matrix(y_test, y_pred)

    ConfusionMatrixDisplay(cm).plot()

    plt.title(f"Confusion Matrix - {name}")

    plt.show()


# ==============================
# ROC Curve
# ==============================
def plot_roc(models, x_test, y_test):

    plt.figure()

    for name, model in models.items():

        if hasattr(model, "predict_proba"):

            y_prob = model.predict_proba(x_test)[:, 1]

        else:
            continue

        fpr, tpr, _ = roc_curve(y_test, y_prob)

        roc_auc = auc(fpr, tpr)

        plt.plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")

    plt.plot([0,1],[0,1],'--')

    plt.xlabel("False Positive Rate")

    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    plt.legend()

    plt.show()


# ==============================
# Cross Validation
# ==============================
def run_cross_validation(model, x_train, y_train):

    scores = cross_val_score(
        model,
        x_train,
        y_train,
        cv=5,
        scoring='f1'
    )

    print("\nCross Validation F1 Scores:", scores)

    print("Average F1 Score:", scores.mean())


# ==============================
# Error Analysis
# ==============================
def error_analysis(model, X_test, y_test, X_test_text):

    y_pred = model.predict(X_test)

    error_df = pd.DataFrame({
        "Text": X_test_text,
        "Actual": y_test,
        "Predicted": y_pred
    })

    errors = error_df[error_df["Actual"] != error_df["Predicted"]]

    return errors


# ==============================
# Important Spam Words
# ==============================
def show_top_spam_words(model, vectorizer, n=20):

    feature_names = vectorizer.get_feature_names_out()

    top = model.coef_[0].argsort()[-n:]

    print("\nImportant Spam Words:\n")

    for i in top:
        print(feature_names[i])