from MYSQL.database_quiz import SQL_Quiz

class Player_Quiz:

    def player(self):
        score = 0
        attemp_que = 0
        print("""
                WELCOME TO THE GAME
        
                Rules:- 
                1. You will earn 1 mark for each correct answer
                2. You must answer the question in "A, B, C & D only"
                """)
        obj = SQL_Quiz()
        obj.get_connection()
        Que = obj.read_quiz()
        for dict in Que :
            print("Que:", dict[1])
            print("A:", dict[2])
            print("B:", dict[3])
            print("C:", dict[4])
            print("D:", dict[5])
            attemp_que += 1
            while True:
                ans = input("Enter Your Choice (A, B, C or D): ").upper()
                if ans in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Only Enter A, B, C or D")
            print()
            if ans == dict[6]:
                score += 1
            leave = input('\nDo you want to play further? (Enter "NO" to Quit)\nEnter: ')
            print()
            if leave.upper() == "NO":
                print("Okay... Thanks For Playing")
                break
        print(f"\nYou scored {score} out of {attemp_que}")
        return 0   