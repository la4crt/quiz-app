from typing import List, Dict

Question = Dict[str, object]


def build_questions() -> List[Question]:
    return [
        {
            "text": "What is the capital of Saudi Arabia?",
            "options": ["Jeddah", "Riyadh", "Makkah", "Dammam"],
            "answer": 2,
        },
        {
            "text": "When did Queen Elizabeth II pass away?",
            "options": ["2020", "2021", "2022", "2023"],
            "answer": 3,
        },
        {
            "text": "Which continent is Saudi Arabia located in?",
            "options": ["Europe", "Asia", "Africa", "Australia"],
            "answer": 2,
        },
        {
            "text": "Which programming language is commonly considered easy for beginners?",
            "options": ["Assembly", "C++", "Python", "Machine Code"],
            "answer": 3,
        },
        {
            "text": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Control Processing User",
            ],
            "answer": 1,
        },
    ]


def get_user_choice() -> int:
    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice.isdigit():
            num = int(choice)
            if 1 <= num <= 4:
                return num
        print("Invalid input. Please enter a number between 1 and 4.")


def ask_question(question: Question, number: int) -> bool:
    print(f"\nQuestion {number}: {question['text']}")
    for idx, option in enumerate(question["options"], start=1):
        print(f"{idx}. {option}")

    user_answer = get_user_choice()
    if user_answer == question["answer"]:
        print("Correct!")
        return True

    correct_option = question["options"][question["answer"] - 1]
    print(f"Incorrect. The correct answer is: {question['answer']} ({correct_option})")
    return False


def run_quiz() -> None:
    print("Welcome to the Holton College Quiz!")
    print("Answer using numbers (1, 2, 3, or 4).")

    questions = build_questions()
    score = 0

    for i, q in enumerate(questions, start=1):
        if ask_question(q, i):
            score += 1

    print("\nQuiz Complete!")
    print(f"You scored {score} out of {len(questions)}.")
    print("Thank you for playing!")


if __name__ == "__main__":
    run_quiz()

