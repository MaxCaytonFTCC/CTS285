# Minimal Flask App
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Find template from /templates
    name = "John"
    return render_template("main_page.html", name=name)

@app.route("/action")
def action():
    return "Hello from the action route!"