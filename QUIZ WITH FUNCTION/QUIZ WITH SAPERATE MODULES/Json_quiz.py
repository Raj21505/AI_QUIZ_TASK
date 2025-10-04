import json
import os

Quetions = [
            {"que": "Who was the son of Arjuna and Subhadra?", "A": "Abhimanyu", "B": "Pradyumna", "C": "Lakshmana", "D": "Ghatotkacha", "ans": "A"},
            {"que": "What is the value of sin²θ + cos²θ?", "A": "0", "B": "1", "C": "2", "D": "Undefined", "ans": "B"},
            {"que": "How many meters in one angstrom?", "A": "10⁻¹⁰ m", "B": "10² m", "C": "10¹⁰ m", "D": "10⁷ m", "ans": "A"},
            {"que": "Stainless steel is an alloy, whereas air is a _____", "A": "Compound", "B": "Element", "C": "Mixture", "D": "Solution", "ans": "C"},
            {"que": "Who proposed the photoelectric effect?", "A": "Compton", "B": "Maxwell", "C": "Newton", "D": "Einstein", "ans": "D"}
        ]

def save_questions():
    with open("questions.json", "w") as file:
        json.dump(Quetions , file, indent=4)

def load_questions():
    if os.path.exists("questions.json"):
        with open("questions.json", "r") as file:
            return json.load(file)
    else:
        Quetions
        save_questions()