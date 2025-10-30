# Task Runner

> A minimal task automation tool in ~100 lines

## Purpose

Simple task automation without npm, make, or heavy build tools. Define tasks in a simple file and run them.

## Philosophy Demonstration

This module exemplifies QSOL constraints:
- **Size**: ~100 lines of code, zero dependencies
- **Speed**: Instant startup, fast execution
- **Transparency**: Plain Python, easy to understand and modify

## Installation

```bash
# No installation needed - just run it
python3 run.py [task]
```

## Usage

Create a `tasks.py` file:

```python
"""Project tasks"""

def build():
    """Build the project"""
    print("Building...")
    # Your build commands here
    return 0

def test():
    """Run tests"""
    print("Running tests...")
    # Your test commands here
    return 0

def clean():
    """Clean build artifacts"""
    print("Cleaning...")
    # Your clean commands here
    return 0
```

Run tasks:

```bash
# List available tasks
python3 run.py

# Run a task
python3 run.py build

# Run multiple tasks
python3 run.py clean build test
```

## Advanced Tasks

### Task with arguments

```python
def deploy(env="staging"):
    """Deploy to environment"""
    print(f"Deploying to {env}...")
    return 0
```

```bash
python3 run.py deploy:production
```

### Task dependencies

```python
def deploy():
    """Deploy (builds and tests first)"""
    import run
    if run.run_task('build') != 0:
        return 1
    if run.run_task('test') != 0:
        return 1
    print("Deploying...")
    return 0
```

### Running shell commands

```python
import subprocess

def lint():
    """Run linter"""
    result = subprocess.run(['flake8', '.'], capture_output=True)
    print(result.stdout.decode())
    return result.returncode
```

## Features

- ✅ Simple task definitions (just Python functions)
- ✅ Task listing with descriptions
- ✅ Multiple task execution
- ✅ Task arguments
- ✅ Return code handling
- ✅ Zero configuration
- ❌ No complex DAG dependencies (keep it simple)
- ❌ No parallel execution (use & in shell if needed)

## Constraints Met

- **Lines of code**: ~100
- **Dependencies**: 0 external
- **Startup time**: <50ms
- **Task overhead**: <10ms

## Example Project

```
my-project/
├── tasks.py          # Task definitions
├── run.py            # QSOL task runner (copy here)
├── src/              # Your source code
└── tests/            # Your tests
```

```python
# tasks.py
import subprocess
import os

def build():
    """Compile the project"""
    return subprocess.call(['gcc', '-o', 'app', 'src/main.c'])

def test():
    """Run all tests"""
    return subprocess.call(['python3', '-m', 'pytest', 'tests/'])

def run():
    """Run the application"""
    if build() != 0:
        return 1
    return subprocess.call(['./app'])

def clean():
    """Remove build artifacts"""
    if os.path.exists('app'):
        os.remove('app')
    print("Cleaned!")
    return 0

def all():
    """Build and test"""
    if build() != 0:
        return 1
    return test()
```

## Why This Template?

Demonstrates:
1. **Task automation** - Common developer need
2. **Zero overhead** - No complex build systems
3. **Pure Python** - No DSL to learn
4. **Extensible** - Full Python power when needed

## Comparison

### Traditional (Makefile, npm scripts, etc.)
- ❌ New syntax to learn
- ❌ Platform-specific issues
- ❌ Complex dependencies
- ❌ Slow startup (npm especially)

### QSOL Task Runner
- ✅ Just Python functions
- ✅ Works everywhere Python does
- ✅ Zero dependencies
- ✅ Instant startup
- ✅ Full language power

---

*This is QSOL: Small, Fast, Clear.*
