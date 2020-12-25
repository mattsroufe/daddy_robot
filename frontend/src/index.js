import nipplejs from 'nipplejs';
import ROSLIB from 'roslib';

// Create a connection to the rosbridge WebSocket server.
if (window.location.protocol == "https:") {
  var ws_scheme = "wss://";
} else {
  var ws_scheme = "ws://"
};

var ros = new ROSLIB.Ros({
  url : ws_scheme + window.location.hostname + ':9090'
});

ros.on('connection', function() {
  document.getElementById("status").innerHTML = "Connected";
});

ros.on('error', function(error) {
  document.getElementById("status").innerHTML = "Error";
});

ros.on('close', function() {
  document.getElementById("status").innerHTML = "Closed";
});

var options = {
  mode: 'static',
  position: {left: '50%', top: '50%'},
  color: 'red',
  size: 150,
  lockY: true
};

nipplejs.create(Object.assign(options, {zone: document.getElementById('zone_joystick_1')}));
nipplejs.create(Object.assign(options, {zone: document.getElementById('zone_joystick_2')}));

