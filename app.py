from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Ok, ci sono. Meet me @ port #5000"

app.run(host='0.0.0.0', port=5000)



