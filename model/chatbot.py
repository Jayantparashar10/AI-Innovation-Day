from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from config.config import GITHUB_TOKEN, MODEL_ENDPOINT, MODEL_NAME

class MedicalChatbot:
    def __init__(self):
        self.client = ChatCompletionsClient(
            endpoint=MODEL_ENDPOINT,
            credential=AzureKeyCredential(GITHUB_TOKEN),
            api_version="2024-12-01-preview"
        )
        self.system_prompt = """You are a medical AI Agent. You detect diseases based on the symptoms entered by user. 
        You will give appropriate actions to take and medicines commonly used for treatment. 
        You will also suggest alternate medicine names with same compound."""

    def get_response(self, user_input):
        try:
            response = self.client.complete(
                stream=False,
                messages=[
                    SystemMessage(content=self.system_prompt),
                    UserMessage(content=user_input)
                ],
                model=MODEL_NAME
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def __del__(self):
        if hasattr(self, 'client'):
            self.client.close()