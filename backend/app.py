from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

PCI_API_KEY = os.getenv("PCI_VAULT_API_KEY")
PCI_BASE_URL = os.getenv("PCI_VAULT_BASE_URL")

@app.route("/")
def home():
    return {"status": "running"}

@app.route("/tokenize", methods=["POST"])
def tokenize():

    payload = request.json

    headers = {
        "Authorization": f"Bearer {PCI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{PCI_BASE_URL}/vault",
        headers=headers,
        json=payload
    )

    return jsonify(response.json())

@app.route("/mock-card")
def mock_card():
    return {
        "cardholder": "Test User",
        "card_number": "4242 4242 4242 4242",
        "expiry": "12/28",
        "balance": 100
    }

if __name__ == "__main__":
    app.run(debug=True)
