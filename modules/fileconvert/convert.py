#!/usr/bin/env python3
"""
QSOL File Converter - JSON ⟷ CSV
Zero-dependency format converter.
"""

import csv
import json
import sys
from pathlib import Path


def flatten_dict(d, parent_key='', sep='_'):
    """Flatten nested dictionary one level deep."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def json_to_csv(json_data, csv_file, delimiter=',', fields=None):
    """
    Convert JSON array to CSV.
    
    Args:
        json_data: List of dictionaries
        csv_file: Output file object
        delimiter: CSV delimiter
        fields: List of fields to include (None = all)
    """
    if not json_data:
        return
    
    # Flatten dictionaries
    flat_data = [flatten_dict(item) for item in json_data]
    
    # Determine fields
    if fields is None:
        fields = sorted(set().union(*(d.keys() for d in flat_data)))
    
    # Write CSV
    writer = csv.DictWriter(csv_file, fieldnames=fields, 
                           delimiter=delimiter, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(flat_data)


def csv_to_json(csv_file, json_file, delimiter=',', pretty=False):
    """
    Convert CSV to JSON array.
    
    Args:
        csv_file: Input file object
        json_file: Output file object
        delimiter: CSV delimiter
        pretty: Pretty-print JSON
    """
    reader = csv.DictReader(csv_file, delimiter=delimiter)
    data = list(reader)
    
    # Write JSON
    indent = 2 if pretty else None
    json.dump(data, json_file, indent=indent)
    if pretty:
        json_file.write('\n')


def detect_format(filename):
    """Detect format from file extension."""
    ext = Path(filename).suffix.lower()
    if ext == '.json':
        return 'json'
    elif ext in ['.csv', '.tsv']:
        return 'csv'
    return None


def main():
    """Parse arguments and convert."""
    import argparse
    
    # Print QSOL banner
    print("QSOL v0.0.2 — Zero Bloat Equilibrium Maintained.", file=sys.stderr)
    
    parser = argparse.ArgumentParser(
        description='QSOL File Converter - JSON ⟷ CSV with zero dependencies',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s data.json output.csv              # JSON to CSV
  %(prog)s data.csv output.json              # CSV to JSON
  %(prog)s data.tsv out.json --delimiter \\t  # TSV to JSON
  %(prog)s --from json --to csv < in > out   # Pipe mode
  %(prog)s data.json out.csv --fields id,name # Select fields
        '''
    )
    
    parser.add_argument(
        'input',
        nargs='?',
        help='Input file (or stdin if omitted)'
    )
    
    parser.add_argument(
        'output',
        nargs='?',
        help='Output file (or stdout if omitted)'
    )
    
    parser.add_argument(
        '--from',
        dest='from_format',
        choices=['json', 'csv'],
        help='Input format (auto-detected if not specified)'
    )
    
    parser.add_argument(
        '--to',
        dest='to_format',
        choices=['json', 'csv'],
        help='Output format (auto-detected if not specified)'
    )
    
    parser.add_argument(
        '--delimiter', '-d',
        default=',',
        help='CSV delimiter (default: comma)'
    )
    
    parser.add_argument(
        '--fields', '-f',
        help='Comma-separated list of fields for CSV output'
    )
    
    parser.add_argument(
        '--pretty', '-p',
        action='store_true',
        help='Pretty-print JSON output'
    )
    
    args = parser.parse_args()
    
    # Handle delimiter escapes
    args.delimiter = args.delimiter.replace('\\t', '\t').replace('\\n', '\n')
    
    # Parse fields
    fields = args.fields.split(',') if args.fields else None
    
    # Determine input/output
    input_file = open(args.input, 'r') if args.input else sys.stdin
    output_file = open(args.output, 'w') if args.output else sys.stdout
    
    try:
        # Detect formats
        from_format = args.from_format
        to_format = args.to_format
        
        if not from_format and args.input:
            from_format = detect_format(args.input)
        if not to_format and args.output:
            to_format = detect_format(args.output)
        
        # Validate formats
        if not from_format or not to_format:
            print("Error: Cannot detect format. Use --from and --to", file=sys.stderr)
            return 1
        
        if from_format == to_format:
            print(f"Error: Input and output formats are both {from_format}", file=sys.stderr)
            return 1
        
        # Convert
        try:
            if from_format == 'json' and to_format == 'csv':
                data = json.load(input_file)
                if not isinstance(data, list):
                    print("Error: JSON must be an array", file=sys.stderr)
                    return 1
                json_to_csv(data, output_file, args.delimiter, fields)
            
            elif from_format == 'csv' and to_format == 'json':
                csv_to_json(input_file, output_file, args.delimiter, args.pretty)
            
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON - {e}", file=sys.stderr)
            return 1
        except csv.Error as e:
            print(f"Error: Invalid CSV - {e}", file=sys.stderr)
            return 1
        
    finally:
        if args.input:
            input_file.close()
        if args.output:
            output_file.close()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
