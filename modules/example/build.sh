#!/bin/bash
# QSOL Example Module - Build Script
# Demonstrates: Build completes in <1 second

echo "Building linecount (C version)..."
time gcc -O2 -Wall -Wextra -o linecount linecount.c

if [ $? -eq 0 ]; then
    echo "✓ Build successful!"
    echo "Usage: ./linecount file.txt"
else
    echo "✗ Build failed"
    exit 1
fi
