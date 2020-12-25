import nipplejs from 'nipplejs';
import ROSLIB from 'roslib';

var ros = new ROSLIB.Ros({
  url : 'ws://localhost:9090'
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

