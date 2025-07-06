#!/bin/bash
# DuskCipher Pro - Advanced Test Script
# This script demonstrates various features for encryption testing

echo "=== DuskCipher Pro Test Script ==="
echo "Testing encryption capabilities..."

# System information
echo "System: $(uname -s) $(uname -r)"
echo "User: $(whoami)"
echo "Date: $(date)"

# Sample operations
for i in {1..5}; do
    echo "Processing step $i..."
    sleep 0.5
done

# File operations
echo "Current directory: $(pwd)"
echo "Files in directory:"
ls -la

# Network test
echo "Network interfaces:"
ip addr show 2>/dev/null || ifconfig 2>/dev/null || echo "Network info unavailable"

# Completion
echo "Test completed successfully!"
echo "This script is ready for encryption testing."
