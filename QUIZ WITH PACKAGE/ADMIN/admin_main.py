from JSON.json_quiz import JsonOp

class Admin_Quiz:

    def __init__(self):
        self.__username = "admin"
        self.__password = int("2005")
        self.questions_storage = JsonOp()

    # def get_username(self):
    #     return self.__username
    
    def authenticate(self , username , password : int):
        if username == self.__username and password == self.__password:
            return True
        else:
            print("\n Username or Password is wrong")
            obj = Admin_Quiz()
            obj.admin()
            
    
    # def show_questions(self):
    #     ques = self.get_questions()
    #     for i, question in enumerate(ques):
    #         print(f"{i+1}. {question['que']}")
    #         print(f"A. {question['A']}")
    #         print(f"B. {question['B']}")
    #         print(f"C. {question['C']}")
    #         print(f"D. {question['D']}")
    #         print(f"Answer: {question['ans']}\n")

    # def get_questions(self):
    #     return self.questions_storage.read_questions()

    # def __get_question(self, question_id):
    #     return self.questions_storage.read_questions()[question_id]
    
    def admin(self):
        obj3 = Admin_Quiz()
        obj = JsonOp()
        obj.read_questions()
        while True:
            try:
                username = input("\nEnter the Username: ")
                password = int(input("\nEnter the password: "))
                break
            except:
                print("\n --> Password Must be in Integer <--")
        while True:
            if obj3.authenticate(username , password) == True:
                while True:
                    try:
                        activity = int(input("""
                                        What do you want to do now..?
                                        1. Add Question
                                        2. Delete Question
                                        3. Update Question
                                        4. Show dictionary of questions
                                        5. Exit
                                        (Give answer in format of 1 , 2 , 3 , 4 or 5 )
                                        Your choice: """))
                        print()
                        if activity == 1:
                            print("-----You Want to Add a question-----")
                            obj1 = JsonOp()
                            obj1.add_questions()
                        elif activity == 2:
                            print("-----You Want to Delete a question-----")
                            obj2 = JsonOp()
                            obj2.delete_quetions()
                        elif activity == 3:
                            print("-----You Want to Update a question-----")
                            obj2 = JsonOp()
                            obj2.update_quetions()
                        elif activity == 4:
                            print("-----This Game consists of questions listed below-----\n")
                            obj = JsonOp()
                            Que = obj.read_questions()
                            for i in range(len(Que)):
                                print(f"{i+1}. {Que[i]}")
                        elif activity == 5:
                            print("Okay... Leaving")
                            break
                        else:
                            print("Enter valid number")
                    except:
                        print("Password must be integer")
            else:
                print("Incorrect Password")
            break