#!/bin/bash

echo "========================================"
echo "Motor Insurance Dashboard Setup"
echo "========================================"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Generate data
echo "Generating synthetic data..."
python utils/data_generator.py

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To run the dashboard:"
echo "  1. Activate the environment: source venv/bin/activate"
echo "  2. Run the dashboard: streamlit run Home.py"
echo ""
