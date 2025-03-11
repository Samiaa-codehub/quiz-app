import streamlit as st
import random
import time

st.set_page_config(
    page_title="Quiz App",
    page_icon="🎗",
    layout="wide",
    
)

st.markdown("<h1 style='color:purple;'>📜Quiz Application Build By Samia Adnan </h1>",
          unsafe_allow_html=True)
st.write("<h5 style='color:purple;'>Learning is not about right or wrong. It's about understanding🎇..</h5>",
         unsafe_allow_html=True)
Questions = [
    {
        "question": "Who is the creater of Python?",
        "options":["Dennis Ritchie","Guido van Rossum","James Gosling","Bjarne Stroustrup"],
        "answer":"Guido van Rossum"
    },
    {
        "question" : "What type of language is Python?",
        "options" :["Compiled","Interpreted","Both Compiled and Interpreted","None of the above"],
        "answer":"Interpreted"
    },
    {
    "question" : "Which of the following data types is immutable in Python?",
    "options":["List","Tuple","Set","Dictionary"],
    "answer":"Tuple"
    },
    {
        "question" : "Which keyword is used to define a function in Python?",
        "options":["func","define","def","function"],
        "answer":"def"
    },
    {
        "question":"What is the starting index of list in Python?",
        "options":["1","0","-1","None"],
        "answer":"0",
    },
    {
        "question":"In Python, how are key-value pairs separated in a dictionary?",
        "options":[",(comma)",":(colon)","=(equal)","->(arrow)"],
        "answer":":(colon)",
    },
    {
        "question":"Which of the following is a valid variable name in Python?",
        "options":["1variable","_variable","variable-name","variable name"],
        "answer": "_variable"
    },
    {
        "question":"Which of the following is Not a Python data type?",
        "options":["list","array","tuple","set"],
        "answer": "array"
    },
    {
        "question":"What is the correct file extension for Python files?",
        "options":[".pyth",".pt",".py",".p"],
        "answer":".py"
    },
    {
        "question":"What will be the output of the following Python code?\n\n"
        "x = [1 , 2 , 3]\n"
        "print(x[1])",
        "options":["1","2","3","Error"],
         "answer": "1"
    },
    {
        "question":"What will this code print\n\n"
         "print(2 ** 3)",
         "options":["6","8","9","12"],
         "answer":"8"
    },    
]
if "current_question" not in st.session_state:
    st.session_state.current_question=random.choice(Questions)

question = st.session_state.current_question
st.subheader(question["question"])
selected_option = st.radio("Choose your answer",question["options"],key="answer")
if st.button("submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
    else:
        st.success("❎ Incorrect! the correct answer is "+ question["answer"])
        st.success("✨Every quiz is a quest. Sometimes you win,sometimes you learn!")
    time.sleep(5)

    st.session_state.current_question = random.choice(Questions)
    st.rerun()