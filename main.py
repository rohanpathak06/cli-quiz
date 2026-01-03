quiz_questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing Unit"
        ],
        "answer": "A"
    }
]


def run_quiz(questions):
    score = 0

    print("Welcome to the Quiz App.\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. Correct answer is {q['answer']}\n")

    print("Quiz Finished!!!")
    print(f"Your Score: {score}/{len(questions)}")


run_quiz(quiz_questions)
