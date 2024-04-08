# from langchain_core.messages import AIMessage, HumanMessage
# from langchain_community.document_loaders import WebBaseLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import Chroma
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain.chains import create_history_aware_retriever, create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os


def getLLM(model):
    load_dotenv()   
    if model == "GOOGLE_API_KEY":
        llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
    return llm

