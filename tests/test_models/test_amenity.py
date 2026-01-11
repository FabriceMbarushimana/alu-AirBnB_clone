#!/usr/bin/python3
"""test file for amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """creating a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for testing"""
        self.amenity_model = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.amenity_model, Amenity)

    def test_name(self):
        self.assertIsInstance(self.amenity_model.name, str)
        self.assertEqual(self.amenity_model.name, "")
        self.amenity_model.name = "WiFi"
        self.assertEqual(self.amenity_model.name, "WiFi")


if __name__ == "__main__":
    unittest.main()
