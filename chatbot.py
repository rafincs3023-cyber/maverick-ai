from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]


def get_response(user_message):

    messages.append({
        "role": "user",
        "content": user_message
    })

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": messages
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    result = response.json()

    answer = result["choices"][0]["message"]["content"]

    messages.append({
        "role": "assistant",
        "content": answer
    })

    return answer