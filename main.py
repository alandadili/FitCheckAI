from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below

Here is the conversation history: {context}

Here is the additional data: {data}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def load_data(file_path):
    # Load your data from a text file
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def conversation():
    context = ""
    data = load_data('C:\\Users\\AA\\Documents\\FitCheckAI\\data.txt')
    print("Welcome to FitCheckAI, let's check your fit. Type 'exit' to end the conversation.")
    print("")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break    
        if user_input.strip() == "":
            continue
        result = chain.invoke({"context": context, "data": data, "question": user_input})
        print("")
        print("FitCheckAI:", result)
        print("")
        context += f"\nYou: {user_input}\nFitCheckAI: {result}"

if __name__ == "__main__":
    conversation()