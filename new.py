import os

from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader

from langchain_community.vectorstores.pinecone import Pinecone

from pinecone import __version__


os.environ["OPENAI_API_KEY"] = "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"
os.environ["PINECONE_API_KEY"] = "15a6528d-f365-4d9e-825a-4962214da1d8"
os.environ["PINECONE_ENV"] = "gcp-starter"


loader = TextLoader("./carsticks.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()

query = "Co je to carsticks?"

docsearch = Pinecone.from_documents(docs, embeddings, index_name="two")


# docs = docsearch.similarity_search(query)

# print(docs[0].page_content)