#LANGCHAIN_API_KEY="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"
#OPENAI_API_KEY="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"
#LANGCHAIN_PROJECT="Bot_Demo"



from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()



#Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING V2"] = "true"

#Chatbot

promt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistance . please provide response to the the user query"),
        ("user","query:{query}")
    ]
)

#streamlit freamwork
st.title("Langchain Demo with Ollama2 API")
input_text = st.text_input("Search the topic you want")


#open AI LLM Call
llm=Ollama(model="llama2")
output_parser=StrOutputParser()

#chain call
chain=promt|llm|output_parser

if input_text:
    st.write(chain.invoke({'query':input_text}))
