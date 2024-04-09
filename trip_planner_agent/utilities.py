from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# # get the LLM
# def getLLM(model):
#     load_dotenv()   
#     if model == "GOOGLE_API_KEY":
#         llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
#     return llm

# Placeholder classes for Grog and OpenAI (replace with actual implementations)
class ChatGrogGenerativeAI:
    def __init__(self):
        
        pass

class ChatOpenAIGenerativeAI:
    def __init__(self):
        pass
class LLMFactory:
    @classmethod
    def create_llm(cls, model):
        load_dotenv()
        if model == "GOOGLE_API_KEY":
            return ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
        elif model == "GROG":
            return ChatGrogGenerativeAI()
        elif model == "OPENAI":
            return ChatOpenAIGenerativeAI()
        else:
            raise ValueError(f"Invalid LLM model: {model}")

# Get the LLM using the factory
def getLLM(model):
    return LLMFactory.create_llm(model)