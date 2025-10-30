"""
Example tasks for QSOL Task Runner
Copy this file to your project and customize it.
"""

import subprocess
import os
from pathlib import Path


def hello():
    """Say hello - demonstrates a simple task"""
    print("Hello from QSOL Task Runner!")
    print("This is a minimal task automation tool.")
    return 0


def build():
    """Build the project - example build task"""
    print("Building project...")
    # Example: compile C code
    # return subprocess.call(['gcc', '-o', 'app', 'main.c'])
    
    # For this demo, just simulate
    print("✓ Build complete (simulated)")
    return 0


def test():
    """Run tests - example test task"""
    print("Running tests...")
    # Example: run pytest
    # return subprocess.call(['python3', '-m', 'pytest'])
    
    # For this demo, just simulate
    print("✓ All tests passed (simulated)")
    return 0


def clean():
    """Clean build artifacts"""
    print("Cleaning build artifacts...")
    
    # Example: remove build files
    artifacts = ['*.o', '*.pyc', '__pycache__', 'dist', 'build']
    
    for pattern in artifacts:
        print(f"  Removing {pattern}...")
    
    print("✓ Clean complete")
    return 0


def lint():
    """Run code linter - example linting task"""
    print("Running linter...")
    # Example: run flake8
    # return subprocess.call(['flake8', '.'])
    
    # For this demo, just simulate
    print("✓ No linting issues found (simulated)")
    return 0


def deploy(env="staging"):
    """Deploy to environment (usage: deploy:production)"""
    print(f"Deploying to {env}...")
    
    # In a real project, you might:
    # 1. Build first
    # 2. Run tests
    # 3. Deploy to target
    
    print(f"✓ Deployed to {env} (simulated)")
    return 0


def all():
    """Run all checks - build, lint, and test"""
    import run
    
    print("Running all checks...")
    print()
    
    # Run tasks in sequence
    tasks = ['build', 'lint', 'test']
    
    for task in tasks:
        if run.run_task(task) != 0:
            return 1
    
    print()
    print("✓ All checks passed!")
    return 0


def watch():
    """Watch for changes and rebuild - example watch task"""
    print("Watching for changes... (Press Ctrl+C to stop)")
    print("(This is a simulated watcher)")
    
    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n✓ Watcher stopped")
        return 0


def info():
    """Show project information"""
    print("Project: QSOL Task Runner Example")
    print("Version: 1.0")
    print("Python:", subprocess.check_output(['python3', '--version']).decode().strip())
    print("Current directory:", os.getcwd())
    return 0
