from ADMIN.admin_main import Admin_Quiz
from PLAYER.player_main import Player_Quiz

class Quiz:
    while True:
        try:
            role = int(input("""
                        Who are you? 
                        1. Admin
                        2. Player
                        3. Leave
                        Ans (1 or 2 or 3): """))
    
            if role == 1:
                obj = Admin_Quiz()
                obj.admin()
                
            elif role == 2:
                obj2 = Player_Quiz()
                obj2.player()
            elif role == 3:
                print("Exiting... Goodbye..!!")
                break
            else:
                print("\n--> Enter valid Number (1, 2 or 3) <--\n")
        except Exception as e:
            print("Please Enter Only Numeric Values...")
            print(e)