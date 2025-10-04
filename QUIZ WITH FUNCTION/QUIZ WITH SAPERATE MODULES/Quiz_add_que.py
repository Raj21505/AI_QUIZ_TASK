from Json_quiz import *

def add():
    while True:
        user_que = input("Que: ")
        user_opt_1 = input("A: ")
        user_opt_2 = input("B: ")
        user_opt_3 = input("C: ")
        user_opt_4 = input("D: ")
        while True:
            user_ans = input("Ans: ").upper()
            if user_ans in ["A", "B", "C", "D"]:
                break
            else:
                print("Enter Answer in ( A , B , C or D ) format")
        new_dict = {
            "que": user_que,
            "A": user_opt_1,
            "B": user_opt_2,
            "C": user_opt_3,
            "D": user_opt_4,
            "ans": user_ans,
        }
        Quetions.append(new_dict)
        save_questions()
        from Continue_quiz import cont
        cont("add")
        break  