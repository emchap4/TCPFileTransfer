from flask import Flask, render_template, jsonify, make_response
from flask_bootstrap import Bootstrap
import webview
import threading

import helper
from helper import *

app = Flask(__name__)
class server_thread(threading.Thread, object):
    def __init__(self):
        threading.Thread.__init__(self, target=self.FlaskRunner)
    
    def FlaskRunner(self):
        app.run()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sender')
def sender():
    return render_template('sender.html')

@app.route('/send/<file>/<ip>/<port>', methods=['GET', 'POST'])
@app.route('/send/<file>/<ip>', methods=['GET', 'POST'])
def send(file, ip, port=6667):
    #    sen = helper.Sender(port, file, ip)
    #sen.run()
    print(str(file)+str(ip)+str(port))
    sen = helper.Sender(port, file, ip)
    sen.run()
    print("File sent!")
    return make_response(jsonify({"message": "Messge sent"}), 200)
#    return render_template('send.html', file=file, ip=ip)

@app.route('/receiver')
def receiver():
    ip = helper.get_ip_addr()
    return render_template('receiver.html', ip=ip)

@app.route('/listening/<file>', methods=['GET', 'POST'])
@app.route('/listening/<file>/<port>', methods=['GET', 'POST'])
def listening(file, port="6667"):
    lis = helper.Listener(port, file)
    lis.run()
    print("File made!")
    return render_template('lis.html', file=file)


def on_closed():
    print("Window closed")

if __name__ == "__main__":
    #srvThread = server_thread()
    #srvThread.start()
    Bootstrap(app)
    app.run(debug=True)

#    window = webview.create_window('File Transfer', "http://127.0.0.1:5000")
 #   window.destroy()
