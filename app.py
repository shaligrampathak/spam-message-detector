import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

st.set_page_config(page_title="Spam Message Detector", page_icon="🛡️", layout="centered")

# A small hand-written teaching dataset: real ML, but not a real-world benchmark.
messages = [
    "Congratulations! You won a free prize. Call now to claim.",
    "URGENT: claim your cash reward by clicking the link",
    "Free entry in our weekly contest. Reply WIN now",
    "You have been selected for a special offer",
    "Earn money fast from home. Sign up today",
    "Your account has a problem. Verify details immediately",
    "Limited time offer: get a free gift card",
    "Winner! Text CLAIM to collect your bonus",
    "Can we meet for lunch after class?",
    "I will be late, please save me a seat",
    "Are you coming to the library today?",
    "Thanks for sending me the notes",
    "Please call me when you reach home",
    "The assignment is due on Friday",
    "Happy birthday! Hope you have a great day",
    "I am on the bus and will arrive soon",
]
labels = ["spam"] * 8 + ["not spam"] * 8

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB()),
])
model.fit(messages, labels)

st.title("🛡️ Spam Message Detector")
st.caption("A beginner machine-learning project using TF-IDF and Naive Bayes")
st.write("Enter a message to see how a text-classification model labels it. This is an educational demonstration, not a security or filtering service.")

with st.form("message_form"):
    message = st.text_area("Message to check", placeholder="Example: Congratulations, claim your free prize today!", height=140, max_chars=2000)
    submitted = st.form_submit_button("Check message", type="primary")

if submitted:
    if not message.strip():
        st.warning("Please enter a message before checking it.")
    else:
        prediction = model.predict([message.strip()])[0]
        if prediction == "spam":
            st.error("Prediction: Likely spam")
        else:
            st.success("Prediction: Likely not spam")
        st.caption("This is the model's prediction, and it can be wrong.")

with st.expander("How does the model work?"):
    st.markdown("""
    1. **TF-IDF** turns words into numbers. Words that help distinguish messages receive more influence.
    2. **Multinomial Naive Bayes** learns word patterns from labelled examples and estimates which label fits a new message.
    3. The model returns **spam** or **not spam**. It does not understand intent like a person does.
    """)

st.subheader("Dataset and limitations")
st.write("The model trains when this app starts on 16 hand-written teaching examples (8 labelled spam and 8 labelled not spam). This small dataset was created for demonstration; it is not a public benchmark and does not represent real-world messages. No accuracy score is claimed because no separate test set has been evaluated.")
st.info("Do not use this demo to make security decisions or paste private messages. A next improvement would be training and evaluating on a properly sourced public SMS dataset.")
st.divider()
st.caption("Student demonstration project • Python · scikit-learn · Streamlit")
