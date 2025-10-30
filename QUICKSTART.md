# QSOL Quick Start Guide

> Get started with QSOL in under 60 seconds

## Installation

```bash
# Clone the repository
git clone https://github.com/QSOLKCB/QSOL.git
cd QSOL
```

That's it. No npm install, no dependency hell, no waiting.

## Try the Templates

### 1. Line Counter (30 seconds)

```bash
cd modules/example

# Count lines in a file
python3 linecount.py README.md

# Or build the C version for maximum speed
bash build.sh
./linecount README.md
```

### 2. Web Server (30 seconds)

```bash
cd modules/webserver

# Serve current directory
python3 serve.py

# Open browser to http://localhost:8000
# Press Ctrl+C to stop
```

### 3. File Converter (60 seconds)

```bash
cd modules/fileconvert

# Create sample JSON
echo '[{"name":"Alice","age":30},{"name":"Bob","age":25}]' > test.json

# Convert to CSV
python3 convert.py test.json test.csv

# Check the result
cat test.csv

# Convert back to JSON
python3 convert.py test.csv test-back.json --pretty
cat test-back.json
```

### 4. Task Runner (60 seconds)

```bash
cd modules/taskrunner

# List available tasks
python3 run.py

# Run a task
python3 run.py hello

# Run multiple tasks
python3 run.py build test
```

## Use QSOL in Your Project

### Option 1: Copy a Template

```bash
# Copy the template you want
cp -r QSOL/modules/webserver my-project/

# Customize it
cd my-project
# Edit the code to fit your needs
```

### Option 2: Learn from Examples

Each module demonstrates QSOL principles:
- Zero dependencies
- Clear, readable code
- Fast execution
- Practical utility

Study the code, understand the patterns, apply to your own projects.

### Option 3: Contribute a Module

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## What's Next?

### Understand the Philosophy

Read [MEMESTACKS_PHILOSOPHY.md](MEMESTACKS_PHILOSOPHY.md) to understand why QSOL exists and how it thinks about software.

### Explore the Constraints

Read [CONSTRAINTS_VALIDATION.md](CONSTRAINTS_VALIDATION.md) to see how we validate the three sacred laws.

### Build Something

The best way to learn QSOL is to use it. Start small:

1. Pick a simple problem
2. Write a minimal solution
3. Ask: "Can I remove 10 lines instead of adding 100?"
4. Measure: Is it fast? Is it clear?
5. Share: Contribute back if it's useful

## Common Patterns

### The QSOL Way

```python
#!/usr/bin/env python3
"""
Tool Name - One sentence description
"""
import sys  # Minimal stdlib imports only

def main():
    """Main entry point - keep it simple"""
    # Parse args (argparse for complex, sys.argv for simple)
    # Do the work
    # Return 0 for success, 1 for error
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

### Key Principles

1. **Use Standard Library First**
   - Python: sys, os, pathlib, argparse, json, csv
   - C: stdio.h, stdlib.h, string.h
   - Only add dependencies if truly necessary

2. **Keep Functions Small**
   - One function, one purpose
   - Aim for <30 lines per function
   - If longer, split it

3. **Make It Obvious**
   - Clear names over short names
   - Explicit over implicit
   - Comments for "why", not "what"

4. **Fail Fast**
   - Validate inputs immediately
   - Give clear error messages
   - Return non-zero on failure

5. **Measure Everything**
   ```bash
   # Build time
   time ./build.sh
   
   # Startup time
   time python3 tool.py --help
   
   # File size
   ls -lh tool.py
   
   # Line count
   wc -l tool.py
   ```

## Troubleshooting

### "Command not found"

Make sure Python 3 is installed:
```bash
python3 --version
```

### "Permission denied"

Make scripts executable:
```bash
chmod +x script.py
```

### "Module not found"

QSOL uses only standard library. If you see import errors:
- For Python: You have Python installed, stdlib is included
- For C: You need a C compiler (gcc, clang)

### "It's too simple!"

That's the point. If you need more features:
1. Add them yourself (you can understand the code)
2. Keep them minimal (every line must justify itself)
3. Consider if you really need them (maybe you don't)

## Examples of Real Use

### Development Server
```bash
cd my-website
python3 /path/to/QSOL/modules/webserver/serve.py
```

### Data Processing Pipeline
```bash
# Download, convert, and process data
curl api.com/data.json | \
  python3 convert.py --from json --to csv | \
  grep "active" | \
  sort -t, -k2 -n > results.csv
```

### Build Automation
```bash
# Copy task runner to your project
cp QSOL/modules/taskrunner/run.py my-project/

# Create your tasks
cat > tasks.py << 'EOF'
def build():
    """Build the project"""
    import subprocess
    return subprocess.call(['gcc', '-o', 'app', 'main.c'])

def test():
    """Run tests"""
    import subprocess
    return subprocess.call(['./app', '--test'])
EOF

# Run tasks
python3 run.py build test
```

## The 5-Minute Challenge

Can you understand a QSOL module in 5 minutes? Try it:

1. Pick a module
2. Read its README (1 min)
3. Read its source code (3 min)
4. Run it (1 min)

If you can't, something is wrong with the module. File an issue.

## Resources

- **Philosophy:** [MEMESTACKS_PHILOSOPHY.md](MEMESTACKS_PHILOSOPHY.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Validation:** [CONSTRAINTS_VALIDATION.md](CONSTRAINTS_VALIDATION.md)
- **Inspiration:** [tinyapps.org](https://tinyapps.org)

## Get Help

- Open an issue on GitHub
- Read the source (it's short!)
- Check existing modules for patterns

Remember: QSOL is about simplicity. If something seems complicated, it probably shouldn't be.

---

**Welcome to QSOL. Start small. Stay fast. Keep it clear.**
