from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
load_dotenv()

model =ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")


chat_histroy=[
    SystemMessage("you are a helpful assistant")   
]
while True:
    user_input=input("Enter Query : ")
    chat_histroy.append(HumanMessage(user_input))
    if(user_input == "exit" or user_input == "buy"):
        break
    respons=model.invoke(chat_histroy )
    chat_histroy.append(AIMessage(respons.content))
    print("Ai : ",respons.content)
print(chat_histroy)