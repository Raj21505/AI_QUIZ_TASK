from JSON.json_quiz import JsonOp

class Player_Quiz:

    def player(self):
        score = 0
        total_que = 0
        print("""
                WELCOME TO THE GAME

                Rules:- 
                1. You will earn 1 mark for each correct answer
                2. You must answer the question in "A, B, C & D only"
                """)
        obj = JsonOp()
        Que = obj.read_questions()
        for dict in Que:
            print("Que:", dict["que"])
            print("A:", dict["A"])
            print("B:", dict["B"])
            print("C:", dict["C"])
            print("D:", dict["D"])
            total_que += 1
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
        print(f"\nYou scored {score} out of {total_que}")
        return 0