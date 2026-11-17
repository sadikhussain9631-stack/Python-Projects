
import streamlit as st

st.set_page_config(
    page_title="📃 Quiz Application",
    layout="centered"
)


questions = [
    {
        "question": "What is the full form of CPU?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing Unit"
        ],
        "answer": "A. Central Processing Unit",
        "explanation": "CPU stands for Central Processing Unit. It is known as the brain of the computer because it processes instructions and performs calculations."
    },
    {
        "question": "Which language is used in this project?",
        "options": [
            "A. Java",
            "B. Python",
            "C. C++",
            "D. HTML"
        ],
        "answer": "B. Python",
        "explanation": "Python is the programming language used to develop this project. Streamlit is a Python framework used to create the web application."
    },
    {
        "question": "Which data structure stores key-value pairs?",
        "options": [
            "A. List",
            "B. Tuple",
            "C. Dictionary",
            "D. Set"
        ],
        "answer": "C. Dictionary",
        "explanation": "A dictionary stores data in key-value pairs. In this project, dictionaries store each question, its options, its correct answer, and its explanation."
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": [
            "A. function",
            "B. define",
            "C. fun",
            "D. def"
        ],
        "answer": "D. def",
        "explanation": "The def keyword is used to define a function in Python. In this project, it defines functions such as calculate_score(), display_result(), and main()."
    },
    {
        "question": "Which loop is commonly used to iterate over a list?",
        "options": [
            "A. if",
            "B. for",
            "C. def",
            "D. return"
        ],
        "answer": "B. for",
        "explanation": "A for loop is used to iterate through items in a list. In this project, it is used to display questions and check answers."
    }
]



def calculate_score(questions, answers):
    score = 0

    for question, user_answer in zip(questions, answers):
        if user_answer == question["answer"]:
            score += 1

    return score



def display_result(questions, answers):
    score = calculate_score(questions, answers)
    total = len(questions)
    percentage = (score / total) * 100

    st.subheader("Quiz Results")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Questions", total)
    col2.metric("Correct Answers", score)
    col3.metric("Wrong Answers", total - score)

    st.progress(score / total)

    st.write(f"### Final Score: {score}/{total}")
    st.write(f"### Percentage: {percentage:.2f}%")

    if percentage >= 80:
        st.success("Excellent performance!")
    elif percentage >= 50:
        st.info("Good job! Keep practicing.")
    else:
        st.warning("Keep learning and try again!")

    st.subheader("Answer Review")

    for i, question in enumerate(questions):

        st.write(f"### Question {i + 1}: {question['question']}")

        if answers[i] == question["answer"]:

            st.success(f"Your answer: {answers[i]} — Correct!")

            st.info(
                f"**Why is it correct?** {question['explanation']}"
            )

        else:

            st.error(f"Your answer: {answers[i]} — Incorrect!")

            st.warning(
                f"**Correct answer:** {question['answer']}"
            )

            st.info(
                f"**Why is the correct answer right?** {question['explanation']}"
            )



def main():

    st.title("📝 Quiz Application")
    st.write("Welcome! Test your knowledge with this Python quiz.")
    st.caption("Each correct answer carries 1 mark.")

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if not st.session_state.submitted:

        with st.form("quiz_form"):

            answers = []

            for i, question in enumerate(questions):

                st.markdown(f"### Question {i + 1}")
                st.write(question["question"])

                answer = st.radio(
                    "Choose your answer:",
                    question["options"],
                    index=None,
                    key=f"question_{i}"
                )

                answers.append(answer)

            submitted = st.form_submit_button(
                "Submit Quiz",
                type="primary",
                use_container_width=True
            )

        if submitted:

            if any(answer is None for answer in answers):

                st.warning("Please answer all questions before submitting.")

            else:

                st.session_state.submitted_answers = answers
                st.session_state.submitted = True

                st.rerun()

    else:

        display_result(
            questions,
            st.session_state.submitted_answers
        )

        if st.button("Restart Quiz", use_container_width=True):

            st.session_state.submitted = False
            st.session_state.pop("submitted_answers", None)

            for i in range(len(questions)):
                st.session_state.pop(f"question_{i}", None)

            st.rerun()



if __name__ == "__main__":
    main()
