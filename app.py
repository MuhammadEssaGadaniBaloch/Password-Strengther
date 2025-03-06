import re
import streamlit as st


# Page Styling 
st.set_page_config(page_title="Password Strength Checker by M Essa Gadani", page_icon="🔑",layout="centered")

# Custom CSS
st.markdown(
     """
<style>
   .main { text-align: center; }
    .stTextInput{width: 60% important; margin:auto;}
    .stButton button {width: 50%;  background-color: #4CAF50; color:bule font-size:18px}
    .tButton button:hover {background-color: #45a049;}
    </style>

    """, unsafe_allow_html=True)


# Title
st.title("🔐Password Strength Checker")  
st.write("Enter your password below to check its strength 🔍.") 

# fuction to check password strength
def check_password_strength(password):
    score =0
    feedback=[]
    if len(password) >= 8:
        score += 1 #increased  score by 1
    else :
        feedback.append("❌ Password shoud be **atlest 8 charactor log**.")

    if re.search(r"[A-Z]", password ) and re.search("r[a-z],password"):
        score +=1 
    else:
        feedback.append("❌ Password shoud be **both  upper case (A-Z) and lower case (a-z) letters**.")

    if re.search(r"\d". password):
        score += 1
    else :
        feedback.append("❌ Password shoud be **atlest 1 number (0-1)**.")

    # Speail Character
    if re.search(r"!@#$%^&*]". password):
        score +=1
    else:
        feedback.append("❌ Inculde ** atlest one speial Character**.")

# Display 
    if score == 4:
        st.success("✅ **Strong Password ** Your Password is secour.")
    if score ==3:
        st.info("⚠️**Moderate Password** - Consider improving secursity by adding more feature")
    else :
        st.error("❌ **Weak password** - Follow the suggestion below to strength it.")

    #FeedBack
    if feedback:
          with st.expander("🔍** Improve your Password**."):
           for item in feedback:
                st.write(item)
    password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong🔐")
    
    #Button
    if st.button("Check strength"):
          if password :
            check_password_strength(password)
          else : 
            st.warning("Please enter a password first!⚠️") #show warning if password is empty


          


