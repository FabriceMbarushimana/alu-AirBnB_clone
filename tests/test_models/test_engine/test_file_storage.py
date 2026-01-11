#!/usr/bin/python3
"""test file for file storage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """creating a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for testing"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()

    def tearDown(self):
        """clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """test instance creation"""
        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        """test the all method"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """test the new method"""
        initial_count = len(self.storage.all())
        new_model = BaseModel()
        self.storage.new(new_model)
        updated_count = len(self.storage.all())
        self.assertEqual(updated_count, initial_count + 1)
        
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], new_model)

    def test_save(self):
        """test the save method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        
        with open("file.json", 'r') as file:
            data = json.load(file)
            key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
            self.assertIn(key, data)

    def test_reload(self):
        """test the reload method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        
        # Create new storage instance and reload
        new_storage = FileStorage()
        new_storage.reload()
        
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)
        self.assertIn(key, new_storage.all())

    def test_reload_with_all_models(self):
        """test reload with different model types"""
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()
        
        models = [user, state, city, amenity, place, review]
        
        for model in models:
            self.storage.new(model)
        
        self.storage.save()
        
        # Create new storage and reload
        new_storage = FileStorage()
        new_storage.reload()
        
        for model in models:
            key = "{}.{}".format(model.__class__.__name__, model.id)
            self.assertIn(key, new_storage.all())

    def test_reload_nonexistent_file(self):
        """test reload when file doesn't exist"""
        # Remove file if it exists
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        
        # Should not raise an exception
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIsInstance(new_storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
