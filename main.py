from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

def query_ollama(prompt, model="phi3"):
    url = "http://localhost:11434/api/generate"
    headers = {'Content-Type': 'application/json'}
    data = {
        "model": model,
        "prompt": prompt
    }

    response = requests.post(url, headers=headers, json=data, stream=True)
    response.raise_for_status()

    full_response = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line.decode('utf-8'))
            full_response += chunk.get('response', "")
            if chunk.get('done', False):
                break

    return full_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    print("Received prompt:", data) 
    prompt = data.get('prompt', '')
    answer = query_ollama(prompt)
    return jsonify({'response': answer})

if __name__ == '__main__':
    app.run(debug=True)
