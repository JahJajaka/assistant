from langchain_cohere.llms import Cohere
from langchain_openai import ChatOpenAI
import os

def get_model():
    return Cohere(max_tokens=256, temperature=0)

def get_openai_model():
    #gpt-3.5-turbo gpt-4o
    return ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv('OPENAI_KEY'))
