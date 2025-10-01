from Json_quiz import *
from Continue_quiz import *
from Read_quiz import show

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
                    from Quiz_add_que import add
                    add()
                elif activity == "2":
                    print("-----You Want to Delete a question-----")
                    from Remove_quiz import remove
                    remove()
                elif activity == "3":
                    print("-----You Want to Update a question-----")
                    from Update_quiz import update
                    update()
                elif activity == "4":
                    print("-----This Game consists of questions listed below-----\n")
                    show()
                elif activity == "5":
                    print("Okay... Leaving")
                    break
                else:
                    print("Enter valid number")
            break
        else:
            print("Incorrect Password")
            break

