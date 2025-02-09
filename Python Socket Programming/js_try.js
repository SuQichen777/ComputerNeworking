var net = require('net');
console.log('foo');
var server = net.createServer(function(sock) {
    console.log('bar'); 
    sock.on('data', function(binaryData) {
        console.log('baz'); 
    });
});
console.log('qux'); 
server.listen(8080, '127.0.0.1');