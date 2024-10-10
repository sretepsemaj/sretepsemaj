from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the keys
plex_key = os.getenv('PLEX')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/api/query', methods=['POST'])
def process_query():
    data = request.get_json()  # Get the JSON data sent by the frontend
    user_query = data.get("query")  # Extract the query from the data

    if not user_query:
        return jsonify({"error": "No query provided"}), 400

    headers = {
        'Authorization': f'Bearer {plex_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        "model": "llama-3.1-sonar-large-128k-online",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ],
        "max_tokens": 150,
        "temperature": 0.2,
        "top_p": 0.9
    }

    try:
        response = requests.post('https://api.perplexity.ai/chat/completions', headers=headers, json=payload)

        if response.status_code == 200:
            api_data = response.json()
            return jsonify({"response": api_data})
        else:
            return jsonify({"error": f"API request failed with status {response.status_code}"}), 500

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/direct')
def direct():
    return render_template('direct.html')

@app.route('/anchor')
def anchor():
    return render_template('anchor.html')

@app.route('/paper')
def paper():
    return render_template('paper.html')

if __name__ == "__main__":
    app.run(debug=True)  

