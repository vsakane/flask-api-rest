# thank you https://mherman.org/blog/flask-for-node-developers/
# error 404 :(

import sqlite3
from flask import Flask


app = Flask(__name__)


if __name__ == '__main__':
    app.debug = True
    app.run()