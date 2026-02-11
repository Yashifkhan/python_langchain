from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
load_dotenv()  


embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
docsQuery=[
"Harry Potter is a young wizard who fights evil with magic.",
"Doraemon is a robot cat who helps his friend with gadgets.",
"Harry Potter is a young wizard who fights evil with magic.",
"Thor is a god who controls thunder with his hammer."

]
userQuery="tell em about harry"

docsEmbs=embeddings.embed_documents(docsQuery)
userEmbs = embeddings.embed_query(userQuery)

scores=cosine_similarity([userEmbs],docsEmbs)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(userQuery)
print("sementic search : ",docsQuery[index])



from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from dotenv import load_dotenv
load_dotenv()  


embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
docsQuery=[
"Harry Potter is a young wizard who fights evil with magic.",
"Doraemon is a robot cat who helps his friend with gadgets.",
"Harry Potter is a young wizard who fights evil with magic.",
"Thor is a god who controls thunder with his hammer."

]
userQuery="tell em about harry"

docsEmbs=embeddings.embed_documents(docsQuery)
userEmbs = embeddings.embed_query(userQuery)

scores=cosine_similarity([userEmbs],docsEmbs)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(userQuery)
print("sementic search : ",docsQuery[index])