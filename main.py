from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

model = ChatOllama(model="tinyllama")

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI assistant. Answer the user's questions clearly and concisely.",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

chain = prompt | model

def handle_conversation():
    chat_history = []
    print("Welcome to the AI Chat! Type 'exit' to quit.")

    while True:  
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            break
        
        result = chain.invoke({"chat_history": chat_history, "question": user_input})
        
        # result.content contains the string output in ChatOllama
        print(f"AI: {result.content}")
        
        chat_history.extend(
            [
                HumanMessage(content=user_input),
                AIMessage(content=result.content),
            ]
        )

if __name__ == "__main__":
    handle_conversation()