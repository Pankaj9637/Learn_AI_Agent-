from langchain_core.prompts import  ChatPromptTemplate 
from langchain_core.output_parsers import JsonOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
load_dotenv()

client = ChatNVIDIA(
  model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
  api_key=os.getenv("NVIDIA_API_KEY", "$NVIDIA_API_KEY"), 
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system" , """Return ONLY valid JSON.

Keys:
- answer
- confidence"""
        ),
        ("human" , "{text}")
    ]
)

parser = JsonOutputParser()

chain =  prompt |client | parser

response = chain.invoke({
    "text":"what is capital of india ? "
})

print(response)