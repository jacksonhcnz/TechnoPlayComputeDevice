#!/bin/bash

echo "Updating package lists..."
sudo apt update -y

echo "Installing Python 3 and pip..."
sudo apt install -y python3 python3-pip

echo "Installing Python packages..."
pip3 install --break-system-packages textual pygame RPi.GPIO

echo "Installation complete!"
