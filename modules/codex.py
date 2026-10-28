import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def getResponse(prompt):
    response = client.responses.create(model="gpt-6-luna", instructions="You are a coding assistant that will answer in a short, concise way with no waffling.", input=prompt)
    # for cost purposes, i use gpt-6-luna, you can of course use a smarter model with your own credits
    return response

def ui():
    while True:
        print("\nWelcome to Codex (BAIDEX). Ask a question below and GPT-6-Luna will answer!")
        prompt = str(input("Write your prompt: "))
        print("\nBefore you submit, please confirm that you will use this responsibly. ")
        confirmation = str(input("Please confirm: (type confirm) "))
        if confirmation != "confirm":
            print("not confirmed")
        else:
            getResponse(prompt)

        if prompt == "":
            return
        else:
            print("\nAnswer: \n")
            print(prompt)