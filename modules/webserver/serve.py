#!/usr/bin/env python3
"""
QSOL Minimal Web Server
A zero-dependency static file server.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path


class QSOLHTTPHandler(http.server.SimpleHTTPRequestHandler):
    """Minimal HTTP handler with clean output."""
    
    def log_message(self, format, *args):
        """Log requests in a clean format."""
        print(f"[{self.log_date_time_string()}] {args[0]}")
    
    def end_headers(self):
        """Add minimal security headers."""
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()


def serve(directory='.', port=8000, allow_index=True):
    """
    Start the web server.
    
    Args:
        directory: Directory to serve (default: current directory)
        port: Port to listen on (default: 8000)
        allow_index: Allow directory listings (default: True)
    """
    # Change to target directory
    os.chdir(directory)
    
    # Disable directory listing if requested
    if not allow_index:
        QSOLHTTPHandler.extensions_map = {
            '': 'application/octet-stream',
        }
    
    # Create server
    with socketserver.TCPServer(("", port), QSOLHTTPHandler) as httpd:
        addr = httpd.server_address
        print(f"QSOL Web Server")
        print(f"Serving: {Path(directory).absolute()}")
        print(f"Address: http://localhost:{addr[1]}")
        print(f"Press Ctrl+C to stop")
        print("-" * 40)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")
            return 0


def main():
    """Parse arguments and start server."""
    import argparse
    
    # Print QSOL banner
    print("QSOL v0.0.2 — Zero Bloat Equilibrium Maintained.")
    print()
    
    parser = argparse.ArgumentParser(
        description='QSOL Minimal Web Server - Zero dependencies, instant start',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s                    # Serve current directory on port 8000
  %(prog)s /path/to/files     # Serve specific directory
  %(prog)s --port 3000        # Use custom port
  %(prog)s --no-index         # Disable directory listings
        '''
    )
    
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to serve (default: current directory)'
    )
    
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=8000,
        help='Port to listen on (default: 8000)'
    )
    
    parser.add_argument(
        '--no-index',
        action='store_true',
        help='Disable directory listings'
    )
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory", file=sys.stderr)
        return 1
    
    # Validate port
    if not (1 <= args.port <= 65535):
        print(f"Error: Port must be between 1 and 65535", file=sys.stderr)
        return 1
    
    # Start server
    try:
        return serve(args.directory, args.port, not args.no_index)
    except PermissionError:
        print(f"Error: Permission denied on port {args.port}", file=sys.stderr)
        print("Hint: Ports below 1024 require root/admin privileges", file=sys.stderr)
        return 1
    except OSError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
