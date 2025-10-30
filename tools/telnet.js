#!/usr/bin/env node
const net = require('net');

const [host = 'lostsounds.tech', port = '443'] = process.argv.slice(2);
const p = parseInt(port);
if (isNaN(p) || p < 1 || p > 65535) {
  console.error('Invalid port. Must be 1-65535.');
  process.exit(1);
}

console.log(`Trying ${host}:${p}...`);

const socket = net.createConnection({ host, port: p }, () => {
  console.log(`Connected to ${host}:${p}`);
  process.stdin.pipe(socket);
});

socket.on('data', data => process.stdout.write(data));
socket.on('error', err => console.error(`Error: ${err.message}`));
socket.on('end', () => console.log('Connection closed by foreign host.'));
