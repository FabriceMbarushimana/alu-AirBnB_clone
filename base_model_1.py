#!/usr/bin/python3
"""Test BaseModel save functionality"""

from models.base_model import BaseModel
import os

try:
    # Remove any existing file to test fresh
    if os.path.exists("file.json"):
        os.remove("file.json")
    
    # Test save functionality
    obj = BaseModel()
    obj.name = "test"
    obj.save()
    
    # Check if file was created
    if os.path.exists("file.json"):
        print("OK")
    else:
        print("FAIL: file.json not created")
        
except Exception as e:
    print(f"FAIL: {str(e)}")
