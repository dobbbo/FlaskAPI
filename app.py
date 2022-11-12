from flask import Flask

# Created app instance and passed import name.
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!'