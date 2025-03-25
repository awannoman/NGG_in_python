import random
import streamlit as st

# Set background color and text color using CSS
st.markdown(
    """
    <style>
        body {
            background-color: white;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for storing the random number
if 'computer_random_number' not in st.session_state:
    st.session_state.computer_random_number = random.randint(1, 10)
    st.session_state.game_over = False
    st.session_state.message = ""

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 10")
st.markdown("---")

# Input field for user guess
guess = st.number_input("Enter your number:", min_value=1, max_value=10, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    if guess == st.session_state.computer_random_number:
        st.session_state.message = "🎉 Congratulations! You guessed the right number!"
        st.session_state.game_over = True
    elif guess > st.session_state.computer_random_number:
        st.session_state.message = "🔺 Your guess is too high, try again!"
    else:
        st.session_state.message = "🔻 Your guess is too low, try again!"

st.write(st.session_state.message)

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.computer_random_number = random.randint(1, 10)
        st.session_state.game_over = False
        st.session_state.message = ""
