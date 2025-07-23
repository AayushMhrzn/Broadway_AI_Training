import os
import streamlit as st
from groq import Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Streamlit app
st.title("Groq Chatbot (with Memory)")


system_prompt = """You are helpful assistant. You help with user query."""

# Initialize chat memory in session state
if "conversations" not in st.session_state:
    st.session_state.conversations = [{"role": "system", "content": system_prompt}]

# Input box
user_input = st.chat_input("Ask Anything...")

# Show previous conversation history
for msg in st.session_state.conversations[1:]:  # skip system message in display
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# When user sends a new prompt
if user_input:
    st.session_state.conversations.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call the Groq API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = groq_client.chat.completions.create(
                model="gemma2-9b-it",
                messages=st.session_state.conversations,
                max_tokens=500,
                temperature=1,
            )
            ai_output = response.choices[0].message.content
            st.markdown(ai_output)

    # Add assistant reply to memory
    st.session_state.conversations.append({"role": "assistant", "content": ai_output})