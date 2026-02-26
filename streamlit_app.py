from openai import OpenAI
import streamlit as st 

user = OpenAI(api_key = " ")
gptmodel = "gpt-4o-mini"
userrole = "user"

pre_prompt = "Teach me the following concept:"
response = ""

st.title("PreffessorGPT app") 
st.divider()
prompt  = st.text_input("What You Want To Learn?")
gpt_button = st.button("Teach Me")
st.caption("Proffessor will work when you press the button.")
st.divider()

if gpt_button:
    with st.spinner("Iam preparing your lecture"):
        response = user.chat.completions.create(
            model = gptmodel,
            messages=[
                {"role":userrole,"content": pre_prompt + prompt}
            ]
        )
    st.snow()
    st.write(response.choices[0].message.content)

