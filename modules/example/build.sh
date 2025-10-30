#!/bin/bash
# QSOL Example Module - Build Script
# Demonstrates: Build completes in <1 second

echo "Building linecount (C version)..."
if time gcc -O2 -Wall -Wextra -o linecount linecount.c; then
    echo "✓ Build successful!"
    echo "Usage: ./linecount file.txt"
else
    echo "✗ Build failed"
    exit 1
fi
