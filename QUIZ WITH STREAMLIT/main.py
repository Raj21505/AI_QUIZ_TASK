import streamlit as st

from ADMIN.admin_main import Admin_Quiz
from PLAYER.player_main import Player_Quiz

class Quiz:
    demo = st.subheader("Who are you?" )
    if demo:
        role = st.selectbox(label="Role" , options=["Select","1 --> Admin","2 --> Player","3 --> Leave"] )
        # score += 1

        if role == "1 --> Admin":
            obj = Admin_Quiz()
            obj.admin()
        elif role == "2 --> Player":
            obj = Player_Quiz()
            obj.player()
        elif role == "3 --> Leave":
            st.write("Exiting...Goodbye!")        