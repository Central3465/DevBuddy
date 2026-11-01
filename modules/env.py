from dotenv import load_dotenv
import os

load_dotenv()

def list():
    variables = {key: os.getenv(key) for key in os.environ.keys()}
    return variables

def scan():
    variables = list()

    if not variables.get("OPENAI_API_KEY"):
        print("OpenAI API key not found.")
    else:
        print(f"OPENAI_API_KEY: {variables['OPENAI_API_KEY']}")