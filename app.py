from flask import Flask
import consul

app = Flask(__name__)

@app.route('/')

def home():
    consulhost = input("Input consul address")
    c = consul.Consul(host=consulhost)

    # Register Service
    c.agent.service.register('pyRestNoSwarm',
                             service_id=consulhost,
                             address='192.168.1.2',
                             port=5001,
                             tags=[])
    print("Let's see if - pyRestNoSwarm - I'm on Consul => ")
    print(c.agent.services())
    # List all registered Services
    for x in c.agent.services():
        print(x)
        # To remove the service entry
        # c.agent.service.deregister(service_id='pyRestNoSwarm')
    return "Ok, ci sono. Meet me @ port #5001"

home()
app.run(host='0.0.0.0', port=5001)
