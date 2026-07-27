


### CREATING fIRST LANGRAPH AGENT 


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate , ChatPromptTemplate
from pydantic import BaseModel
import asyncio


load_dotenv()

client = ChatGroq(
    model="qwen/qwen3.6-27b",
    api_key=os.getenv("GROQ_API_KEY", "$GROQ_API_KEY"), 
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    # other params...
)


# Create first graph agent 

#define schema
class  Schema(BaseModel):
    name : str 
    message : str
    
#create node    
def welcome(state : Schema)-> Schema:
    name = state.name
    message = state.message
    
    response = client.invoke(f"My name is {name} and message is {message}").content
    
    state.message = f"your message was {message} . Here's my response {response}"
    
    return state

from langgraph.graph import StateGraph , START , END
#add nodes
graph = StateGraph(Schema)

graph.add_node("welcome" , welcome)


#connect edges 
graph.add_edge(START , "welcome")
graph.add_edge("welcome" , END)

compiled_graph = graph.compile()

#run the graph 

response = compiled_graph.invoke({
    "name":"Pankaj" ,
    "message":"how are you "
})

print(response)



    
    
    
    