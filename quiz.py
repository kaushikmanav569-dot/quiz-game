import streamlit as st

st.title("🎯 Simple Quiz ")
st.write("Q1. What is the first alphabet of English language?")
answer1 = st.selectbox("Choose your answer:", ["A", "B", "C", "D"])
if answer1 == "A":
    score += 1

# Question 2
st.write("Q2. Which of these is a mammal?")
answer2 = st.selectbox("Choose your answer:", ["Duck", "Hen", "Owl", "Whale"])
if answer2 == "Whale":
    score += 1

# Show result
st.write("---")
st.write(f"Your total score is: *{score}*")

if score == 2:
    st.success("🎉 Congratulations  You got all answers correct!")
    st.balloons()
else:
    st.info("Try again Ayaan! You can do better 🙂")
