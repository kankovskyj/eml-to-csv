# llm = OpenAI(openai_api_key="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")

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer but your write in pirate tongue."),
#     ("user", "{input}")
# ])

# chain = prompt | llm

# # chain = prompt | llm | output_parser


# result = chain.invoke({"input": "how can langsmith help with testing?"})

# print(result)