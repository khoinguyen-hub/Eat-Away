#Flask connector for html tmeplates and main.py
from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')