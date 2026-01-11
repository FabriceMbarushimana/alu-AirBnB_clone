#!/usr/bin/python3
"""test for the FileStorage class"""

import unittest
import json
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        obj = BaseModel()
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objects)

    def test_save_and_reload(self):
        obj = User()
        self.storage.new(obj)
        self.storage.save()

        self.storage._FileStorage__objects = {}

        self.storage.reload()

        all_objects = self.storage.all()

        self.assertIn("User.{}".format(obj.id), all_objects)


if __name__ == '__main__':
    unittest.main()
