# Minimal Flask App
from flask import Flask;

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Welcome to my shiny new Flask app!</p>"