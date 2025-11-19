from JSON.json_quiz import JsonOp
import streamlit as st
class Player_Quiz:

    def player(self):
        score = 0
        total_que = 0
        st.subheader("""
                WELCOME TO THE GAME

                Rules:- 
                1. You will earn 1 mark for each correct answer
                2. You must answer the question in "A, B, C & D only"
                """)
        
        st.subheader("Let's Play...!!!")
        obj = JsonOp()
        Que = obj.read_questions()
        for i,dict in enumerate(Que):
            st.subheader(f"Question  No. {i+1}.")
            st.write("Que. is : ",dict["que"])
            st.write("A:", dict["A"])
            st.write("B:", dict["B"])
            st.write("C:", dict["C"])
            st.write("D:", dict["D"])
            total_que += 1
            ans = st.selectbox("Select Your Choice ",["Select","A","B","C","D"] , key=f"Answer{i}")
            if ans in ["A", "B", "C", "D"]:
                if ans == dict["ans"]:
                    score += 1
        submit = st.button("Submit")
        if submit:
            st.subheader(f"Your Score is : {score}")
        
        
                # break
            # else :
            #     st.warning("Select Answer")
            #     break
                
                
            # else:
            #     st.write("Choose Answer")
            # print()
            
            # leave = input('\nDo you want to play further? (Enter "NO" to Quit)\nEnter: ')
            # print()
            # if leave.upper() == "NO":
            #     print("Okay... Thanks For Playing")
            #     break
        # print(f"\nYou scored {score} out of {total_que}")
        # return 0