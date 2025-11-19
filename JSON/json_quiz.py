import json
import streamlit as st

# num = 0
class JsonOp:

    def __init__(self , path: str = None):
        self.path = path or "question.json"

    def read_questions(self): 
        global questions
        try:
            with open(self.path , "r") as f:
                questions = json.load(f)
        except FileNotFoundError:
            questions = []
            with open(self.path , "w") as f:
                json.dump(questions , f)
        return questions
      
    def add_questions(self):
        user_que = st.text_input("Que: ")
        user_opt_1 = st.text_input("A: ")
        user_opt_2 = st.text_input("B: ")
        user_opt_3 = st.text_input("C: ")
        user_opt_4 = st.text_input("D: ")
        user_ans = st.selectbox("Select correct Ans:", ["A" , "B" , "C" , "D"])
        if user_que and user_opt_1 and user_opt_2 and user_opt_3 and user_opt_4 and user_ans:
            submit = st.button("SUBMIT")
            if submit:
                new_dict = {
                    "que": user_que,
                    "A": user_opt_1,
                    "B": user_opt_2,
                    "C": user_opt_3,
                    "D": user_opt_4,
                    "ans": user_ans,
                }
                obj = JsonOp()
                obj.read_questions()
                questions.append(new_dict)
                with open(self.path, "w") as f: 
                    json.dump(questions, f, indent=4)
                
                # obj.further("add")
                                  

    def update_questions(self):
        obj = JsonOp()
        Que = obj.read_questions()
        data = ["Select"]
        for i, q in enumerate(Que):
            st.markdown(f"{i+1}. {q}")
            data.append(i+1)
        update_que_1 = st.selectbox("Consider the above list and Enter the number that you want to Update" , options=data)
        update_que = update_que_1-1
        if update_que:
            st.subheader("Your Selected Question is as below:")
            st.subheader(Que[update_que])
            sel_upd = st.selectbox("What do you want to update..?" , options=["Select" , "Que" , "Options" , "Ans"])
            if sel_upd == "Que":
                obj.update_que(update_que)
            if sel_upd == "Options":
                obj.update_opt(update_que)
            if sel_upd == "Ans":
                obj.update_ans(update_que)

    def update_que(self, update_que) :
        obj = JsonOp()
        obj.read_questions()
        new_que = st.text_input("New Question :- ")
        questions[update_que]["que"] = new_que
        if new_que:
            st.subheader("Updated Question :")
            st.subheader(questions[update_que])
            with open(self.path, "w") as f: 
                json.dump(questions, f, indent=4)

    def update_opt(self, update_que) :
        obj = JsonOp()
        obj.read_questions()
        sel_opt = st.selectbox("Which Option do you want to update..?" , options=["Select" , "A" , "B" , "C" , "D"])
        if sel_opt == "A":
            new_a = st.text_input("New Option A :- ")
            questions[update_que]["A"] = new_a
            if new_a:
                st.subheader("Updated Option A :")
                st.subheader(questions[update_que])
                with open(self.path, "w") as f: 
                    json.dump(questions, f, indent=4)
        if sel_opt == "B":
            new_b = st.text_input("New Option B :- ")
            questions[update_que]["B"] = new_b
            if new_b:
                st.subheader("Updated Option B :")
                st.subheader(questions[update_que])
                with open(self.path, "w") as f: 
                    json.dump(questions, f, indent=4)
        if sel_opt == "C":
            new_c = st.text_input("New Option C :- ")
            questions[update_que]["C"] = new_c
            if new_c:
                st.subheader("Updated Option C :")
                st.subheader(questions[update_que])
                with open(self.path, "w") as f: 
                    json.dump(questions, f, indent=4)
        if sel_opt == "D":
            new_d = st.text_input("New Option D :- ")
            questions[update_que]["D"] = new_d
            if new_d:
                st.subheader("Updated Option D :")
                st.subheader(questions[update_que])
                with open(self.path, "w") as f: 
                    json.dump(questions, f, indent=4)
    
    def update_ans(self, update_que) :
        obj = JsonOp()
        obj.read_questions()
        new_que = st.radio("New Answer : " , ["A" , "B" , "C" , "D"] , index=None)
        questions[update_que]["ans"] = new_que
        if new_que:
            st.subheader("Updated Answer :")
            st.subheader(questions[update_que])
            with open(self.path, "w") as f: 
                json.dump(questions, f, indent=4)

    def delete_quetions(self) :
        # global num
        # num+=1
        obj = JsonOp()
        Que = obj.read_questions()
        # for i in range(len(Que)):
        #     (f"{i+1}. {Que[i]}")
        data = []
        for i, q in enumerate(Que):
            st.markdown(f"{i+1}. {q}")
            data.append(i+1)
        data  
        del_que = st.selectbox("Consider the above list and Enter the number that you want to delete" , options=data)
        if del_que:
            button = st.button("Delete")
            if button:
                del Que[del_que - 1]
                with open(self.path , "w") as f:
                    json.dump(Que , f , indent=4)
                st.subheader("Question Deleted\n")
                st.subheader("--- Updated List is as given below ---")
                for i, q in enumerate(Que):
                    st.markdown(f"{i+1}. {q}")
                # obj.further("delete")
                # num += 1
        # if 1 <= del_que <= len(Que):
        #     del Que[del_que - 1]
        #     with open(self.path , "w") as f:
        #         json.dump(Que , f , indent=4)
        #     print("Question removed")
        #     obj.further("delete")
            
        # else:
        #     print("Enter valid number")
            # except ValueError:
            #     print("Please Enter Only Numeric Value...")
            #     print(ValueError)

    # def further(self , action) :
    #     global num
    #     obj = JsonOp()
    #     st.subheader(f"Do you want to {action} further..? ")
    #     leave = st.radio(" " ,("Yes","No") , key=f"radio_{action}",index=None)
    #     # leave = st.selectbox(label= "Answer",options=("Select","Yes","No"))
    #     print()
    #     if leave == "Yes":
    #         if action == "add":
    #             obj.add_questions()
    #         elif action == "delete":
    #             obj.delete_quetions()
    #         elif action == "update":
    #             obj.update_quetions()
    #     elif leave=="No":
    #         st.success("Okay... Question list updated")