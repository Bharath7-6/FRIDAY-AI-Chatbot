import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

# Page settings
st.set_page_config(
    page_title="FRIDAY",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.title("🤖 FRIDAY")
    st.write("Status: ONLINE 🟢")
    st.write("Model: Gemini")
    
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Header
st.title("🤖 FRIDAY")
st.caption("Your Personal AI Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Good day sir. FRIDAY online and ready for your commands."
        }
    ]

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Message FRIDAY...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("FRIDAY is thinking..."):

            response = model.generate_content(prompt)
            reply = response.text

            st.write(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )