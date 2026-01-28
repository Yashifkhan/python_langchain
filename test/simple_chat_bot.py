from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
load_dotenv()

model =ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

chat_histroy=[]
while True:
    user_input=input("Enter Query : ")
    chat_histroy.append(user_input)
    if(user_input == "exit" or user_input == "buy"):
        break
    respons=model.invoke(chat_histroy)
    chat_histroy.append(respons.content)
    print("Ai : ",respons.content)
print(chat_histroy)