import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="You are an AI career coach. Give Rohit one AI career tip in one sentence."
)

print(response.output_text)