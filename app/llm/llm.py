from langchain_cohere.llms import Cohere
from langchain_openai import ChatOpenAI
import os

def get_model():
    model_name = os.getenv('LLM_MODEL')
    if model_name == 'cohere':
        return Cohere(max_tokens=256, temperature=0)
    elif model_name == "gpt-3.5-turbo":
        return ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv('OPENAI_KEY'), max_tokens=500)
    elif model_name == 'gpt-4o':
        return ChatOpenAI(model='gpt-4o', api_key=os.getenv('OPENAI_KEY'), max_tokens=500)
    else:
        return "No model like this configured!"
    
