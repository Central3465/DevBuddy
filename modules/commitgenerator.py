from openai import OpenAI
from dotenv import load_dotenv
import os
import subprocess
import sys

load_dotenv()

def env():
    try:
        if not os.environ.get("OPENAI_API_KEY"):
            print("api variable not set")
    except Exception as e:
        print(f"error occurred while fetching environment variables: {e}")

    api_key = os.environ.get("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)
    return client

def getdiff():
    try:
        subprocess.run(["git", "add", "."])
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as i:
        print(f"error running git diff: {i.stderr}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: git command not found0")
        return None

def run():
    output = getdiff()

    client = env()
    response = client.responses.create(model="gpt-6-luna", instructions="You are a coding assistant that will use the git diffs provided to generate a commit message. The commit message should be concise, short and clear.", input=output)

    return response.output_text