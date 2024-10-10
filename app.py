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
    
    # Simulate an API call or do actual processing here
    headers = {
        'Authorization': f'Bearer {plex_key}'
    }

    # Example external API request (replace with actual API endpoint)
    response = requests.get(f'https://api.example.com/search?q={user_query}', headers=headers)

    # Return the result of the API call to the frontend
    if response.status_code == 200:
        api_data = response.json()
        return jsonify({"response": api_data})
    else:
        return jsonify({"error": "API request failed"}), 500

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

