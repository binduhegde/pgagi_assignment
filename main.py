import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
google_api_key = os.getenv("google_api_key")

# Configure Gemini API
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-pro")

# Initialize session state
if "show_chatbot" not in st.session_state:
    st.session_state["show_chatbot"] = False
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "chat_ended" not in st.session_state:
    st.session_state["chat_ended"] = False

# Initialize chat session
if "chat" not in st.session_state:
    st.session_state["chat"] = model.start_chat()

title = '<div style="background: linear-gradient(to right,#F9C58D,#F492F0); color: transparent; color: black; font-family: Helvetica; font-weight: bold; font-size: 40px; text-align: center; padding: 30px; letter-spacing:1px; width: 100%; margin-bottom: 20px;"><h2>TalentScout AI Interview assistant</h2></div>'
st.markdown(title, unsafe_allow_html=True)

if not st.session_state["show_chatbot"]:
    name = st.text_input("Please enter your name")
    contact_no = st.text_input("Please enter your contact number")
    location = st.text_input("Your current city")
    position = st.selectbox("Please select the role you're applying for", ['Data Scientist', 'Full stack developer', 'Frontend Developer', 'Backend Developer'])
    years_of_exp = st.number_input("How many years of experience do you have?", step=1)
    submit_button = st.button("Submit")
    
    if submit_button:
        if not name or not contact_no or not location:
            st.error("Please fill out all the information")
        else:
            st.session_state["user_details"] = {
                "name": name,
                "contact_no": contact_no,
                "location": location,
                "position": position,
                "years_of_exp": years_of_exp,
            }
            st.session_state["show_chatbot"] = True
            
            # Generate initial chatbot prompt
            prompt = f"""
            You are an AI Hiring Assistant chatbot for TalentScout. These are your tasks: 
            1. Given some information about the candidate, greet the candidate first
            2. Ask the candidates to specify their tech stack, including programming languages, frameworks, databases, and tools they are proficient in.
            3. Based on the declared tech stack, generate a set of 3-5 technical questions tailored to assess the candidate’s proficiency in each specified technology.
                Example: If a candidate lists Python and Django, generate questions related to Python programming and Django framework

            
            Rules:
            1. Only ask one question at a time
            2. Don't ask more than 1 question at a time. Let the candidate respond and then ask the next question
            3. Never deviate from the topic. Never talk about something other than their technical stack.
            
            Name = {name}
            Position = {position}
            
            Begin the interview.
            """
            response = st.session_state["chat"].send_message(prompt)
            st.session_state["messages"] = [{"role": "assistant", "content": response.text}]
            st.rerun()
else:
    # Display chat history
    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Disable the input field and end the conversation if chat is ended
    if st.session_state["chat_ended"]:
        st.stop()
    else:
        # User input (only active if chat is not ended)
        user_input = st.chat_input("Type your message...", disabled=st.session_state["chat_ended"])
        
        if user_input:
            if user_input.lower() == 'exit':
                # Disable reply bar and end the conversation
                st.session_state["chat_ended"] = True
                st.success("Chat ended. Thank you!")
                st.stop()

            # Display user message
            st.chat_message("user").write(user_input)
            st.session_state["messages"].append({"role": "user", "content": user_input})
            
            # Send user input and get a response from the assistant
            response = st.session_state["chat"].send_message(user_input)
            bot_reply = response.text
            
            # Display bot response
            with st.chat_message("assistant"):
                st.write(bot_reply)
            st.session_state["messages"].append({"role": "assistant", "content": bot_reply})



