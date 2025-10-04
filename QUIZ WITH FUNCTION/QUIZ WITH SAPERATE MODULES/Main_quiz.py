from Json_quiz import *
from Admin_quiz import admin
from Player_quiz import player

load_questions() 

while True:
    role = input("""
                Who are you? 
                1. Admin
                2. Player
                3. Leave
                Ans (1 or 2 or 3): """)
    
    if role == "1":
        admin()
    elif role == "2":
        player()
    elif role == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("\n--> Enter valid Number (1, 2 or 3) <--\n")
