import json

class JsonOp:

    def __init__(self , path: str = None):
        self.path = path or "question.json"

    def read_questions(self): 
        global questions
        try:
            with open(self.path , "r") as f:
                questions = json.load(f)
        except FileNotFoundError:
            questions = []
            with open(self.path , "w") as f:
                json.dump(questions , f)
        return questions
    
    def add_questions(self):
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
            obj = JsonOp()
            obj.read_questions()
            questions.append(new_dict)
            with open(self.path, "w") as f: 
                json.dump(questions, f, indent=4)
            obj.further("add")
            break  

    def update_quetions(self):
        obj = JsonOp()
        obj.read_questions()
        for i in range(len(questions)):
            print(f"{i+1}. {questions[i]}")
        update_list = int(input("\nEnter the number of dictionary that you want to update: ")) - 1
        if update_list < 0 or update_list >= len(questions):
            print("Enter Valid Number")
        else:
            while True:
                print()
                print(questions[update_list])
                print("""
                    1. For update a Question, Enter 'que' 
                    2. For update options, Enter 'A', 'B', 'C' or 'D'
                    3. For update an Answer, Enter 'ans'
                    4. To exit, Enter 'exit'
                    """)
                user = input("Enter what you want to update (consider above instruction): ").upper()
                print()
                if user == "QUE":
                    obj.update_que(update_list)
                elif user in ["A", "B", "C", "D"] :
                    obj.update_opt(update_list, user)
                elif user == "ANS" :
                    obj.update_ans(update_list)
                elif user == "EXIT" :
                    break
                else:
                    print("Enter valid key")
                with open(self.path, "w") as f : 
                    json.dump(questions, f, indent=4)
        obj.further("update")

    def update_que(self, update_list) :
        obj = JsonOp()
        obj.read_questions()
        update_que = input("Enter your new Question : ")
        questions[update_list]["que"] = update_que
        print("\nUpdated the Question\n")

    def update_opt(self, update_list, user) :
        obj = JsonOp()
        obj.read_questions()
        update_option = input("Enter your new option: ")
        questions[update_list][user] = update_option
        print("\nUpdated the Option\n")

    def update_ans(self, update_list) :
        obj = JsonOp()
        obj.read_questions()
        while True:
            update_ans = input("Enter your new Ans (A, B, C or D): ").upper()
            if update_ans in ["A", "B", "C", "D"]:
                break
            else:
                print("Enter Valid Answer (A, B, C or D)")
        questions[update_list]["ans"] = update_ans
        print("\nUpdated the Answer\n")

    def delete_quetions(self) :
        obj = JsonOp()
        Que = obj.read_questions()
        # show()
        for i in range(len(Que)):
            print(f"{i+1}. {Que[i]}")
        print("\nConsider the above list and Enter the number that you want to delete")
        while True:
            try:
                del_que = int(input("\nEnter the number: "))
                if 1 <= del_que <= len(Que):
                    del Que[del_que - 1]
                    with open(self.path , "w") as f:
                        json.dump(Que , f , indent=4)
                    print("Question removed")
                    obj.further("delete")
                    break
                else:
                    print("Enter valid number")
            except ValueError:
                print("Please Enter Only Numeric Value...")
                print(ValueError)

    def further(self , action) :
        obj = JsonOp()
        while True:
            print(f"Do you want to {action} further..? (Enter 'No' to Quit)")
            leave = input("Enter: ")
            print()
            if leave.upper() == "NO":
                print("Okay... Question list updated")
                break
            elif action == "add":
                return obj.add_questions()
            elif action == "delete":
                return obj.delete_quetions()
            elif action == "update":
                return obj.update_quetions()