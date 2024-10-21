var socket = io.connect();
var username = prompt("Enter your username:");
var room = prompt("Enter room name:");

socket.emit('join', {'username': username, 'room': room});

socket.on('message', function(data) {
    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<p>' + data.user + ': ' + data.message + '</p>';
});

document.getElementById('send-btn').onclick = function() {
    var message = document.getElementById('message-input').value;
    socket.emit('message', {'username': username, 'message': message});
};
