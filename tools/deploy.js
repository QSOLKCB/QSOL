#!/usr/bin/env node
/**
 * QSOL FTP Deploy Script
 * Small Is Beautiful. Fast Is Holy.
 * 
 * Uploads files to FTP server using basic-ftp
 * Usage: node tools/deploy.js
 * 
 * Required environment variables:
 *   FTP_HOST   - FTP server hostname
 *   FTP_USER   - FTP username
 *   FTP_PASS   - FTP password
 *   FTP_LOCAL  - Local file/directory path to upload
 *   FTP_REMOTE - Remote path on FTP server
 */

const ftp = require('basic-ftp');
const fs = require('fs');
const path = require('path');

// Load environment variables from .env file if it exists
const envPath = path.join(__dirname, '..', '.env');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf8');
  envContent.split('\n').forEach(line => {
    const match = line.match(/^([^=:#]+)=(.*)$/);
    if (match) {
      const key = match[1].trim();
      const value = match[2].trim();
      if (!process.env[key]) {
        process.env[key] = value;
      }
    }
  });
}

async function deploy() {
  const config = {
    host: process.env.FTP_HOST,
    user: process.env.FTP_USER,
    password: process.env.FTP_PASS,
    localPath: process.env.FTP_LOCAL,
    remotePath: process.env.FTP_REMOTE
  };

  // Validate configuration
  const missing = [];
  if (!config.host) missing.push('FTP_HOST');
  if (!config.user) missing.push('FTP_USER');
  if (!config.password) missing.push('FTP_PASS');
  if (!config.localPath) missing.push('FTP_LOCAL');
  if (!config.remotePath) missing.push('FTP_REMOTE');

  if (missing.length > 0) {
    console.error('Error: Missing required environment variables:');
    missing.forEach(v => console.error(`  - ${v}`));
    console.error('\nSet them in .env file or as environment variables.');
    process.exit(1);
  }

  // Validate local path exists
  if (!fs.existsSync(config.localPath)) {
    console.error(`Error: Local path does not exist: ${config.localPath}`);
    process.exit(1);
  }

  const client = new ftp.Client();
  client.ftp.verbose = true;

  try {
    console.log('Connecting to FTP server...');
    await client.access({
      host: config.host,
      user: config.user,
      password: config.password,
      secure: false
    });

    console.log(`Connected to ${config.host}`);
    console.log(`Uploading ${config.localPath} to ${config.remotePath}...`);

    const stats = fs.statSync(config.localPath);
    
    if (stats.isFile()) {
      // Upload single file
      await client.uploadFrom(config.localPath, config.remotePath);
      console.log(`✓ Uploaded file: ${config.localPath} → ${config.remotePath}`);
    } else if (stats.isDirectory()) {
      // Upload directory
      await client.uploadFromDir(config.localPath, config.remotePath);
      console.log(`✓ Uploaded directory: ${config.localPath} → ${config.remotePath}`);
    }

    console.log('Deploy completed successfully!');
  } catch (err) {
    console.error('Deploy failed:', err.message);
    process.exit(1);
  } finally {
    client.close();
  }
}

// Run deploy
deploy();
