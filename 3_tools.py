from langchain_core.prompts import  ChatPromptTemplate 
# from langchain_core.output_parsers import JsonOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()

@tool
def multiply(a:int , b:int )  -> int:
    """multiply 2 numbers """
    return a*b

@tool
def add(a:int , b:int ) -> int:
    """adds 2 numbers"""
    return a+b


client = ChatNVIDIA(
  model="meta/llama-3.1-70b-instruct",
  api_key=os.getenv("NVIDIA_API_KEY", "$NVIDIA_API_KEY"), 
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
#   chat_template_kwargs = {"thinking":False},
)

prompt = ChatPromptTemplate([
    ("system" , "you are a helpful assistant . you can use tools  and answer the question "),
    ("human","{text}")
])

client_with_tools = client.bind_tools([multiply , add])

chain = prompt | client_with_tools

response = chain.invoke({
    "text":"what is answer of following 2*(5+2)"
})

if response.tool_calls :
    print(response.tool_calls)
    
print(f"content:\n")
print(response.content)