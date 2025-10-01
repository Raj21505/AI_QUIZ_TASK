# QUIZ

# -----------> PASSWORD = 2005 <-----------

Quetions = [{"que" : "Who was the son of Arjuna and Subhadra?" , "A" : "Abhimanyu" , "B" : "Pradyumna" , "C" : "Lakshmana" , "D" : "Ghatotkacha" , "ans" : "A"} , 
            {"que" : "What is the value of sin²θ + cos²θ?" , "A" : "0" , "B" : "1" , "C" : "2" , "D" : "Undefined" , "ans" : "B"} , 
            {"que" : "How many meters in one angstrom?" , "A" : "10⁻¹⁰ m" , "B" : "10² m" , "C" : "10¹⁰ m" , "D" : "10⁷ m" , "ans" : "A"} ,
            {"que" : "Stainless steel is an alloy, whereas air is a _____" , "A" : "Compound" , "B" : "Element" , "C" : "Mixture" , "D" : "Solution" , "ans" : "C"} ,
            {"que" : "Who proposed the photoelectric effect?" , "A" : "Compton" , "B" : "Maxwell" , "C" : "Newton" , "D" : "Einstein" , "ans" : "D"}]

while True:
    role = input("""
                Who are you? 
                1. Admin
                2. Player
                Ans(1 or 2) :- """)
    
    score = 0

    if role == "1":
        password = int(input("\n Enter the password :- "))
        while True:
            if password == 2005:
                while True:
                    activity = input("""
                                    What do you want to do now..?
                                    1. Add Quetion
                                    2. Delete Quetion
                                    3. Update Quetion
                                    4. Show dictionary of questions
                                    5. Exit
                                    (Give answer in format of 1 , 2 , 3 , 4 or 5 )
                                    Your choice :- """)
                    print()
                    if activity == "1":
                        print("-----You Want to Add a quetion-----")
                        while True:
                            user_que = input("Que :- ")
                            user_opt_1 = input("A :")
                            user_opt_2 = input("B :")
                            user_opt_3 = input("C :")
                            user_opt_4 = input("D :")
                            while True:
                                user_ans = input("Ans :").upper()
                                if user_ans in ["A","B","C","D"]:
                                    break
                                else:
                                    print("Enter Answer in ( A , B , C or D ) format")
                            dict = {
                                "que" : user_que ,
                                "A" : user_opt_1 ,
                                "B" : user_opt_2 ,
                                "C" : user_opt_3 ,
                                "D" : user_opt_4 ,
                                "ans" : user_ans ,
                            }
                            Quetions.append(dict)
                            leave = input("""
                                    "Do you want to add further..?" (Enter "NO" to Quit)
                                    Enter :- """)
                            print()
                            if leave.upper() == "NO":
                                print("Okay... Quetions added")
                                break

                    elif activity == "2":
                        print("-----You Want to Delete a quetion-----")
                        for q in range(len(Quetions)):
                            print(f"{q+1} . {Quetions[q]}")
                        print()
                        print("Consider the above list and Enter the number that you want to delete")
                        while True:
                            del_que = int(input("Enter the number :- ")) - 1
                            if del_que <= 0 or del_que > len(Quetions):
                                print("Enter valid number")
                            else:
                                Quetions.pop(del_que)
                                print("Question removed")
                                break

                    elif activity == "3":
                        print("-----You Want to Update in a Quiz-----")
                        print()
                        for p in range(len(Quetions)):
                            print(f"{p+1} . {Quetions[p]}")
                        
                        while True:
                            update_list = int(input("\nEnter the number of dictionary that you want to update :- ")) - 1
                            if update_list <= 0 or update_list > len(Quetions):
                                print("Enter Valid Number")
                            else:
                                while True:
                                    print()
                                    print(Quetions[update_list])
                                    print("""
                                        1. For update a Quetion , Enter 'que' 
                                        2. For update options , Enter 'A' , 'B' , 'C' or 'D'
                                        3. For update a Answer , Enter 'ans'
                                        4. For exit , Enter 'exit'
                                    """)
                                    user_update = input("Enter what you want to update (consider above instruction):- ")
                                    print()

                                    if user_update.lower() == "que":
                                        update_que = input("Enter your Que :- ")
                                        Quetions[update_list]["que"] = update_que
                                        print("\n Updated the Question \n" , Quetions[update_list])

                                    elif user_update.upper() in ["A","B","C","D"]:
                                        update_option = input("Enter your option :- ")
                                        Quetions[update_list][user_update.upper()] =  update_option
                                        print("\n Updated the Option \n" , Quetions[update_list])

                                    elif user_update.lower() == "ans":
                                        while True:
                                            update_ans = input("Enter your Ans ( A , B , C or D ) :- ")
                                            if update_ans.upper() in ["A","B","C","D"]:
                                                break
                                            else:
                                                print("Enter Valid Answer ( A , B , C or D ) ")
                                        Quetions[update_list]["ans"] = update_ans.upper()
                                        print("\n Updated the Answer \n" , Quetions[update_list])

                                    elif user_update.lower() == "exit":
                                        break
                                    
                                    else:
                                        print("Enter valid key")
                                    
                                leave = input("""
                                        "Do you want to update further..?" (Enter "NO" to Quit)
                                                Enter :- """)
                                print()
                                if leave.upper() == "NO":
                                    print("Okay... Quetions Updated")
                                    break

                    elif activity == "4":
                        print("-----This Game consist of questions listed below-----")
                        print()
                        for p in range(len(Quetions)):
                            print(f"{p+1} . {Quetions[p]}")
                    
                    elif activity == "5":
                        print("Okayy... Leaving")
                        break

                    else:
                        print("Enter valid number")
                break
            else:
                print("Incorrect Password")
                break
    
    elif role == "2":
        print("""
            WELCOME TO THE GAME
                
            Rules :- 
                    1. You will earn 1 marks for each correct answer
                    2. You must answer the quetion in "A , B , C & D only"
            """)
        for dict in Quetions:
            print("Que : " , dict["que"])
            print("A : " , dict["A"])
            print("B : " , dict["B"])
            print("C : " , dict["C"])
            print("D : " , dict["D"])
            while True:
                ans = input("Enter Your Choice (A , B , C or D):- ").upper()
                if ans == "A" or ans == "B" or ans == "C" or ans == "D" :
                    break
                else:
                    print("Only Enter A , B , C or D in your choice..")
            print()
            if ans.upper() == dict["ans"]:
                score += 1
            leave = input("""
                            "Do you want to play further..?" (Enter "NO" to Quit)
                            Enter :- """)
            print()
            if leave.upper() == "NO":
                print("Okay... Thanks For Playing")
                break
        print(f"\n You scored {score} out of", len(Quetions))
        break
    
    else:
        print("\n --> Enter valid Number ( 1 or 2 ) <-- \n")