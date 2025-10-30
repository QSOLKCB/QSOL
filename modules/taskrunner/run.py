#!/usr/bin/env python3
"""
QSOL Task Runner
Minimal task automation in pure Python.
"""

import sys
import importlib.util
from pathlib import Path


def load_tasks(filename='tasks.py'):
    """
    Load tasks from a Python file.
    
    Returns:
        module: The loaded tasks module
    """
    if not Path(filename).exists():
        return None
    
    spec = importlib.util.spec_from_file_location("tasks", filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def list_tasks(tasks_module):
    """
    List all available tasks with their descriptions.
    
    Args:
        tasks_module: The loaded tasks module
    """
    print("Available tasks:")
    print()
    
    tasks = []
    for name in dir(tasks_module):
        if not name.startswith('_'):
            obj = getattr(tasks_module, name)
            if callable(obj):
                doc = obj.__doc__ or "No description"
                tasks.append((name, doc.strip().split('\n')[0]))
    
    if not tasks:
        print("  (no tasks defined)")
        return
    
    # Calculate padding for alignment
    max_name_len = max(len(name) for name, _ in tasks)
    
    for name, doc in sorted(tasks):
        print(f"  {name:<{max_name_len}}  {doc}")
    
    print()
    print("Usage: python3 run.py <task> [task2] [task3] ...")


def run_task(task_name, tasks_module=None):
    """
    Run a single task.
    
    Args:
        task_name: Name of the task (can include :arg for arguments)
        tasks_module: The loaded tasks module (will load if None)
    
    Returns:
        int: Return code (0 for success)
    """
    # Load tasks if not provided
    if tasks_module is None:
        tasks_module = load_tasks()
        if tasks_module is None:
            print("Error: tasks.py not found", file=sys.stderr)
            return 1
    
    # Parse task name and argument
    if ':' in task_name:
        name, arg = task_name.split(':', 1)
    else:
        name, arg = task_name, None
    
    # Get task function
    if not hasattr(tasks_module, name):
        print(f"Error: Task '{name}' not found", file=sys.stderr)
        return 1
    
    task_func = getattr(tasks_module, name)
    if not callable(task_func):
        print(f"Error: '{name}' is not a task", file=sys.stderr)
        return 1
    
    # Run task
    try:
        print(f"→ Running task: {task_name}")
        if arg:
            result = task_func(arg)
        else:
            result = task_func()
        
        # Handle return code
        if result is None:
            result = 0
        
        if result == 0:
            print(f"✓ Task '{name}' completed successfully")
        else:
            print(f"✗ Task '{name}' failed with code {result}", file=sys.stderr)
        
        return result
    
    except Exception as e:
        print(f"✗ Task '{name}' failed: {e}", file=sys.stderr)
        return 1


def main():
    """Main entry point."""
    # Load tasks
    tasks_module = load_tasks()
    
    if tasks_module is None:
        print("Error: tasks.py not found in current directory", file=sys.stderr)
        print()
        print("Create a tasks.py file with task definitions:")
        print()
        print('def build():')
        print('    """Build the project"""')
        print('    print("Building...")')
        print('    return 0')
        return 1
    
    # No arguments - list tasks
    if len(sys.argv) < 2:
        list_tasks(tasks_module)
        return 0
    
    # Run tasks in sequence
    for task_name in sys.argv[1:]:
        result = run_task(task_name, tasks_module)
        if result != 0:
            # Stop on first failure
            return result
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
