from openai import OpenAI
import os
from dotenv import load_dotenv

# Carga la variable de entorno
load_dotenv()
# Crea un cliente explícito, con timeout opcional
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=30)

def responder_agent(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content
