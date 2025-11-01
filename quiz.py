import streamlit as st
st.title("QUIZ GAME:-")
ques=["Q1: First Alphabet of English language..?\nA) d\tB) e\nC) a\tD) f","Q2: Which of these is a mammel..?\nA) Duck\tB) Hen\nC) Owl\tD) Whale","Q3: Which is the largest ocean in the world?\nA) Indian ocean\tB) Pacific ocean\nC) Arctic ocean\tD) Atlantic ocean","Q4: WHich is the National Animal ..?\nA) Fox\tB) Cow\nC) Tiger\tD) Elephant","Q5: How many continents in the world..?\nA) 4\tB) 7\nC) 8\tD) 9"]
AL=[]
for i in ques:
    st.write(i)
    ans =st.text_input(f"Enter your choice....",key=i)
    AL.append(ans)
    st.write("<....................................>")
# for j in range(len(ques)):
#     ans =st.text_input(f"Enter your {j+1} choice....",key=i)
#     AL.append(ans)
# st.write(AL)
# RA=['c','d','b','c','b']
Total = 0
if AL[0] == 'c' or AL[0]=="C":
    Total +=1
    
if AL[1] == 'd' or AL[1]=="D":
    Total +=1

if AL[2] == 'b' or AL[2]=="B":
    Total +=1

if AL[3] == 'c' or AL[3]=="C":
    Total +=1

if AL[4] == 'b' or AL[4]=="B":
    Total +=1
if Total ==5:
    st.write("Congratulations.... You are the topper with 5 points....")
elif Total == 4:
    st.write("Congratulations... You have scored Second position")
elif Total == 3:
    st.write("You have passed the Quiz wih 3 points.. Wish you very best for next time....  ")
else:
    st.write("Better Luck next time....")
st.balloons()
