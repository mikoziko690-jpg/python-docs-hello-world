from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "tak se tylko ten teges"
