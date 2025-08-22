from flask import Blueprint, request, jsonify
from openai import OpenAI, RateLimitError
from dotenv import load_dotenv
import os
import time

chat_bp = Blueprint("chat", __name__)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "settings.env"))

@chat_bp.route("/get-gpt-reply", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    print("API KEY:", os.getenv("OPENAI_API_KEY"))

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    retries = 3
    reply = ""
    for i in range(retries):
        try:
            completion = client.chat.completions.create(
                model="deepseek/deepseek-chat-v3-0324:free",
                messages=[{"role": "user",
                           "content": user_message}]
            )
            reply = completion.choices[0].message.content
            return jsonify({"reply": reply})
        except RateLimitError as e:
            print(f"Rate limit hit. Retrying in {2 ** i} seconds...")
            time.sleep(2 ** i)
            reply = "服务繁忙，请稍后再试。"
    return jsonify({"reply": reply})
