import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_ollama   import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from langchai-c!")
    information = """
    Elon Musk is an industrialist, entrepreneur, and the wealthiest person in recorded history, with an estimated net worth of $1.1 trillion as of October 2026. He achieved the milestone of becoming the world's first trillionaire in June 2026 following the highly anticipated initial public offering (IPO) of his aerospace company, SpaceX.
Musk serves as the CEO of both Tesla and SpaceX, steering global shifts in electric vehicles, autonomous robotics, and aerospace technology.
    """

    summary_template = """
    given the information {information} about a person I want you to create: 
    1. A short Summary
    2. Two interesign facts about them
"""
    summary_template_prompts = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # llm = ChatOpenAI(temperature=0, model="gpt-5")
    #llm = ChatOllama(temperature=0, model="gpt-oss:20b")
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_template_prompts | llm
    response = chain.invoke(input={"information" : information})

    print(response.content)

if __name__ == "__main__":
    main()
