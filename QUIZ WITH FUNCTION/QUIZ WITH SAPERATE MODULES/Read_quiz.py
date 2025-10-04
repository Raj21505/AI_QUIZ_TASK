from Json_quiz import *

def show():
    Quetions = load_questions()

    for a in range(len(Quetions)):
        print(f"{a+1}. {Quetions[a]}")