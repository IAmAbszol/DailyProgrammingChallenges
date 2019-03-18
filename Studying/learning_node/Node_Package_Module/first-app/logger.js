const EventEmitter = require('events');

var url = 'http://mylogger.io/log';

// Pascal case convention
class Logger extends EventEmitter{
	log(message) {
		// Send an HTTP request
		console.log(message);
		// Raise an event. Now added an event argument object.
		this.emit('messageLogged', {id: 1, url: 'http://'});
	}
}

module.exports = Logger;