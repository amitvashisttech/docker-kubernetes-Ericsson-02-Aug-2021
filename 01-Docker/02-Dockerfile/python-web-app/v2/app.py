from flask import Flask
import os 
import socket 


app = Flask(__name__)


@app.route("/")
def hello():
    html= "<h2> Welcome to the world of Docker</h2>"
    return html



@app.route("/hello")
def hello_test():
    html= "<h2>Hello from docker apache web server.!!</h2>"
    return html


@app.route("/info")
def hello_info():
    html = "<h2>Hello World</h2>"\
           "<b>Hostname:</b> {hostname}<br/>"\
           "<b>FQDN:</b> {fqdn}<br/>"
    return html.format(hostname=socket.gethostname(),fqdn=socket.getfqdn())


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80)

