#!/bin/bash

echo "Starting Motor Insurance Analytics Dashboard..."
echo ""

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Run Streamlit
streamlit run Home.py
