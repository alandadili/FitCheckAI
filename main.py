from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template="""
Answer the question below

Here is the converstaion history: {context}

Question: {question}

Answer:
"""
model=OllamaLLM(model="llama3.2")
prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

def conversation():
    context=""
    print("Welcome to FitCheckAI, lets check your fit","type 'exit' to end the conversation")
    print("")
    while True:
        user_input=input("You: ")
        if user_input.lower()=="exit":
            break    
        result=chain.invoke({"context":context,"question":user_input})
        print("")
        print("FitCheckAI:",result)
        print("")
        context+=f"\nYou: {user_input}\nFitCheckAI: {result}"

if __name__=="__main__":
    conversation()