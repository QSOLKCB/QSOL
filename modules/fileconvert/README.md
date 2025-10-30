# File Converter - JSON ⟷ CSV

> A minimal, zero-dependency data format converter

## Purpose

Convert between JSON and CSV formats with zero dependencies. Fast, reliable, and transparent.

## Philosophy Demonstration

This module exemplifies QSOL constraints:
- **Size**: ~150 lines of code, zero external dependencies
- **Speed**: Converts files instantly, O(n) performance
- **Transparency**: Pure Python standard library, clear logic

## Installation

```bash
# No installation needed - just run it
python3 convert.py input.json output.csv
```

## Usage

### JSON to CSV

```bash
# Convert JSON array to CSV
python3 convert.py data.json output.csv

# With custom delimiter
python3 convert.py data.json output.tsv --delimiter '\t'

# Specify fields order
python3 convert.py data.json output.csv --fields name,email,age
```

### CSV to JSON

```bash
# Convert CSV to JSON array
python3 convert.py data.csv output.json

# With custom delimiter
python3 convert.py data.tsv output.json --delimiter '\t'

# Pretty print JSON
python3 convert.py data.csv output.json --pretty
```

### Pipe Support

```bash
# From stdin to stdout
cat data.json | python3 convert.py --from json --to csv > output.csv

# Chain with other tools
curl api.example.com/data.json | python3 convert.py --from json --to csv | head -n 10
```

## Input Formats

### JSON
```json
[
  {"name": "Alice", "age": 30, "city": "NYC"},
  {"name": "Bob", "age": 25, "city": "LA"}
]
```

### CSV
```csv
name,age,city
Alice,30,NYC
Bob,25,LA
```

## Features

- ✅ JSON to CSV conversion
- ✅ CSV to JSON conversion
- ✅ Custom delimiters (comma, tab, pipe, etc.)
- ✅ Field selection and ordering
- ✅ Stdin/stdout support for piping
- ✅ Pretty-print JSON
- ✅ Handles nested objects (flattens them)
- ❌ No XML support (outside scope)
- ❌ No complex nested arrays (keep it simple)

## Constraints Met

- **Lines of code**: ~150
- **Dependencies**: 0 external (only Python stdlib)
- **Startup time**: <50ms
- **Conversion speed**: >10K rows/second
- **Memory**: O(n) - processes line by line where possible

## Examples

### Convert API response to CSV

```bash
curl https://api.github.com/users | python3 convert.py --from json --to csv > users.csv
```

### Convert CSV to JSON for API

```bash
python3 convert.py users.csv users.json --pretty
```

### Quick data inspection

```bash
python3 convert.py large-data.json preview.csv --fields id,name,status
```

## Why This Template?

Demonstrates:
1. **Data format agility** - Common conversion need
2. **Pipeline friendly** - Works with stdin/stdout
3. **Zero dependencies** - csv and json modules are stdlib
4. **Practical utility** - Solves real problems daily

## Limitations

Intentionally simple:
- Doesn't handle deeply nested JSON (flattens one level)
- CSV must have headers
- UTF-8 encoding only
- No schema validation

These limitations keep the code simple and maintainable. For complex transformations, use specialized tools.

---

*This is QSOL: Small, Fast, Clear.*
