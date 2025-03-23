import re
import streamlit as st

# Page Styling 
st.set_page_config(page_title="Password Strength Checker by M Essa Gadani", page_icon="🔑", layout="centered")

# Custom CSS to center input field
import streamlit as st

st.markdown(
    """
    <style>
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .stTextInput > div {
            margin: 0 auto !important;
            width: 50% !important;
        }
        .stButton > button {
            display: block;
            margin: 10px auto !important;
            width: 50% !important;
            background-color: #4CAF50 !important;
            color: white !important;
            font-size: 18px !important;
        }
        .stButton > button:hover {
            background-color: #45a049 !important;
        }
    </style>
    """, 
    unsafe_allow_html=True
)

# Title
st.title("🔐 Password Strength Checker")  
st.write("Enter your password below to check its strength 🔍.") 

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Uppercase and lowercase letters check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **at least 1 number (0-9)**.")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display result
    if score == 4:
        st.success("✅ **Strong Password!** Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Feedback section
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Input field (centered using CSS)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")

# Button to check password strength
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")
