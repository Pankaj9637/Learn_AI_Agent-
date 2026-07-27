from langchain_core.prompts import  ChatPromptTemplate 
# from langchain_core.output_parsers import JsonOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.tools import tool
from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent

@tool
def multiply(a:int , b:int )  -> int:
    """multiply 2 numbers """
    return a*b

@tool
def add(a:int , b:int ) -> int:
    """adds 2 numbers"""
    return a+b

@tool
def sub(a:int , b:int) -> int:
    """subtracts b from a"""
    return a-b

@tool
def divide(a:int , b:int) -> int:
    """divide a by b"""
    return a/b
    

client = ChatNVIDIA(
  model="deepseek-ai/deepseek-v4-pro",
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

agent = create_agent(
    model=client,
    tools=[add , multiply , sub , divide], 
    system_prompt= """you are a helpful assistant . you can use tools  and answer the question """
)

# response = agent.invoke({
#     "messages":[
#         {
#             "role":"user",
#             "content":"what is answer of following equation  Calculate ((20 + 5) * 4) / 2"
#         }
#     ]
# })
# print(response)
# print()
# print("-"*15)
# print(response["messages"][-1].content)


for chunk in agent.stream({
    "messages":[
        {
            "role":"user",
            "content":"what is answer of following equation  Calculate ((20 + 5) * 4) / 2"
        }
    ]
}
    
):
    print("="*50)
    print(chunk)