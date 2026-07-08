from dotenv import load_dotenv
import os

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)


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

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

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


    return jsonify({
        "reply": answer
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )