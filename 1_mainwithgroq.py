import os
from dotenv import load_dotenv
from langchain_core import __version__ as core_version
# from langgraph import __version__ as lggraph_version
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate , ChatPromptTemplate
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

prompt = ChatPromptTemplate.from_messages(
 [
   (
     "system" ,"Write a article on  {topic}"
   ),
   (
     "human" , "{title}"
     
   )
 ]
)

chain = prompt | client
input  = {
  "topic":"AI",
  "title":"How to make AI ethical . The 2 sides of a coin"
}

async def stream_chain_response():
    total_characters = 0
    inputs = input
    print("Streaming Response: ", end="", flush=True)

    # Use chain.astream instead of model.astream to pass inputs through the prompt template
    async for chunk in chain.astream(inputs):
        # In LCEL, chunks from chat models are AIMessageChunk objects
        text_chunk = chunk.content
        
        if text_chunk:
            # Print the text chunk immediately without adding newlines
            print(text_chunk, end="", flush=True)
            total_characters += len(text_chunk)
            
    print(f"\nTotal characters: {total_characters}")

# 3. Run the async loop
asyncio.run(stream_chain_response())
            
# print(response.content)
# lc_messages = [{"role":"user","content":"what are the wonders of the world"}]

# response = client.invoke(lc_messages, chat_template_kwargs={"enable_thinking":True})
# print("message sent")
# if response.additional_kwargs and "reasoning_content" in response.additional_kwargs:
#   print(response.additional_kwargs["reasoning_content"])
# print(response.content)

