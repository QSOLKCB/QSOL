# QSOL v1.0

> **"Small Is Beautiful. Fast is Holy."**

## Philosophy

QSOL (Quick & Simple Open-source Library) is a modern open-source framework inspired by [tinyapps.org](https://tinyapps.org), dedicated to creating ultra-efficient, minimal, local-first tools that prioritize clarity over complexity.

We believe that software has become unnecessarily bloated. QSOL is a return to the fundamentals:
- **Small is Beautiful** - Every line of code must justify its existence
- **Fast is Holy** - Performance is not a feature, it's a requirement
- **Local-First** - Privacy and independence through local execution
- **Clarity over Complexity** - Simple solutions that anyone can understand and modify

📖 **Read the full doctrine in [MEMESTACKS_PHILOSOPHY.md](MEMESTACKS_PHILOSOPHY.md)**

## Core Principles

### 1. **Size Constraints**
- Each module must be comprehensible in a single sitting
- Source code should be measurable in kilobytes, not megabytes
- Dependencies are a liability, not an asset - use sparingly

### 2. **Speed Constraints**
- Build times measured in seconds, not minutes
- Runtime performance that feels instant
- No bloat, no unnecessary abstractions

### 3. **Transparency Constraints**
- Code should be readable by intermediate programmers
- No magic - explicit over implicit
- Documentation is mandatory, obfuscation is forbidden

## What QSOL Provides

QSOL is a collection of:
- **Minimal Modules** - Small, focused tools that do one thing well
- **Zero-Bloat Design** - No frameworks, minimal dependencies
- **Local-First Architecture** - Run everything on your machine
- **Fast Build Times** - Complete builds in seconds
- **Clear Documentation** - Every module is self-explanatory

## Quick Start

```bash
# Clone the repository
git clone https://github.com/QSOLKCB/QSOL.git
cd QSOL

# Try a template in 30 seconds
cd modules/example
python3 linecount.py README.md

# Start a web server instantly
cd ../webserver
python3 serve.py
```

📚 **See [QUICKSTART.md](QUICKSTART.md) for detailed examples and usage patterns**

## Starter Templates

QSOL provides ready-to-use templates that embody minimalist principles:

### 🧮 [Line Counter](modules/example/) 
Basic file processing utility demonstrating zero-dependency design. **~50 lines** in Python, **<1s** build time.

### 🌐 [Web Server](modules/webserver/)
Minimal static file server with zero dependencies. **~120 lines**, starts in **<50ms**, perfect for development.

### 🔄 [File Converter](modules/fileconvert/)
JSON ⟷ CSV converter using only standard library. **~150 lines**, **>10K rows/sec** throughput.

### ⚡ [Task Runner](modules/taskrunner/)
Simple task automation without npm or make. **~100 lines**, **instant** startup, pure Python power.

Each template is:
- ✅ **Self-contained** - Copy and use immediately
- ✅ **Well-documented** - Clear README with examples
- ✅ **Constraint-compliant** - Size, speed, and clarity validated
- ✅ **Production-ready** - Actually useful, not just demos

## Repository Structure

```
QSOL/
├── README.md                    # This file - philosophy and overview
├── MEMESTACKS_PHILOSOPHY.md     # The complete doctrine
├── CONTRIBUTING.md              # Guidelines for contributors
├── LICENSE                      # Open-source license
└── modules/                     # QSOL modules and templates
    ├── example/                 # Line counter - basic example
    ├── webserver/              # Minimal HTTP server
    ├── fileconvert/            # JSON/CSV converter
    └── taskrunner/             # Task automation tool
```

## Sacred Constraints

Every QSOL module must adhere to:

1. **Build in seconds** - If it takes minutes, it's too complex
2. **Run without bloat** - Minimal memory, minimal dependencies
3. **Honor clarity** - Code as documentation
4. **Stay local** - No unnecessary network calls
5. **Be transparent** - No hidden behavior

## Contributing

We welcome contributions that align with the QSOL philosophy. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

Remember: **The best code is no code. The second best is simple code.**

## License

QSOL is open-source software. See [LICENSE](LICENSE) for details.

## Inspiration

QSOL draws inspiration from:
- [tinyapps.org](https://tinyapps.org) - Celebrating small, focused software
- The Unix Philosophy - Do one thing and do it well
- The Suckless movement - Simplicity and clarity
- Plan 9 - Clean, minimal design

---

*"Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away."* - Antoine de Saint-Exupéry
