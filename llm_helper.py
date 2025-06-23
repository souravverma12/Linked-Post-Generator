from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm=ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"),model_name="llama3-70b-8192")
#here you are not running your llm locally . here it takes key and goes t groqcloud and fetches you the data

if __name__=="__main__":
    response=llm.invoke("waht are the two main ingradients in samosa")
    print(response.content)