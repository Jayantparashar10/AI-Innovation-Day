import streamlit as st
from model.chatbot import MedicalChatbot
from utils.helper import format_response, validate_input, sanitize_input
from config.config import APP_TITLE, APP_DESCRIPTION

GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

def initialize_session_state():
    """Initialize session state variables"""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = MedicalChatbot()
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def display_chat_history():
    """Display the chat history with proper formatting"""
    st.subheader("Chat History")
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.write(f"👤 **You:** {message}")
        else:
            st.markdown(f"🤖 **Assistant:** {message}")
        st.markdown("---")

def main():
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🏥",
        layout="wide"
    )
    
    initialize_session_state()
    
    st.title(f"🏥 {APP_TITLE}")
    st.markdown(APP_DESCRIPTION)
    
    # Chat interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_input = st.text_area(
            "Describe your symptoms:",
            key="user_input",
            height=100
        )
    
    with col2:
        if st.button("Get Medical Advice", type="primary"):
            sanitized_input = sanitize_input(user_input)
            is_valid, error_message = validate_input(sanitized_input)
            
            if is_valid:
                with st.spinner("Analyzing your symptoms..."):
                    response = st.session_state.chatbot.get_response(sanitized_input)
                    formatted_response = format_response(response)
                    
                    # Add to chat history
                    st.session_state.chat_history.append(("You", sanitized_input))
                    st.session_state.chat_history.append(("Assistant", formatted_response))
            else:
                st.error(error_message)
    
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()
    
    display_chat_history()

if __name__ == "__main__":
    main()
