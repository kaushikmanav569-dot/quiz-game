import streamlit as st
 st.title("Quiz Game:-")
 st.write("Q1: First Alphabet of English language..?\nA) d\tB) e\nC) a\tD) f")
 ans1 = st.text_input("Enter your answer here...",key.i)
 st.write("your answer is ...",ans1)
 st.write("<....................................>")
 st.write("Q2: Which of these is a mammel..?\nA) Duck\tB) Hen\nC) Owl\tD) Whale")
 ans2 =st.text_input("Enter your answer here...")# print("your answer is ...",ans2)
 st.write("<...................................>")
 print("Q3: Which is the largest ocean n the world?\nA) Indian ocean\tB) Pacific ocean\nC) Arctic ocean\tD) Atlantic ocean")
 ans3 = input("Enter your answer here...")
 print("your answer is ...",ans3)
 print("<....................................>")
 print("Q4: WHich is the National Animal ..?\nA) Fox\tB) Cow\nC) Tiger\tD) Elephant")
 ans4 = input("Enter your answer here...")
 print("your answer is ...",ans4)
 print("<....................................>")
 print("Q5: How many continents in the world..?\nA) 4\tB) 7\nC) 8\tD) 9")
 ans5 = input("Enter your answer here...")
 print("your answer is ...",ans5)
 Total = 0
 if ans1=="c" or ans1 == "C":
     Total +=1
if ans2=="d" or ans2 == "D":
     Total +=1
 if ans3=="b" or ans3 == "B":
     Total +=1
 if ans4=="c" or ans4 == "C":
     Total +=1
 if ans5=="b" or ans5 == "B":
     Total +=1
 print(Total)
 if Total ==5:
     print("Congratulations.... You are the topper with 5 points....")
 elif Total == 4:
     print("Congratulations... You have scored Second position")
 elif Total == 3:
     print("You have passed the Quiz wih 3 points.. Wish you very best for next time....  ")
 else:
     print("Better Luck next time....")
