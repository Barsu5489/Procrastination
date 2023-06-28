from flask import Flask

app = Flask(__name__)

@ap.route('/')
def index():
    return "Hello World"