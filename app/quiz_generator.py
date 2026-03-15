import random

def generate_questions(text):

    questions = [
        {
            "question": "How many sides does a triangle have?",
            "type": "MCQ",
            "options": ["2", "3", "4", "5"],
            "answer": "3",
            "difficulty": "easy"
        },
        {
            "question": "A square has four equal sides.",
            "type": "True/False",
            "options": ["True", "False"],
            "answer": "True",
            "difficulty": "easy"
        },
        {
            "question": "Fill in the blank: A circle has ___ corners.",
            "type": "Fill in the blank",
            "options": [],
            "answer": "0",
            "difficulty": "easy"
        },
        {
            "question": "What is the capital of France?",
            "type": "MCQ",
            "options": ["London", "Paris", "Berlin", "Madrid"],
            "answer": "Paris",
            "difficulty": "medium"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "type": "MCQ",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "answer": "Mars",
            "difficulty": "medium"
        },
        {
            "question": "What is the largest mammal?",
            "type": "MCQ",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "answer": "Blue Whale",
            "difficulty": "medium"
        },
        {
            "question": "What is the chemical symbol for water?",
            "type": "Fill in the blank",
            "options": [],
            "answer": "H2O",
            "difficulty": "easy"
        },
        {
            "question": "True or False: The Earth is flat.",
            "type": "True/False",
            "options": ["True", "False"],
            "answer": "False",
            "difficulty": "easy"
        },
        {
            "question": "What is the square root of 16?",
            "type": "Fill in the blank",
            "options": [],
            "answer": "4",
            "difficulty": "easy"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "type": "MCQ",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide",
            "difficulty": "medium"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "type": "MCQ",
            "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
            "answer": "Jupiter",
            "difficulty": "medium"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "type": "Fill in the blank",
            "options": [],
            "answer": "Au",
            "difficulty": "easy"
        },
        {
            "question": "True or False: The Sun is a star.",
            "type": "True/False",
            "options": ["True", "False"],
            "answer": "True",
            "difficulty": "easy"
        },
        {
            "question": "What is the capital of Japan?",
            "type": "MCQ",
            "options": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
            "answer": "Tokyo",
            "difficulty": "medium"
        },
        {
            "question": "Which element has the atomic number 1?",
            "type": "Fill in the blank",
            "options": [],
            "answer": "Hydrogen",
            "difficulty": "easy"
        }
    ]

    return random.choice(questions)