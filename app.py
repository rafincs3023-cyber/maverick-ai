from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)


API_KEY = "sk-or-v1-8388c28ae03c2cf677c73e9040c1c74013b7296b71"


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


app.run(debug=True)