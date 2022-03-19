from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html',
    leftPic='avatar-0a1c0bc58c596766d78dbc157b4e0c5c.jpg',
    rightPic='avatar-0a48007a0f9a5f331b5282cd6b1b72ca.jpg')