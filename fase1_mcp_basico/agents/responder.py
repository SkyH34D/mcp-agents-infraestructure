import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def responder_agent(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return resp.choices[0].message.content
