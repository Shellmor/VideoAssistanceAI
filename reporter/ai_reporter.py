import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

MODEL_AI = os.getenv("MODEL_AI")
SYSTEM_ROLE_AI = os.getenv("SYSTEM_ROLE_AI")

def ai_assistant(text: str):
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": MODEL_AI,
        "messages": [
            {"role": "system", "content": SYSTEM_ROLE_AI},
            {"role": "user", "content": text}
        ]
    })
    result = ""
    for line in response.text.strip().split('\n'):
        if line:
            data = json.loads(line)
            result += data["message"]["content"]
    return result
