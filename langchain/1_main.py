import os
from dotenv import load_dotenv
from langchain_core import __version__ as core_version
# from langgraph import __version__ as lggraph_version
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import PromptTemplate , ChatPromptTemplate


load_dotenv()

client = ChatNVIDIA(
  model="nvidia/nemotron-3-nano-omni-30b-a3b-reasoning",
  api_key=os.getenv("NVIDIA_API_KEY", "$NVIDIA_API_KEY"), 
  temperature=0.6,
  top_p=0.95,
  max_tokens=65536,
  # reasoning_budget=16384,
  chat_template_kwargs={"enable_thinking":False}
)

prompt = ChatPromptTemplate.from_messages(
 [
   (
     "system" ,"Translate to {language}"
   ),
   (
     "human" , "{text}"
     
   )
 ]
)

chain = prompt | client
response = chain.invoke({
  "language":"German",
  "text":"I am going to market tomorrow"
})

print(response.content)
# lc_messages = [{"role":"user","content":"what are the wonders of the world"}]

# response = client.invoke(lc_messages, chat_template_kwargs={"enable_thinking":True})
# print("message sent")
# if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
#   print(response.additional_kwargs["reasoning_content"])
# print(response.content)

