import os
from dotenv import load_dotenv

import streamlit as st
from azure.core.credentials import AzureKeyCredential

# Retrieve the secret from Streamlit secrets
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

# Use it in your chatbot
credential = AzureKeyCredential(GITHUB_TOKEN)



load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
MODEL_ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "o3-mini"

APP_TITLE = "Medical Assistant Chatbot"
APP_DESCRIPTION = """
This chatbot can help answer your medical questions and provide basic health advice.
Note: This is not a substitute for professional medical advice.
"""
