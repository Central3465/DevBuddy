from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if os.getenv("OPENAI_API_KEY") else None

def explain_code(code):
    if client is None:
        raise RuntimeError("api key not set")

    prompt = f"Please explain the following code in detail to me:\n\n{code}\n\nPlease provide a clear and concise explanation."

    response = client.responses.create(model="gpt-6-sol", instructions="You are a coding assistant that will answer in a short, concise way with no waffling. ", input=prompt)

    return response.output_test

def explain_error(error):
    if client is None:
        raise RuntimeError("api key not set")

    prompt = f"Please explain the following error in detail to me like I am a baby:\n\n{error}\n\nPlease provide a clear and concise explanation and the steps to fix it"

    response = client.responses.create(model="gpt-6-sol", instructions="You are a coding assistant that will answer in a short, concise way with no waffling. ", input=prompt)

    return response.output_test