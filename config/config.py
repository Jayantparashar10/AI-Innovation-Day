import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
MODEL_ENDPOINT = "https://models.inference.ai.azure.com"
MODEL_NAME = "o3-mini"

APP_TITLE = "Medical Assistant Chatbot"
APP_DESCRIPTION = """
This chatbot can help answer your medical questions and provide basic health advice.
Note: This is not a substitute for professional medical advice.
"""