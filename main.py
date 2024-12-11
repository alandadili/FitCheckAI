#langchain doesnt work the one time so I updated it
#make sure to run ollama
#to run ollama type into terminal ollama run llama3.2
#make sure to install py -m pip install langchain-ollama and py -m pip install langchain-core
#optional if not working install -m pip install ollama
#!!! VERY IMPORTANT the python stuff isnt on path fix that might have to do with the venv !!!

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
    data = load_data(r"C:\Users\AA\Documents\FitCheckAI\FitCheckAI\data.txt")   #changed to raw string
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