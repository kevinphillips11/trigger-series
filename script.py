import requests
import json
import os
import time
import threading

# cancel the previous run
print('canceling previous run')

try:
    url = f"https://api.github.com/repos/kevinphillips11/trigger-series/actions/runs/{os.environ['PREVIOUS_RUN_ID']}/cancel"

    payload = json.dumps({
    "ref": "main",
    "inputs": {
        "manual_trigger": "true"
    }
    })
    headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
    'X-GitHub-Api-Version': '2022-11-28'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
except:
    pass

# middle part - print hello




from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = "b5b9a807cf6649128b07b112213b234d"  # Replace with your News API key


@app.route('/')
def index():
    # Fetch top headlines from News API
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()

    # Extract relevant information from the response
    articles = news_data.get('articles', [])

    return render_template('index.html', articles=articles)


def run_flask_app():
    app.run(port=5000)


# Start Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.start()

# Wait for 5 minutes
time.sleep(300)

# Print "hello" after 5 minutes
print("hello")

# Stop the Flask app (you may need to adjust this based on your specific use case)
func = request.environ.get('werkzeug.server.shutdown')
if func is not None:
    func()







# trigger the next run
print('triggering next run')

url = "https://api.github.com/repos/kevinphillips11/trigger-series/actions/workflows/run.yml/dispatches"

payload = json.dumps({
"ref": "main",
"inputs": {
    "previous_run_id": os.environ['CURRENT_RUN_ID']
}
})
headers = {
'Accept': 'application/vnd.github+json',
'Authorization': f'Bearer {os.environ["GITHUB_TOKEN"]}',
'X-GitHub-Api-Version': '2022-11-28',
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# wait to be canceled by the next run
print('waiting to be canceled by next run')

time.sleep(60)
