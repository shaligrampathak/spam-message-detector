# Spam Message Detector

A simple machine learning web app that labels a message as **likely spam** or **likely not spam**.

Created by Shaligram Pathak | Chandigarh University

## Live App

[Open the live Streamlit app](https://spam-message-detector-h8ih6njyklhqezjpdac6zj.streamlit.app/)

## How It Works

The app uses a scikit-learn Pipeline with two steps:

1. **TfidfVectorizer** converts the words of a message into weighted numerical features.
2. **MultinomialNB** (Multinomial Naive Bayes) uses those features to predict the label.

The model is fitted once when the app starts. It does not learn from visitor messages. The input is limited to 2,000 characters. If the input is empty, the app shows a warning instead of a prediction.

The app returns either **spam** or **not spam**, displayed as “Likely spam” or “Likely not spam.” The prediction can be wrong because the model does not understand intent like a person and cannot verify whether a link is dangerous.

## Tech Stack

- Python
- scikit-learn
- Streamlit
- Google Colab for development
- GitHub for hosting the code
- Streamlit Community Cloud for deployment

## Training Data

The model uses 16 hand-written teaching examples: 8 spam and 8 not spam. No public dataset is used.

## Limitations

- Very small and narrow training data, English only
- No separate test set, so accuracy, precision, recall, and F1 score have not been calculated
- It only looks at words and cannot verify whether a link is actually dangerous
- Predictions can be wrong, so this is a learning prototype and not a real spam filter
- Do not use this demo to make security decisions or paste private messages into it

## Future Work

Train on a public SMS dataset such as the [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection), split the data into training and test sets before fitting, evaluate on unseen messages, and inspect errors.

## Run Locally

1. Install Python 3.
2. Clone this repository and open a terminal in the project folder.
3. Install the dependencies with: `py -m pip install -r requirements.txt`.
4. Start the app with: `py -m streamlit run app.py`.
5. Open the local address shown by Streamlit, usually `http://localhost:8501`.

## Project Links

- [Live app](https://spam-message-detector-h8ih6njyklhqezjpdac6zj.streamlit.app/)
- [Source code](https://github.com/shaligrampathak/spam-message-detector)

## References and Acknowledgement

- [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) — a possible dataset for future work; it is not used by this current app
- [scikit-learn Naive Bayes guide](https://scikit-learn.org/stable/modules/naive_bayes.html)
- [TfidfVectorizer documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Streamlit documentation](https://docs.streamlit.io/)

AI assistance was used while drafting and explaining parts of the code. The student should review and understand the implementation and follow course academic-integrity rules.
