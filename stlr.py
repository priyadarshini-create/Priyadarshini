import streamlit as st
import sqlite3
import hashlib



#============================ BACKGROUND IMAGE  ==========================

import base64



st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Soil Recommendation system"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('12.jpg')



# Initialize SQLite3 database
conn = sqlite3.connect("users.db")
c = conn.cursor()

# Create table for storing user information if it doesn't exist
c.execute('''
          CREATE TABLE IF NOT EXISTS users
          (username TEXT PRIMARY KEY, password TEXT)
          ''')
conn.commit()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the user exists
def user_exists(username):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    return c.fetchone()

# Register function
def register():
    st.title("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if password != confirm_password:
        st.warning("Passwords do not match!")
    elif st.button("Register"):
        if user_exists(username):
            st.warning("Username already exists!")
        else:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                      (username, hash_password(password)))
            conn.commit()
            st.success("Registration successful! You can now login.")

# Login function
def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = user_exists(username)
        if user and user[1] == hash_password(password):
            st.success("Login successful!")
            import subprocess
            subprocess.run(['streamlit','run','soil_recomm.py'])
        else:
            st.warning("Invalid credentials. Please try again.")

# Main function
def main():
    st.sidebar.title("Choose an option")
    choice = st.sidebar.radio("Login or Register", ["Login", "Register"])

    if choice == "Register":
        register()
    else:
        login()

if __name__ == "__main__":
    main()
