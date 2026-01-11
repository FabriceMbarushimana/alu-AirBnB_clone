#!/usr/bin/python3
"""test file for place class"""

import unittest
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """creating a testcase class that inherits from unittest.TestCase"""
    def setUp(self):
        """setting up the object for testing"""
        self.place_model = Place()

    def test_instance(self):
        self.assertIsInstance(self.place_model, Place)

    def test_city_id(self):
        self.assertIsInstance(self.place_model.city_id, str)
        self.assertEqual(self.place_model.city_id, "")
        self.place_model.city_id = "city_123"
        self.assertEqual(self.place_model.city_id, "city_123")

    def test_user_id(self):
        self.assertIsInstance(self.place_model.user_id, str)
        self.assertEqual(self.place_model.user_id, "")
        self.place_model.user_id = "user_123"
        self.assertEqual(self.place_model.user_id, "user_123")

    def test_name(self):
        self.assertIsInstance(self.place_model.name, str)
        self.assertEqual(self.place_model.name, "")
        self.place_model.name = "Beautiful Place"
        self.assertEqual(self.place_model.name, "Beautiful Place")

    def test_description(self):
        self.assertIsInstance(self.place_model.description, str)
        self.assertEqual(self.place_model.description, "")
        self.place_model.description = "A wonderful place to stay"
        self.assertEqual(self.place_model.description, "A wonderful place to stay")

    def test_number_rooms(self):
        self.assertIsInstance(self.place_model.number_rooms, int)
        self.assertEqual(self.place_model.number_rooms, 0)
        self.place_model.number_rooms = 3
        self.assertEqual(self.place_model.number_rooms, 3)

    def test_number_bathrooms(self):
        self.assertIsInstance(self.place_model.number_bathrooms, int)
        self.assertEqual(self.place_model.number_bathrooms, 0)
        self.place_model.number_bathrooms = 2
        self.assertEqual(self.place_model.number_bathrooms, 2)

    def test_max_guest(self):
        self.assertIsInstance(self.place_model.max_guest, int)
        self.assertEqual(self.place_model.max_guest, 0)
        self.place_model.max_guest = 6
        self.assertEqual(self.place_model.max_guest, 6)

    def test_price_by_night(self):
        self.assertIsInstance(self.place_model.price_by_night, int)
        self.assertEqual(self.place_model.price_by_night, 0)
        self.place_model.price_by_night = 100
        self.assertEqual(self.place_model.price_by_night, 100)

    def test_latitude(self):
        self.assertIsInstance(self.place_model.latitude, float)
        self.assertEqual(self.place_model.latitude, 0.0)
        self.place_model.latitude = 37.774
        self.assertEqual(self.place_model.latitude, 37.774)

    def test_longitude(self):
        self.assertIsInstance(self.place_model.longitude, float)
        self.assertEqual(self.place_model.longitude, 0.0)
        self.place_model.longitude = -122.431
        self.assertEqual(self.place_model.longitude, -122.431)

    def test_amenity_ids(self):
        self.assertIsInstance(self.place_model.amenity_ids, list)
        self.assertEqual(self.place_model.amenity_ids, [])
        self.place_model.amenity_ids = ["amenity_1", "amenity_2"]
        self.assertEqual(self.place_model.amenity_ids, ["amenity_1", "amenity_2"])


if __name__ == "__main__":
    unittest.main()
