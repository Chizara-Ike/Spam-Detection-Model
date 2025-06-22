import streamlit as st
import joblib
import re
import string

#Loading saved model
model = joblib.load("spam_detection_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

#Cleaning incoming texts
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

st.set_page_config(
    page_title="Spam Detector",
    page_icon="📩",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

#App UI
st.title("📭Spam Detection App")
st.write("Enter an SMS to check if it's **Spam** or **Ham (Not Spam)**.")


user_input = st.text_area("Enter text:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please Enter a Message.")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.error("❌**Spam**")
        else:
            st.success("✅**Ham** (Not Spam)")
