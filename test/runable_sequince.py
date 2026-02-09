from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage  # ✅ Fixed import
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Write a joke about {topic}."),
    ("human", "{topic}")
])

prompt2 = ChatPromptTemplate.from_messages([
    SystemMessage(content="explain about this jock {text}."),
    ("human", "{text}")
])

parser = StrOutputParser()
chain = RunnableSequence(prompt, model, parser,prompt2,model,parser)

response = chain.invoke({"topic": "machine learning"})
print(response)

