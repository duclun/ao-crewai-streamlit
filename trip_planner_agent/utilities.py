from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# get the LLM
def getLLM(model):
    load_dotenv()   
    if model == "GOOGLE_API_KEY":
        llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    return llm

