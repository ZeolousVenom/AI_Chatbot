import streamlit as st
from utils.model_handler import GemmaChatbot
from utils.theme_manager import apply_theme

# Initialize the chatbot
if "chatbot" not in st.session_state:
    st.session_state.chatbot = GemmaChatbot(model_name="gemma3:1b")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title and description
st.title("💎 Gemma3 Chatbot")
st.caption("A local chatbot powered by Ollama's Gemma3 1B model")

# Theme selection in sidebar
with st.sidebar:
    st.header("Settings :")
    st.subheader("Model Parameters")
    temperature = st.slider("Temperature", 0.1, 1.0, 0.7, 0.1)
    
    st.divider()
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chatbot.clear_context()
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to ask Gemma?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot.generate_response(prompt, temperature)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})