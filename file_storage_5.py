#!/usr/bin/python3
"""Test FileStorage reload functionality"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

try:
    # Test reload functionality
    storage = FileStorage()
    
    # Create a test object and save it
    obj = BaseModel()
    storage.new(obj)
    storage.save()
    
    # Create new storage and test reload
    new_storage = FileStorage()
    # Clear objects to test reload properly
    new_storage._FileStorage__objects = {}
    
    # Reload should restore objects from file
    new_storage.reload()
    
    # Check if object was reloaded
    key = f"BaseModel.{obj.id}"
    if key in new_storage.all():
        print("OK")
    else:
        print("FAIL: Object not reloaded")
        
except Exception as e:
    print(f"FAIL: {str(e)}")
