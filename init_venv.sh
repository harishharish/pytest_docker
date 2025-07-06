#!/bin/bash

# Exit if any command fails
set -e

# Step 1: Create Python 3.7 virtual environment in .venv
echo "Creating virtual environment with Python 3.7..."
python -m venv .venv

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Step 3: Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Step 4: Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "No requirements.txt found. Skipping dependency installation."
fi

# Step 5: Install current project in editable mode
echo "Installing current project in editable mode..."
pip install -e .

echo "✅ Setup complete. Environment is ready."
