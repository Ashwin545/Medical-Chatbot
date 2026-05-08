system_prompt =(
    "Your are a Medical assistant for question-answering tasks."
    "Use the following retrieved documents to answer the question. If you don't know the answer, say you don't know." \
    "the question. If yuo don't know the answer, say you don't know."
    "answer concisely and accurately."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)