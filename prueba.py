from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit

HTML = '''
<html>
<head>
    <script src="https://cdn.socket.io/socket.io-1.0.4.js"></script>
    <script>
    var socket = io();
    </script>
</head>
<body>
Hello
</body>
</html>
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return HTML

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
    app.run(host='0.0.0.0', port=9080)