from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC

from sklearn.ensemble import VotingClassifier, StackingClassifier


def train_models(x_train_tfidf, y_train):

    # -----------------------
    # Base Models
    # -----------------------

    model_lr = LogisticRegression(max_iter=500, class_weight="balanced")

    model_nb = MultinomialNB()

    model_svm = LinearSVC()


    # Train base models
    model_lr.fit(x_train_tfidf, y_train)
    model_nb.fit(x_train_tfidf, y_train)
    model_svm.fit(x_train_tfidf, y_train)


    # -----------------------
    # Voting Ensemble
    # -----------------------

    voting_model = VotingClassifier(
        estimators=[
            ('lr', model_lr),
            ('nb', model_nb),
            ('svm', model_svm)
        ],
        voting='hard'
    )

    voting_model.fit(x_train_tfidf, y_train)


    # -----------------------
    # Stacking Ensemble
    # -----------------------

    stack_model = StackingClassifier(
        estimators=[
            ('lr', model_lr),
            ('nb', model_nb),
            ('svm', model_svm)
        ],
        final_estimator=LogisticRegression(),
        passthrough=False
    )

    stack_model.fit(x_train_tfidf, y_train)


    return model_lr, model_nb, model_svm, voting_model, stack_model


