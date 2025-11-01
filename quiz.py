import streamlit as st

st.title("🎯 Quiz Game")
st.write("Answer the following 5 questions:")

questions = [
    "Q1: First Alphabet of English language?\nA) D\tB) E\tC) A\tD) F",
    "Q2: Which of these is a mammal?\nA) Duck\tB) Hen\tC) Owl\tD) Whale",
    "Q3: Which is the largest ocean in the world?\nA) Indian\tB) Pacific\tC) Arctic\tD) Atlantic",
    "Q4: Which is the National Animal of India?\nA) Fox\tB) Cow\tC) Tiger\tD) Elephant",
    "Q5: How many continents are there in the world?\nA) 4\tB) 7\tC) 8\tD) 9"
]

answers = ['C', 'D', 'B', 'C', 'B']
user_answers = []

# Ask questions using radio buttons
for i, q in enumerate(questions):
    st.subheader(q)
    ans = st.radio(f"Select your answer for Question {i+1}:", ['A', 'B', 'C', 'D'], key=i)
    user_answers.append(ans)

# Submit button to check score
if st.button("Submit Quiz"):
    score = 0
    for i in range(5):
        if user_answers[i] == answers[i]:
            score += 1

    st.write("### 🧮 Your Total Score:", score, "/ 5")

    if score == 5:
        st.success("🏆 Congratulations! You are the topper!")
    elif score == 4:
        st.info("🥈 Great Job! You got Second Position.")
    elif score == 3:
        st.warning("🙂 You passed the quiz!")
    else:
        st.error("😢 Better Luck Next Time.")
