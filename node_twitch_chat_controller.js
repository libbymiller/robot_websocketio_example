const tmi = require('tmi.js');

var io = require('socket.io-client');

// Define configuration options
// username is your bot's username (which may also be yours)
// password generated using https://twitchapps.com/tmi/ (without the 'oauth:' prefix)
const opts = {
  identity: {
    username: "xxxxxx",
    password: "xxxxxxxxxxxxxx"
  },
  channels: [
    "xxxxxxx"
  ]
};

// Create a client with our options
const client = new tmi.client(opts);

// Register our event handlers (defined below)
client.on('message', onMessageHandler);
client.on('connected', onConnectedHandler);

// Connect to Twitch:
client.connect();

//connect to my server
var io = require('socket.io-client');

const url = "wss://myserver/"
var socket = io.connect(url, {reconnect: true});

socket.on("connect", () => {
  console.log("connected");
  socket.emit('message', 'arrived');
});

socket.on("error", () => {
  console.log("error");
});


// Called every time a message comes in
function onMessageHandler (target, context, msg, self) {
  if (self) { return; } // Ignore messages from the bot

  // Remove whitespace from chat message
  const commandName = msg.trim();

  // If the command is known, let's execute it
  if (commandName.startsWith("!")){
    var nc = commandName.substring(1).trim();
    console.log(`* Got a command: ${nc}`);
    switch(nc) {
      case "right":
        console.log("* command is 'right'");
        socket.emit("message", "right");
        break;
      case "left":
        console.log("* command is 'left'");
        socket.emit("message", "left");
        break;
      case "up":
        console.log("* command is 'up'");
        socket.emit("message", "up_a_bit");
        break;
      case "down":
        console.log("* command is 'down'");
        socket.emit("message", "down_a_bit");
        break;
      default:
        console.log(`* Not a command ${nc}`);
        break;
    }    
  } else {
    console.log(`* Not a command ${nc}`);
  }
}


// Called every time the bot connects to Twitch chat
function onConnectedHandler (addr, port) {
  console.log(`* Connected to ${addr}:${port}`);
}

