import sqlite3
from flask import Flask, request


app = Flask(__name__)


@app.route('/api/songs', methods=['GET', 'POST'])
def collection():
    if request.method == 'GET':
        pass  # Handle GET all Request
    elif request.method == 'POST':
        pass  # Handle POST request


@app.route('/api/song/<song_id>', methods=['GET', 'PUT', 'DELETE'])
def resource(song_id):
    if request.method == 'GET':
        pass  # Handle GET single request
    elif request.method == 'PUT':
        pass  # Handle UPDATE request
    elif request.method == 'DELETE':
        pass  # Handle DELETE request


if __name__ == '__main__':
    app.debug = True
    app.run()