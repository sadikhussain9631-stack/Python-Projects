# Quiz Application

A simple interactive quiz web application built with **Python** and
**Streamlit**. Users answer five multiple-choice questions, submit the
quiz, view their score and percentage, and review explanations for each
answer.

## Features

-   Displays five multiple-choice questions.
-   Requires all questions to be answered before submission.
-   Awards **1 mark** for each correct answer.
-   Calculates the total score and percentage.
-   Shows the number of correct and incorrect answers.
-   Displays feedback based on the final percentage.
-   Provides an answer review with explanations.
-   Includes a **Restart Quiz** button to attempt the quiz again.

## Technologies Used

-   **Python** -- application logic and quiz data.
-   **Streamlit** -- web interface.
-   **Lists and dictionaries** -- store questions, options, answers, and
    explanations.
-   **Functions** -- organize scoring, result display, and the main
    application.
-   **Loops and conditional statements** -- display questions and
    evaluate answers.
-   **Session state** -- preserve submitted answers and quiz status
    across Streamlit reruns.

## Project Structure

``` text
quiz-application/
├── app.py
└── README.md
```

## Requirements

-   Python 3.8 or later
-   pip (Python package installer)
-   Streamlit

## Installation and Setup

1.  Install Python if it is not already installed.

2.  Open a terminal or command prompt.

3.  Move into the folder containing `app.py`.

4.  Install Streamlit:

    ``` bash
    pip install streamlit
    ```

## Run the Application

Start the application with:

``` bash
streamlit run app.py
```

Streamlit will open the quiz in your default web browser. If it does not
open automatically, use the local URL shown in the terminal (usually
`http://localhost:8501`).

## How to Use

1.  Open the Quiz Application.
2.  Read each question carefully.
3.  Select one option for every question.
4.  Click **Submit Quiz**.
5.  View your total questions, correct answers, wrong answers, score,
    and percentage.
6.  Read the answer review and explanations.
7.  Click **Restart Quiz** to take the quiz again.

## Scoring System

Each correct answer carries 1 mark.

-   Total questions: 5
-   Maximum score: 5
-   Percentage: `(Correct Answers / Total Questions) × 100`

### Performance Feedback

  Percentage         Feedback
  ------------------ ------------------------------
  80% or above       Excellent performance!
  50% to below 80%   Good job! Keep practicing.
  Below 50%          Keep learning and try again!

## Main Functions

  ---------------------------------------------------------------------------
  Function                                Purpose
  --------------------------------------- -----------------------------------
  `calculate_score(questions, answers)`   Compares submitted answers with the
                                          correct answers and returns the
                                          score.

  `display_result(questions, answers)`    Displays the score, percentage,
                                          performance feedback, and answer
                                          explanations.

  `main()`                                Builds the quiz interface, collects
                                          answers, handles submission, and
                                          restarts the quiz.
  ---------------------------------------------------------------------------

## Learning Outcomes

This project demonstrates how to:

-   Create a simple web application using Streamlit.
-   Store structured information using Python lists and dictionaries.
-   Define and call functions.
-   Use `for` loops, `if` conditions, and `zip()`.
-   Calculate scores and percentages.
-   Manage application state using `st.session_state`.

## Future Improvements

-   Add more questions and categories.
-   Add a timer for the quiz.
-   Randomize the order of questions.
-   Save quiz results for later review.
-   Add a leaderboard.

## Author

**Student Project -- Quiz Application**

------------------------------------------------------------------------

This project is created for learning and demonstrating basic Python
programming concepts with Streamlit.
