#!/bin/bash

# Create a Python virtual environment named "django_venv"
python3 -m venv Django

# Activate the virtual environment
source Django/bin/activate

# Check if the virtual environment is active
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo "The virtual environment is not active."
    exit 1
else
    echo "The virtual environment is active."
fi

# Install Python packages listed in requirements.txt
pip3 install -r requirements.txt