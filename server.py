import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) # Just so we can import GameBot

from flask import Flask, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from GameBot.routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)