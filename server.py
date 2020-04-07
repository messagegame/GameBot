import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) # Just so we can import GameBot

from flask import Flask, request, redirect


app = Flask(__name__)

from GameBot.routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)