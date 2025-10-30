#!/usr/bin/env python3
"""
QSOL Example Module: Line Counter
A minimal, fast, and transparent line counting utility.
"""

import sys


def count_lines(filename):
    """Count lines in a file. Returns (line_count, error_message)."""
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f), None
    except FileNotFoundError:
        return 0, f"Error: File '{filename}' not found"
    except PermissionError:
        return 0, f"Error: Permission denied for '{filename}'"
    except Exception as e:
        return 0, f"Error reading '{filename}': {e}"


def count_stdin():
    """Count lines from stdin."""
    return sum(1 for _ in sys.stdin)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        # Read from stdin
        count = count_stdin()
        print(f"{count} lines")
        return 0
    
    # Read from files
    total = 0
    errors = []
    
    for filename in sys.argv[1:]:
        count, error = count_lines(filename)
        if error:
            errors.append(error)
        else:
            print(f"{filename}: {count} lines")
            total += count
    
    # Show total if multiple files
    if len(sys.argv) > 2:
        print(f"Total: {total} lines")
    
    # Print errors at the end
    for error in errors:
        print(error, file=sys.stderr)
    
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
