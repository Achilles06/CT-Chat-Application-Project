from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")  # Enabling CORS for communication

# Store users and their rooms
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join')
def join_room_page():
    return render_template('join_room.html')

# WebSocket events
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    users[username] = room
    emit('message', f'{username} has joined the room {room}.', room=room)

@socketio.on('message')
def handle_message(data):
    room = users[data['username']]
    message = data['message']
    emit('message', {'user': data['username'], 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app)
