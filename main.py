import os
import streamlit as st

from flask import Flask
from ADMIN.admin_main import Admin_Quiz
from PLAYER.player_main import Player_Quiz

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


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
