from flask import Flask, request, jsonify, render_template
import json
import random
from chatbot_model import predict_intent

app = Flask(__name__)

# Load intents
with open("intents.json") as file:
    data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"].lower()

    tag = predict_intent(message)

    for intent in data["intents"]:
        if intent["tag"] == tag:
            return jsonify({"response": random.choice(intent["responses"])})

    return jsonify({"response": "Sorry, I don't understand."})

if __name__ == "__main__":
    app.run(debug=True)