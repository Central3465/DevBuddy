import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()  # i forgot about this

api_key = os.environ.get(
    "OPENAI_API_KEY"
)  # attempt to fix openai strange issue of not recognizing env previously
if not api_key:
    print("no openai api variable set")
    api_key = "sk_1234_replaceme"

client = OpenAI(api_key=api_key)


def getResponse(prompt):
    response = client.responses.create(model="gpt-6-luna", instructions="You are a coding assistant that will answer in a short, concise way with no waffling.", input=prompt)
    # for cost purposes, i use gpt-6-luna, you can of course use a smarter model with your own credits
    return response

def saveResponse(prompt, response):
    data = {"prompt": prompt, "response": response.output_text}

    try:
        with open("data/chat.json", "r") as d:
            chathist = json.load(d)
    except (FileNotFoundError, json.JSONDecodeError):
        chathist = []

    chathist.append(data)

    with open("data/chat.json", "w") as d:
        json.dump(chathist, d, indent=4)

def ui():
    while True:
        print(
            "\nWelcome to Codex (BAIDEX). Ask a question below and GPT-6-Luna will answer!"
        )
        prompt = str(input("Write your prompt: ")).strip()
        if prompt.lower() == "exit":
            break
        if not prompt:
            print("please enter a prompt")
            continue
        print(
            "\nBefore you submit, please confirm that you will use this responsibly. "
        )
        confirmation = str(input("Please confirm: (type confirm) ")).strip()
        if confirmation != "confirm":
            print("not confirmed")
            continue
        try:
            answer = getResponse(prompt)
            print("\nAnswer: \n")
            saveResponse(prompt, answer)
            print(answer)
        except Exception as e:
            print(e)