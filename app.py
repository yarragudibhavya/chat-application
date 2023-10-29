from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to your own secret key
socketio = SocketIO(app)

# Route to the chat page
@app.route('/')
def chat():
    return render_template('chat.html')

# WebSocket event handler for receiving and broadcasting messages
@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
