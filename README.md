# robot_websocketio_example

Code snippets in python/html/js/node for websocket.io and robots

I happened to be running a 2.3.0 socket.io server anyway, which is why I used 
socket.io not websockets for this. Either would work but they are not the same thing! 
https://socket.io/docs/v4/#what-socketio-is-not

Note that for socket.io and python you need to make sure you have the right versions of everything:
https://github.com/miguelgrinberg/python-socketio/issues/586#issuecomment-754069602

In my case this was python-engineio==3.14.2 python-socketio[client]==4.6.0

You'll need to change "myserver" in the code below to a server running socket.io 
(https://socket.io/docs/v4/server-installation/ or 
https://python-socketio.readthedocs.io/en/latest/server.html)

The code:
 * web_socketio_client.py is running on my pi and connecting to myserver via websockets and moving servos (and displaying stuff on screen etc)
 * web_controller.html is running on myserver as a webpage - it just provides some clickable controls
 * node_twitch_chat_controller.js is a connector between twitch chat and my socket.io server and so the robot that way. It's in node.

The twitch docs here are what I followed: https://dev.twitch.tv/docs/irc

