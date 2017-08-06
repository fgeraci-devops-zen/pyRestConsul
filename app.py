from flask import Flask
import consul

app = Flask(__name__)

@app.route('/')

def home():
    return "Ok, ci sono. Meet me @ port #5000"



    c = consul.Consul(host='127.0.0.1')

    # Register Service
    c.agent.service.register('pyRestNoSwarm',
                             service_id='pyRestNoSwarm',
                             port=5000)

app.run(host='0.0.0.0', port=5000)