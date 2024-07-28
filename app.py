from flask import Flask
app = Flask(__name__)
import socketio

# Create a Socket.IO server
sio = socketio.Server()

# Create a WSGI application
application = socketio.WSGIApp(sio,app)


users = []
# Handle a message event
@sio.event
def message(sid, data):
    print(f'Message from {sid}: {data}')
    sio.send(f'Server received: {data}')

# Handle a connect event
@sio.event
def connect(sid, environ):
    users.append(sid)
    print('Client connected: ', sid, " 1 of ", len(users))
    sio.send(f'{sid} connected to server')

# Handle a disconnect event
@sio.event
def disconnect(sid):
    del users[users.index(sid)]
    sio.send(f'{sid} left')
    print('Client disconnected: ', sid)



@app.route('/')
def hello_world():
    return 'Hello, World!'
