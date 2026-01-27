print("learn gen ai with langchain")


from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
message = HumanMessage(
    content=[
        {"type": "text", "text": "what is the capital of india"},
        
    ]
)
response = model.invoke([message])
print(response.content)