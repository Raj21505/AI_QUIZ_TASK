from MYSQL.database_quiz import SQL_Quiz

class Admin_Quiz:
    
    def __init__(self):
        self.__username = "admin"
        self.__password = int("2005")
        self.questions_storage = SQL_Quiz()
    
    def authenticate(self , username , password : int):
        if username == self.__username and password == self.__password:
            return True
        else:
            print("\n Username or Password is wrong")
            obj = Admin_Quiz()
            obj.admin()
    
    def admin(self):
        obj3 = Admin_Quiz()
        obj = SQL_Quiz()
        obj.get_connection()
        while True:
            try:
                username = input("\nEnter the Username: ")
                password = int(input("\nEnter the password: "))
                break
            except:
                print("\n --> Password Must be in Integer <--")
        while True:
            if obj3.authenticate(username , password) == True:
                obj.create_table()
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
                            obj1 = SQL_Quiz()
                            obj1.add_question()
                        elif activity == 2:
                            print("-----You Want to Delete a question-----")
                            obj2 = SQL_Quiz()
                            obj2.delete_quiz()
                        elif activity == 3:
                            print("-----You Want to Update a question-----")
                            obj3 = SQL_Quiz()
                            obj3.update_Quiz()
                        elif activity == 4:
                            print("-----This Game consists of questions listed below-----\n")
                            obj = SQL_Quiz()
                            Que = obj.read_quiz()
                            for i in range(len(Que)):
                                print(f"{i+1}. {Que[i]}")
                        elif activity == 5:
                            print("Okay... Leaving")
                            break
                        else :
                            print("Enter valid number")
                    except Exception as e:
                        print("Password must be integer")
                        print(e)
            break