from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
import datetime
app = Flask(__name__)

'''
what i learn:
1. how to use render_template(also templates file + html + for loop in html)
2. var, list, 字典
'''
@app.route('/')
def helloword():
    time = datetime.date.today()
    name = ["zhang", "wang", "zhao"]
    task = {"task":"clean the floor","total time":"3h"}
    return render_template('index.html', var = time, list = name, task = task)

@app.route('/1')
def helloword1():
    return 'Hello World 1'

@app.route('/user/<name>')
def welcome(name):
    return 'Hello %s'%name

@app.route('/user/<int:id>')
def welcome2(id):
    return 'Hello %d'%id

if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
    app.run()
# open http://127.0.0.1:5000/