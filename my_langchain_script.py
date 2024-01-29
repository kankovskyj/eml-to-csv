import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores.pinecone import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# Keys
PINECONE_API_KEY = os.environ["PINECONE_API_KEY"]
PINECONE_ENVIRONMENT = os.environ["PINECONE_ENVIRONMENT"]
PINECONE_INDEX_NAME = os.environ["PINECONE_INDEX_NAME"]

# pinecone = PineconeClient(api_key=PINECONE_API_KEY,
#                          environment=PINECONE_ENVIRONMENT)

embeddings = OpenAIEmbeddings(
    api_key="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"
)
vectorstore = Pinecone.from_existing_index(
    index_name=PINECONE_INDEX_NAME, embedding=embeddings
)

retriever = vectorstore.as_retriever(kwargs={"k": 22})


# RAG prompt
template = """Always answer in English. Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# RAG
model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-1106")

chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)

res = chain.invoke("What is carsticks.cz?")

print(res)
