import streamlit as st
from JSON.json_quiz import JsonOp

num = 0 

class Admin_Quiz:

    def __init__(self):
        self.__username = "admin"
        self.__password = int("2005")
        self.questions_storage = JsonOp()
    
    def authenticate(self , username , password : int):
        if username == self.__username and password == self.__password:
            return True
        else:
            st.error("Username or Password is wrong")
            obj = Admin_Quiz()
            obj.admin()
    
    def admin(self):
        global num
        obj3 = Admin_Quiz()
        obj = JsonOp()
        obj.read_questions()
            # try:
        username = st.text_input("\nEnter the Username: ")
        password = int(st.text_input("\nEnter the password: "))
        if obj3.authenticate(username , password) == True:
                st.subheader("What do you want to do now..?")
                activity = st.selectbox(label="Activity" , options=["Select" , "1 --> Add Question" , "2 --> Delete Question" , "3 --> Update Question" , "4 --> Show dictionary of questions" , "5 --> Exit"] , key=f"activity_{num}" , index=None)
                num += 1
                print()
                if activity == "1 --> Add Question":
                    st.subheader("-----You Want to Add a question-----")
                    obj1 = JsonOp()
                    obj1.add_questions()
                    
                elif activity == "2 --> Delete Question":
                    st.subheader("-----You Want to Delete a question-----")
                    obj2 = JsonOp()
                    obj2.delete_quetions()
                    # st.rerun()

                elif activity == "3 --> Update Question":
                    st.subheader("-----You Want to Update a question-----")
                    obj2 = JsonOp()
                    obj2.update_quetions()
                elif activity == "4 --> Show dictionary of questions":
                    st.subheader("-----This Game consists of questions listed below-----\n")
                    obj = JsonOp()
                    Que = obj.read_questions()
                    for i, q in enumerate(Que):
                        st.markdown(f"**{i+1}. {q}**")
                elif activity == "5 --> Exit":
                    st.success("Okay... Leaving")
        else:
            st.error("Incorrect Password")
