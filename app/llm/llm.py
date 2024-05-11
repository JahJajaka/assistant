from langchain_cohere.llms import Cohere

def get_model():
    return Cohere(max_tokens=256, temperature=0)
