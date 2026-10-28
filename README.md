# Spam Message Detector

A beginner machine-learning demonstration that predicts whether entered text resembles spam or not spam.

## Problem statement

Unwanted messages can contain misleading offers or requests. This project demonstrates how a text-classification model can learn from labelled messages and produce a prediction for new text.

## Objectives

- Build a genuine text classifier using scikit-learn.
- Convert text to numeric TF-IDF features.
- Train a Multinomial Naive Bayes classifier.
- Provide a simple Streamlit interface and explain its limitations.

## Technologies

- Python
- Streamlit
- scikit-learn (`TfidfVectorizer`, `MultinomialNB`, `Pipeline`)

## Dataset and limitations

The current app uses 16 hand-written teaching examples (8 spam and 8 not spam). They are included in `app.py` and are for demonstration only. They are not a sourced public dataset, are too small and narrow to represent real messages, and have not been evaluated on a separate test set. No accuracy, precision, recall, or F1 score is claimed.

## Methodology

`TfidfVectorizer` converts message text into word-weight numbers. `MultinomialNB` learns patterns associated with labels. A scikit-learn `Pipeline` keeps vectorization and classification together so new text receives the same transformation before prediction.

## Run locally

1. Install Python 3 from the official Python website if it is not installed.
2. Open Command Prompt in this folder.
3. Run `py -m pip install -r requirements.txt`.
4. Run `py -m streamlit run app.py`.
5. Open the local address Streamlit prints (usually `http://localhost:8501`).

## Test

Try one spam-like message such as `Congratulations, claim your free prize today` and one ordinary message such as `Are we still meeting at the library?`. Record the actual output. Try blank input too; the app should ask for a message. These are demonstrations, not an evaluation set.

## Results

No formal test-set results are included. The hand-picked examples are not a basis for reporting model quality.

## Limitations and future work

The dataset is tiny, manually written, English-only, and unlike a representative collection of real SMS messages. Naive Bayes can misclassify unfamiliar wording, context, sarcasm, and mixed-language text. Future work: use a properly cited public SMS dataset, split into training and test sets before fitting TF-IDF, report accuracy/precision/recall/F1 and a confusion matrix, and compare a second model.

## References and acknowledgement

- scikit-learn documentation: https://scikit-learn.org/stable/
- Streamlit documentation: https://docs.streamlit.io/
- AI assistance was used to help draft and explain parts of the code. The student should review, run, modify, and explain all submitted work, and follow university academic-integrity rules.

## Deployed website

Live app: https://spam-message-detector-h8ih6njyklhqezjpdac6zj.streamlit.app/

## Observed demonstration checks

The live app was checked with hand-picked examples: `Congratulations, claim your free prize today` returned “Likely spam”; `Are we still meeting at the library?` returned “Likely not spam”; and blank input displayed a warning. These are smoke checks, not a formal evaluation or accuracy estimate. No held-out test set or model-quality metrics are available.
