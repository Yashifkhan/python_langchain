from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage  

from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")



loader=PyPDFLoader('Machine_Learning_Beginner_Guide.pdf')
docs=loader.load()
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="create a summery absed on the my flowiign text '\n' {text}."),
    ("human", "{text}")
])

parser = StrOutputParser()

chain=prompt | model | parser

result=chain.invoke(docs[1].page_content)
print(result)