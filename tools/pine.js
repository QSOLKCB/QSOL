#!/usr/bin/env node
const Imap = require('imap');
const nodemailer = require('nodemailer');
const { spawn } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');
const readline = require('readline');

const USER = process.env.GMAIL_USER;
const PASS = process.env.GMAIL_PASS;

if (!USER || !PASS) {
  console.error('Error: GMAIL_USER and GMAIL_PASS environment variables required.');
  process.exit(1);
}

let messages = [];
let cursor = 0;
let currentView = 'list';
let currentMessage = null;

const imap = new Imap({
  user: USER,
  password: PASS,
  host: 'imap.gmail.com',
  port: 993,
  tls: true,
  tlsOptions: { rejectUnauthorized: false }
});

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: { user: USER, pass: PASS }
});

function clear() {
  console.clear();
  process.stdout.write('\x1b[H\x1b[2J');
}

function openBox(cb) {
  imap.openBox('INBOX', true, cb);
}

function fetchMessages(cb) {
  imap.once('ready', () => {
    openBox((err) => {
      if (err) return cb(err);
      imap.search(['ALL'], (err, results) => {
        if (err) return cb(err);
        if (!results || results.length === 0) return cb(null, []);
        
        const latest = results.slice(-10);
        const fetch = imap.fetch(latest, { bodies: '', struct: true });
        const msgs = [];
        
        fetch.on('message', (msg, seqno) => {
          let buffer = '';
          let attrs = null;
          
          msg.on('body', (stream) => {
            stream.on('data', (chunk) => buffer += chunk.toString('utf8'));
          });
          
          msg.once('attributes', (a) => attrs = a);
          
          msg.once('end', () => {
            const header = Imap.parseHeader(buffer);
            msgs.push({
              seqno,
              from: (header.from || ['Unknown'])[0],
              subject: (header.subject || ['(no subject)'])[0],
              date: (header.date || ['Unknown'])[0],
              body: buffer
            });
          });
        });
        
        fetch.once('error', cb);
        fetch.once('end', () => {
          imap.end();
          cb(null, msgs.reverse());
        });
      });
    });
  });
  
  imap.once('error', cb);
  imap.connect();
}

function displayList() {
  clear();
  console.log('QSOL-Mail — Text Is Eternal\n');
  console.log('Controls: ↑↓ navigate | Enter open | r reply | q quit\n');
  
  if (messages.length === 0) {
    console.log('No messages.');
    return;
  }
  
  messages.forEach((m, i) => {
    const marker = i === cursor ? '>' : ' ';
    const from = m.from.substring(0, 30);
    const subj = m.subject.substring(0, 40);
    const date = m.date.substring(0, 20);
    console.log(`${marker} ${i + 1}. ${from} | ${subj} | ${date}`);
  });
}

function displayMessage() {
  clear();
  console.log('QSOL-Mail — Message View\n');
  console.log('Controls: r reply | b back | q quit\n');
  
  if (!currentMessage) return;
  
  console.log(`From: ${currentMessage.from}`);
  console.log(`Subject: ${currentMessage.subject}`);
  console.log(`Date: ${currentMessage.date}\n`);
  console.log('─'.repeat(60));
  
  const lines = currentMessage.body.split('\n');
  const textLines = lines.filter(l => !l.match(/^(From|To|Subject|Date|Content-Type|MIME|Message-ID|Received):/i));
  console.log(textLines.join('\n').trim());
}

function replyToMessage() {
  if (!currentMessage) return;
  
  const tmpFile = path.join(os.tmpdir(), `pine-reply-${Date.now()}.txt`);
  const template = `\n\n--- Original Message ---\nFrom: ${currentMessage.from}\nSubject: ${currentMessage.subject}\n`;
  fs.writeFileSync(tmpFile, template);
  
  const editor = process.env.EDITOR || 'nano';
  const child = spawn(editor, [tmpFile], { stdio: 'inherit' });
  
  child.on('exit', (code) => {
    if (code === 0) {
      const body = fs.readFileSync(tmpFile, 'utf8');
      const replySubject = currentMessage.subject.startsWith('Re:') ? currentMessage.subject : `Re: ${currentMessage.subject}`;
      const toMatch = currentMessage.from.match(/<(.+?)>/);
      const to = toMatch ? toMatch[1] : currentMessage.from;
      
      transporter.sendMail({
        from: USER,
        to,
        subject: replySubject,
        text: body
      }, (err) => {
        fs.unlinkSync(tmpFile);
        if (err) {
          console.error('Send failed:', err.message);
          setTimeout(() => {
            if (currentView === 'message') displayMessage();
            else displayList();
          }, 2000);
        } else {
          console.log('Reply sent!');
          setTimeout(() => {
            if (currentView === 'message') displayMessage();
            else displayList();
          }, 1000);
        }
      });
    } else {
      fs.unlinkSync(tmpFile);
      if (currentView === 'message') displayMessage();
      else displayList();
    }
  });
}

function handleInput(key) {
  if (currentView === 'list') {
    if (key === 'q') process.exit(0);
    if (key === '\u001b[A' && cursor > 0) { cursor--; displayList(); }
    if (key === '\u001b[B' && cursor < messages.length - 1) { cursor++; displayList(); }
    if (key === '\r') {
      currentMessage = messages[cursor];
      currentView = 'message';
      displayMessage();
    }
    if (key === 'r' && messages[cursor]) {
      currentMessage = messages[cursor];
      replyToMessage();
    }
  } else if (currentView === 'message') {
    if (key === 'q') process.exit(0);
    if (key === 'b') { currentView = 'list'; displayList(); }
    if (key === 'r') replyToMessage();
  }
}

// Initialize
clear();
console.log('Loading messages...');

fetchMessages((err, msgs) => {
  if (err) {
    console.error('Error:', err.message);
    process.exit(1);
  }
  
  messages = msgs;
  displayList();
  
  process.stdin.setRawMode(true);
  process.stdin.resume();
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', handleInput);
});
