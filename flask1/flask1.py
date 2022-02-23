'''
following tutorial from the docs.
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloflask():
	return 'Hello, Flask.'