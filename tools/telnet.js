#!/usr/bin/env node
const net = require('net');

const [host = 'lostsounds.tech', port = '443'] = process.argv.slice(2);

console.log(`Trying ${host}:${port}...`);

const socket = net.createConnection({ host, port: parseInt(port) }, () => {
  console.log(`Connected to ${host}:${port}`);
});

socket.on('data', data => process.stdout.write(data));
socket.on('error', err => console.error(`Error: ${err.message}`));
socket.on('end', () => console.log('Connection closed by foreign host.'));

process.stdin.pipe(socket);
