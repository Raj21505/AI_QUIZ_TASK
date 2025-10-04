import psycopg2
# from ADMIN.admin_main import Admin_Quiz

class SQL_Quiz:
    def get_connection(self):
        return psycopg2.connect(
            host="localhost",
            database="mydb",
            user="myuser",
            password="mypass",
            port=5432
        )

    def create_table(self):
        obj = SQL_Quiz()
        conn = obj.get_connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS quiz(" \
        "id SERIAL PRIMARY KEY," \
        "Que Text," \
        "A Text," \
        "B Text," \
        "C Text," \
        "D Text," \
        "Ans VARCHAR(1)" \
        ")")
        conn.commit()
        conn.close()

    def add_question(self):
        obj = SQL_Quiz()
        conn = obj.get_connection()
        cur = conn.cursor()
        user_que = input("Que: ")
        user_opt_1 = input("A: ")
        user_opt_2 = input("B: ")
        user_opt_3 = input("C: ")
        user_opt_4 = input("D: ")
        while True:
            user_ans = input("Ans: ").upper()
            if user_ans not in ["A", "B", "C", "D"]:
                print("Enter Answer in ( A , B , C or D ) format")
            else:
                break
        cur.execute("INSERT INTO quiz (Que , A , B , C , D , Ans) VALUES (%s, %s, %s, %s, %s, %s)", (user_que,user_opt_1,user_opt_2,user_opt_3,user_opt_4,user_ans))
        conn.commit()
        conn.close()
        while True:
            obj.further("add")
            break

    def read_quiz(self):
        obj = SQL_Quiz()
        conn = obj.get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM quiz ORDER BY id ASC")
        rows = cur.fetchall()
        conn.close()
        return rows
    
    def delete_quiz(self):
        obj = SQL_Quiz()
        conn = obj.get_connection()
        Que= obj.read_quiz()
        cur = conn.cursor()
        if not Que:
            print("No questions available.")
            return
        for i in range(len(Que)):
            print(f"{i+1}. {Que[i]}")
        print("\nConsider the above list and Enter the number that you want to delete") 
        while True:
            try:
                del_que = int(input("\nEnter the number: "))
                if 1 <= del_que <= len(Que):
                    Question_list = Que[del_que - 1][0]
                    cur.execute("DELETE FROM quiz WHERE id = %s", (Question_list,))
                    print("Question removed")
                    conn.commit()
                    conn.close()
                    break
                else:
                    print("Enter valid number")
            except ValueError:
                print("Please Enter Only Numeric Value...")
                print(ValueError)
        while True:
            obj.further("delete")
            break

    def update_Quiz(self):
        obj = SQL_Quiz()
        conn = obj.get_connection()
        Que= obj.read_quiz()
        cur = conn.cursor()
        for i in range(len(Que)):
            print(f"{i+1}. {Que[i]}")

        update_list = int(input("\nEnter the number of dictionary that you want to update: ")) - 1
        if update_list < 0 or update_list >= len(Que):
            print("Enter Valid Number")
        else:
            print()
            print(Que[update_list])
            while True:
                print("""
                    1. For update a Question, Enter 'que' 
                    2. For update options, Enter 'A', 'B', 'C' or 'D'
                    3. For update an Answer, Enter 'ans'
                    4. To exit, Enter 'exit'
                    """)
                user_upd = input("Enter what you want to update (consider above instruction): ").upper()
                print()
                if user_upd == "QUE":
                    obj.update_que(update_list)
                elif user_upd in ["A", "B", "C", "D"]:
                    obj.update_opt(update_list, user_upd)
                elif user_upd == "ANS":
                    obj.update_ans(update_list)
                elif user_upd == "EXIT":
                    break
                else:
                    print("Enter valid key")
                obj.further("update")
                break

    def update_que(self, update_list) :
        obj = SQL_Quiz()
        conn = obj.get_connection()
        Que= obj.read_quiz()
        cur = conn.cursor()
        update_que = input("Enter your new Question : ")
        update_list_str = Que[update_list][0]
        cur.execute("UPDATE quiz SET Que = %s WHERE id = %s",(update_que,update_list_str,))
        conn.commit()
        conn.close()
        print("\nUpdated the Question\n")

    def update_opt(self, update_list, user_upd) :
        obj = SQL_Quiz()
        conn = obj.get_connection()
        Que= obj.read_quiz()
        cur = conn.cursor()
        update_option = input("Enter your new Option: ")
        update_list_str = Que[update_list][0]
        cur.execute("UPDATE quiz SET {} = %s WHERE id = %s" .format(user_upd) , (update_option , update_list_str))
        conn.commit()
        conn.close()
        print("\nUpdated the Option\n")

    def update_ans(self, update_list) :
        obj = SQL_Quiz()
        conn = obj.get_connection()
        Que= obj.read_quiz()
        cur = conn.cursor()
        update_list_str = Que[update_list][0]
        while True:
            update_ans = input("Enter your new Ans (A, B, C or D): ").upper()
            if update_ans in ["A", "B", "C", "D"]:
                a = update_ans
                break
            else:
                print("Enter Valid Answer (A, B, C or D)")
        cur.execute("UPDATE quiz SET ans = %s WHERE id = %s",(a,update_list_str))
        conn.commit()
        print("\nUpdated the Answer\n")
        conn.close()

    def further(self , action) :
        # obj = JsonOp()
        obj = SQL_Quiz()
        while True:
            print(f"Do you want to {action} further..? (Enter 'No' to Quit)")
            leave = input("Enter: ")
            print()
            if leave.upper() == "NO":
                print("Okay... Question list updated")
                break
            elif action == "add":
                return obj.add_question()
            elif action == "delete":
                return obj.delete_quiz()
            elif action == "update":
                return obj.update_Quiz()