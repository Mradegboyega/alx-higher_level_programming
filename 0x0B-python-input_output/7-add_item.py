#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.

Author: Your Name
"""

import sys
import os

# Add the path to the directory containing your modules to sys.path
module_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(module_path)

from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_and_save_to_json():
    """
    Add all script arguments to a Python list and save them to a file.
    """
    # Load existing data from the file or initialize an empty list
    try:
        existing_data = load_from_json_file("add_item.json")
    except (FileNotFoundError, ValueError):
        existing_data = []

    # Add script arguments to the list
    for arg in sys.argv[1:]:
        existing_data.append(arg)

    # Save the updated list to the file
    save_to_json_file(existing_data, "add_item.json")
