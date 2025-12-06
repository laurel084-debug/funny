import streamlit as st
import joblib

# Load model
model = joblib.load("friend_model.pkl")

st.title("AI Friend Type Classifier 🤣")

st.write("Predict what type of friend someone is!")

joke = st.slider("Joke Level", 1, 10)
late = st.slider("Lateness Level", 1, 10)
eat = st.slider("Eating Level", 1, 10)

if st.button("Predict"):
    pred = model.predict([[joke, late, eat]])[0]
    labels = ["Clown 🤡","Mom 😭","Gremlin 🐸💥","Foodie 🍕"]
    st.success(f"Your friend is: {labels[pred]}")
