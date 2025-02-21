from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

API_URL = "https://h2ogpte.genai.h2o.ai/api/v1/collections/count"
API_KEY = "sk-W8MpkW7M0C6tpVXo4GzN3QWR406iaExVw017L9gT5BejsI6b"  # Replace with your actual API key

@app.route('/api/collections/count', methods=['GET'])
def proxy_request():
    try:
        # Forward request to the real API
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.get(API_URL, headers=headers)
        
        # Return the response from the API
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to reach API", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
