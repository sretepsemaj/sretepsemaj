from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the keys
plex_key = os.getenv('PLEX')

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for using session

# Simulated user data for login (replace with real authentication logic)
users = {'admin': 'Jaclyn420'}

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if user credentials are correct
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('admin'))
        return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('report'))

# Route for the report page (public)
@app.route('/report')
def report():
    return render_template('report.html')

# Route for the admin page (protected)
@app.route('/admin')
def admin():
    # Only let admin access the admin page
    if 'username' not in session or session['username'] != 'admin':
        return redirect(url_for('login'))
    return render_template('admin.html')  # Available only to admin

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# API query route
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

# Other routes for additional pages
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
