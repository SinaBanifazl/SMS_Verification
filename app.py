from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():

    '''this is main page of the site'''
    return "hello"

