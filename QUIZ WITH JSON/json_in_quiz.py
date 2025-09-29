import json
import os

# ----------------------- JSON Admin Functions -----------------------

def save_questions():
    with open("questions.json", "w") as file:
        json.dump(Quetions, file, indent=4)

def load_questions():
    global Quetions
    if os.path.exists("questions.json"):
        with open("questions.json", "r") as file:
            Quetions = json.load(file)
    else:
        Quetions = [
            {"que": "Who was the son of Arjuna and Subhadra?", "A": "Abhimanyu", "B": "Pradyumna", "C": "Lakshmana", "D": "Ghatotkacha", "ans": "A"},
            {"que": "What is the value of sin²θ + cos²θ?", "A": "0", "B": "1", "C": "2", "D": "Undefined", "ans": "B"},
            {"que": "How many meters in one angstrom?", "A": "10⁻¹⁰ m", "B": "10² m", "C": "10¹⁰ m", "D": "10⁷ m", "ans": "A"},
            {"que": "Stainless steel is an alloy, whereas air is a _____", "A": "Compound", "B": "Element", "C": "Mixture", "D": "Solution", "ans": "C"},
            {"que": "Who proposed the photoelectric effect?", "A": "Compton", "B": "Maxwell", "C": "Newton", "D": "Einstein", "ans": "D"}
        ]
        save_questions()
        
# ------------------------ Admin Functions ------------------------

def admin():
    password = int(input("\nEnter the password: "))
    while True:
        if password == 2005:
            while True:
                activity = input("""
                                What do you want to do now..?
                                1. Add Question
                                2. Delete Question
                                3. Update Question
                                4. Show dictionary of questions
                                5. Exit
                                (Give answer in format of 1 , 2 , 3 , 4 or 5 )
                                Your choice: """)
                print()
                if activity == "1":
                    print("-----You Want to Add a question-----")
                    add()
                elif activity == "2":
                    print("-----You Want to Delete a question-----")
                    remove()
                elif activity == "3":
                    print("-----You Want to Update a question-----")
                    update()
                elif activity == "4":
                    print("-----This Game consists of questions listed below-----\n")
                    for p in range(len(Quetions)):
                        print(f"{p+1}. {Quetions[p]}")
                elif activity == "5":
                    print("Okay... Leaving")
                    break
                else:
                    print("Enter valid number")
            break
        else:
            print("Incorrect Password")
            break

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
        break
    further("add")

def remove():
    for q in range(len(Quetions)):
        print(f"{q+1}. {Quetions[q]}")
    print("\nConsider the above list and Enter the number that you want to delete")
    while True:
        del_que = int(input("Enter the number: "))
        if 1 <= del_que <= len(Quetions):
            del Quetions[del_que - 1]
            save_questions()
            print("Question removed")
            further("remove")
            break
        else:
            print("Enter valid number")

def update():
    print()
    for p in range(len(Quetions)):
        print(f"{p+1}. {Quetions[p]}")
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
    further("update")

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

def further(action):
    while True:
        print(f"Do you want to {action} further..? (Enter 'No' to Quit)")
        leave = input("Enter: ")
        print()
        if leave.upper() == "NO":
            print("Okay... Question list updated")
            break
        elif action == "add":
            return add()
        elif action == "remove":
            return remove()
        elif action == "update":
            return update()

# ------------------------- Player Function -------------------------

def player():
    score = 0
    print("""
            WELCOME TO THE GAME

            Rules:- 
            1. You will earn 1 mark for each correct answer
            2. You must answer the question in "A, B, C & D only"
            """)
    for dict in Quetions:
        print("Que:", dict["que"])
        print("A:", dict["A"])
        print("B:", dict["B"])
        print("C:", dict["C"])
        print("D:", dict["D"])
        while True:
            ans = input("Enter Your Choice (A, B, C or D): ").upper()
            if ans in ["A", "B", "C", "D"]:
                break
            else:
                print("Only Enter A, B, C or D")
        print()
        if ans == dict["ans"]:
            score += 1
        leave = input('\nDo you want to play further? (Enter "NO" to Quit)\nEnter: ')
        print()
        if leave.upper() == "NO":
            print("Okay... Thanks For Playing")
            break
    print(f"\nYou scored {score} out of {len(Quetions)}")
    return 0

# ------------------------- Main Program -------------------------

load_questions() 

while True:
    role = int(input("""
                Who are you? 
                1. Admin
                2. Player
                3. Leave
                Ans (1 or 2 or 3): """))
    if role == 1:
        admin()
    elif role == 2:
        player()
    elif role == 3:
        print("Exiting... Goodbye!")
        break
    else:
        print("\n--> Enter valid Number (1, 2 or 3) <--\n")