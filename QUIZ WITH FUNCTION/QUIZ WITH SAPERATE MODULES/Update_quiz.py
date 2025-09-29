from Json_quiz import *
from Continue_quiz import *
from Read_quiz import show

def update():
    print()
    show()
    update_list = int(input("\nEnter the number of dictionary that you want to update: ")) - 1
    if update_list < 0 or update_list >= len(Quetions):
        print("Enter Valid Number")
    else:
        while True:
            print()
            print(Quetions[update_list])
            print("""
                1. For update a Question, Enter 'que' 
                2. For update options, Enter 'A', 'B', 'C' or 'D'
                3. For update an Answer, Enter 'ans'
                4. To exit, Enter 'exit'
                """)
            user = input("Enter what you want to update (consider above instruction): ").upper()
            print()
            if user == "QUE":
                update_que(update_list)
            elif user in ["A", "B", "C", "D"]:
                update_opt(update_list, user)
            elif user == "ANS":
                update_ans(update_list)
            elif user == "EXIT":
                break
            else:
                print("Enter valid key")
    save_questions()
    cont("update")

def update_que(update_list):
    update_que = input("Enter your new Question: ")
    Quetions[update_list]["que"] = update_que
    print("\nUpdated the Question\n")

def update_opt(update_list, user):
    update_option = input("Enter your new option: ")
    Quetions[update_list][user] = update_option
    print("\nUpdated the Option\n")

def update_ans(update_list):
    while True:
        update_ans = input("Enter your new Ans (A, B, C or D): ").upper()
        if update_ans in ["A", "B", "C", "D"]:
            break
        else:
            print("Enter Valid Answer (A, B, C or D)")
    Quetions[update_list]["ans"] = update_ans
    print("\nUpdated the Answer\n")