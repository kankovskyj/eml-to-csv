import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


# SEARCH TOOL
search = TavilySearchResults(
    max_results=1,
)


# RETRIEVER TOOL
from langchain.tools.retriever import create_retriever_tool
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.pinecone import Pinecone

embeddings = OpenAIEmbeddings(
    api_key="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"
)

vectorstore = Pinecone.from_existing_index(
    index_name=os.environ["PINECONE_INDEX_NAME"], embedding=embeddings
)
retriever = vectorstore.as_retriever(kwargs={"k": 22})

retriever_tool = create_retriever_tool(
    retriever,
    "carsticks_search",
    "Search for information about Carsticks. For any questions about Carsticks, you must use this tool!",
)


# TOOLS DEFINED HERE
tools = [search, retriever_tool]


# AGENT HERE
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0)

from langchain import hub


# PROMPT HERE
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\

{context}"""
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

# AGENT EXECUTOR
from langchain.agents import create_openai_functions_agent

agent = create_openai_functions_agent(llm, tools, prompt)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)


# CHAT HISTORY

from langchain_core.messages import AIMessage, HumanMessage
