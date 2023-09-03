#!/bin/bash
echo "Installing dependencies..."
pip install -r dependencies.txt
# Check if previous command succeeded
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi
echo "Done building!"