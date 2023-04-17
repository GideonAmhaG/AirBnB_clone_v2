#!/usr/bin/python3
""" Unittest for Place class """
import unittest
import re
from time import sleep
from models import storage
from models.place import Place


class Place_Test(unittest.TestCase):
    """Tests for Place class."""
    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        p = Place()
        self.assertEqual(p.__class__.__name__, "Place")

    def test_01_no_args(self):
        """Test for no arguments passed into Place"""
        p = Place()
        self.assertTrue(hasattr(p, "id"))
        self.assertTrue(hasattr(p, "created_at"))
        self.assertTrue(hasattr(p, "updated_at"))
        self.assertTrue(hasattr(p, "name"))
        self.assertTrue(hasattr(p, "city_id"))
        self.assertTrue(hasattr(p, "user_id"))
        self.assertTrue(hasattr(p, "description"))
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "latitude"))
        self.assertTrue(hasattr(p, "longitude"))
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertTrue(hasattr(p, "amenity_ids"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        p = Place()
        self.assertEqual(type(p.id), str)
        self.assertEqual(type(p.name), str)
        self.assertEqual(type(p.city_id), str)
        self.assertEqual(type(p.user_id), str)
        self.assertEqual(type(p.description), str)
        self.assertEqual(type(p.number_rooms), int)
        self.assertEqual(type(p.number_bathrooms), int)
        self.assertEqual(type(p.max_guest), int)
        self.assertEqual(type(p.price_by_night), int)
        self.assertEqual(type(p.latitude), float)
        self.assertEqual(type(p.longitude), float)
        self.assertEqual(type(p.amenity_ids), list)
        self.assertEqual(p.created_at.__class__.__name__, "datetime")
        self.assertEqual(p.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        p = Place()
        p.string = "Tu"
        p.number = 1106
        p.list = [1, 2, 3]
        p.dict = {"a": 1}
        self.assertTrue(hasattr(p, "string"))
        self.assertTrue(hasattr(p, "number"))
        self.assertTrue(hasattr(p, "list"))
        self.assertTrue(hasattr(p, "dict"))
        self.assertEqual(type(p.string), str)
        self.assertEqual(type(p.number), int)
        self.assertEqual(type(p.list), list)
        self.assertEqual(type(p.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        p = Place()
        regex = r'(^\[Place]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(regex)
        match = prog.match(str(p))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        p = Place()
        first_time = p.updated_at
        sleep(.5)
        p.save()
        second_time = p.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        p = Place()
        p.name = "Tu"
        p.number = 1987
        d = p.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        p = Place()
        p.name = "Tu"
        p.number = 1987
        d = p.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        p = Place()
        p.name = "Tim"
        p.number = 1993
        d = p.to_dict()
        new_p = Place(**d)
        self.assertEqual(p.id, new_p.id)
        self.assertEqual(p.created_at, new_p.created_at)
        self.assertEqual(p.updated_at, new_p.updated_at)
        self.assertEqual(p.name, new_p.name)
        self.assertEqual(p.number, new_p.number)
        self.assertEqual(type(new_p.id), str)
        self.assertEqual(new_p.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
