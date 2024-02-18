from flask import Flask, request, jsonify
from flask_cors import CORS
from requests import Session
from time import sleep
from os import getenv

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url')

    if url:
        with Session() as session:
            response = session.get(url)
            print(response.text)
            print(response.json())

        return jsonify({'EchoBot': 'Echoed!'})
    
    return jsonify({'EchoBot': 'No URL provided!'})
