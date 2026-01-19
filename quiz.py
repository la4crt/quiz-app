import json
import random
from typing import List, Dict, Any


QUESTIONS_FILE = "questions.json"


def default_questions() -> List[Dict[str, Any]]:
    """Return a default set of 7 quiz questions (multiple choice)."""
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
            "text": "Which data structure uses key-value pairs in Python?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": 3,
        },
        {
            "text": "Which symbol is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": 3,
        },
        {
            "text": "Which loop is commonly used when the number of iterations is known?",
            "options": ["while", "for", "do-while", "foreach"],
            "answer": 2,
        },
    ]


def load_questions(filename: str) -> List[Dict[str, Any]]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list) or len(data) < 7:
            raise ValueError("Invalid questions format.")

        return data

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        questions = default_questions()
        save_questions(filename, questions)
        return questions


def save_questions(filename: str, questions: List[Dict[str, Any]]) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)


def get_choice(prompt: str, min_value: int, max_value: int) -> int:
    while True:
        choice = input(prompt).strip()
        if choice.isdigit():
            num = int(choice)
            if min_value <= num <= max_value:
                return num
        print(f"Invalid input. Please enter a number between {min_value} and {max_value}.")


def ask_question(question: Dict[str, Any], number: int) -> bool:
    print(f"\nQuestion {number}: {question['text']}")
    for i, option in enumerate(question["options"], start=1):
        print(f"{i}. {option}")

    user_answer = get_choice("Your answer (1-4): ", 1, 4)

    if user_answer == question["answer"]:
        print("Correct!")
        return True

    correct = question["answer"]
    print(f"Incorrect. The correct answer is {correct} ({question['options'][correct - 1]})")
    return False


def run_quiz(questions: List[Dict[str, Any]]) -> None:
    print("Welcome to the Holton College Quiz!")
    print("Answer by typing a number between 1 and 4.")

    score = 0
    random.shuffle(questions)

    for i, question in enumerate(questions, start=1):
        if ask_question(question, i):
            score += 1

    print("\nQuiz Complete!")
    print(f"You scored {score} out of {len(questions)}.")
    print("Thank you for playing!")


def menu() -> None:
    questions = load_questions(QUESTIONS_FILE)

    while True:
        print("\n1. Start Quiz")
        print("2. Reset Questions")
        print("3. Exit")

        choice = get_choice("Choose (1-3): ", 1, 3)

        if choice == 1:
            run_quiz(questions)
        elif choice == 2:
            questions = default_questions()
            save_questions(QUESTIONS_FILE, questions)
            print("Questions reset.")
        else:
            print("Goodbye!")

            break


if __name__ == "__main__":
    menu()

