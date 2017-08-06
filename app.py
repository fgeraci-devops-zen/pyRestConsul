from flask import Flask
import consul

app = Flask(__name__)

@app.route('/')

def home():
    c = consul.Consul(host='127.0.0.1')

    # Register Service
    c.agent.service.register('pyRestNoSwarm',
                             service_id='pyRestNoSwarm',
                             port=5000,
                             tags=[])
    print(c.agent.services())
    # List all registered Services
    for x in c.agent.services():
        print(x)
        # To remove the service entry
        # c.agent.service.deregister(service_id='my_http_service_1')
    return "Ok, ci sono. Meet me @ port #5000"

home()
app.run(host='0.0.0.0', port=5000)
