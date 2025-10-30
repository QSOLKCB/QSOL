# QSOL Tools

> **"Small Is Beautiful. Fast Is Holy."**

## FTP Deploy Script

A minimal, fast FTP deployment tool using basic-ftp.

### Features

- **Lightweight**: Single file, < 110 lines of code
- **Fast**: Direct FTP upload with minimal overhead
- **Simple**: Environment variable configuration
- **Secure**: .env file support for credentials

### Usage

1. **Install dependencies** (first time only):
   ```bash
   npm install
   ```

2. **Configure credentials** (copy and edit .env.example):
   ```bash
   cp .env.example .env
   # Edit .env with your FTP credentials
   ```

3. **Deploy**:
   ```bash
   npm run deploy
   ```

### Configuration

Set these environment variables in `.env` file or as environment variables:

| Variable    | Description                        | Example              |
|-------------|------------------------------------|----------------------|
| `FTP_HOST`  | FTP server hostname                | `ftp.example.com`    |
| `FTP_USER`  | FTP username                       | `username`           |
| `FTP_PASS`  | FTP password                       | `password`           |
| `FTP_LOCAL` | Local file or directory to upload  | `./dist`             |
| `FTP_REMOTE`| Remote path on FTP server          | `/public_html`       |

### Examples

**Upload a single file**:
```bash
FTP_HOST=ftp.example.com \
FTP_USER=myuser \
FTP_PASS=mypass \
FTP_LOCAL=./index.html \
FTP_REMOTE=/public_html/index.html \
npm run deploy
```

**Upload a directory**:
```bash
FTP_HOST=ftp.example.com \
FTP_USER=myuser \
FTP_PASS=mypass \
FTP_LOCAL=./dist \
FTP_REMOTE=/public_html \
npm run deploy
```

### Security Notes

- Never commit `.env` file to version control
- Use `.env.example` as a template
- The `.env` file is automatically ignored by git

### Dependencies

- **basic-ftp** (^5.0.5): Lightweight FTP client (~216 KB)
  - Zero external dependencies
  - Pure JavaScript implementation
  - Supports both files and directories

### Philosophy

This tool embodies QSOL principles:
- **Small**: 104 lines total, 85 lines of code
- **Fast**: Direct upload with minimal overhead
- **Clear**: Simple, readable implementation
- **Minimal**: Single dependency, no bloat
