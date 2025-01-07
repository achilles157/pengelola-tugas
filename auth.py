import streamlit as st
import pandas as pd
import os

# File paths
users_file = 'users.csv'

def initialize_users_file():
    if not os.path.exists(users_file):
        # Create the file with headers
        pd.DataFrame(columns=['Username', 'Password']).to_csv(users_file, index=False)

def load_users():
    initialize_users_file()  # Ensure the file is initialized
    return pd.read_csv(users_file)

def sign_up():
    st.subheader("Sign Up")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Register"):
        users = load_users()
        if username in users['Username'].values:
            st.error("Username already exists.")
        else:
            new_user = pd.DataFrame({'Username': [username], 'Password': [password]})
            new_user.to_csv(users_file, mode='a', header=False, index=False)
            st.success("Registration successful! You can now log in.")

def sign_in():
    st.subheader("Sign In")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.button("Login"):
        users = load_users()
        if username in users['Username'].values:
            user_password = users.loc[users['Username'] == username, 'Password'].values[0]
            if password == user_password:
                st.success("Login successful!")
                st.session_state['username'] = username  # Store username in session state
            else:
                st.error("Incorrect password.")
        else:
            st.error("Username not found.")

def logout():
    if 'username' in st.session_state:
        del st.session_state['username']  # Remove username from session state
    st.success("You have been logged out.")

def main():
    st.title("User Authentication")
    choice = st.selectbox("Choose an option", ["Sign Up", "Sign In"])
    
    if choice == "Sign Up":
        sign_up()
    else:
        sign_in()

if __name__ == "__main__":
    main()
