# Example Module - Line Counter

> A minimal example demonstrating QSOL principles

## Purpose

Counts lines in text files or stdin. Simple, fast, and transparent.

## Philosophy Demonstration

This module exemplifies QSOL constraints:
- **Size**: ~50 lines of code, zero dependencies
- **Speed**: Builds in <1 second, processes files instantly
- **Transparency**: Clear, readable code using only standard library

## Installation

### Unix/Linux/MacOS (Python version)

```bash
# No installation needed - just run it
python3 linecount.py file.txt
```

### Alternative: C version

```bash
# Compile (takes <1 second)
gcc -O2 -o linecount linecount.c

# Run
./linecount file.txt
```

## Usage

```bash
# Count lines in a file
python3 linecount.py myfile.txt

# Count lines from stdin
cat myfile.txt | python3 linecount.py

# Multiple files
python3 linecount.py file1.txt file2.txt file3.txt
```

## Output

```
file1.txt: 42 lines
file2.txt: 128 lines
file3.txt: 7 lines
Total: 177 lines
```

## Constraints Met

- **Lines of code**: 48 (Python), 65 (C)
- **Dependencies**: 0 external
- **Build time**: <1 second
- **Runtime**: O(n) - linear with file size
- **Memory**: O(1) - constant memory usage

## Why This Example?

This demonstrates that useful tools don't need:
- Complex frameworks
- Multiple dependencies
- Long build times
- Complicated abstractions

A line counter is simple, but it's **honest simplicity**. The code does exactly what it says, nothing more.

## Learning Points

1. **Standard library is enough** - No external dependencies needed
2. **Simple is sustainable** - Easy to maintain and modify
3. **Fast by default** - No optimization needed for good performance
4. **Obvious code** - Anyone can understand and modify it

---

*This is QSOL: Small, Fast, Clear.*
