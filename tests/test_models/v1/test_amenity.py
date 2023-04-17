#!/usr/bin/python3
""" Unittest for Amenity class """
import unittest
import re
from time import sleep
from models import storage
from models.amenity import Amenity


class Amenity_Test(unittest.TestCase):
    """Tests for Amenity class."""
    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        a = Amenity()
        self.assertEqual(a.__class__.__name__, "Amenity")

    def test_01_no_args(self):
        """Test for no arguments passed into Amenity"""
        a = Amenity()
        self.assertTrue(hasattr(a, "id"))
        self.assertTrue(hasattr(a, "created_at"))
        self.assertTrue(hasattr(a, "updated_at"))
        self.assertTrue(hasattr(a, "name"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        a = Amenity()
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.name), str)
        self.assertEqual(a.created_at.__class__.__name__, "datetime")
        self.assertEqual(a.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        a = Amenity()
        a.string = "Tu"
        a.number = 1106
        a.list = [1, 2, 3]
        a.dict = {"a": 1}
        self.assertTrue(hasattr(a, "string"))
        self.assertTrue(hasattr(a, "number"))
        self.assertTrue(hasattr(a, "list"))
        self.assertTrue(hasattr(a, "dict"))
        self.assertEqual(type(a.string), str)
        self.assertEqual(type(a.number), int)
        self.assertEqual(type(a.list), list)
        self.assertEqual(type(a.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        a = Amenity()
        p = r'(^\[Amenity]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(a))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        a = Amenity()
        first_time = a.updated_at
        sleep(.5)
        a.save()
        second_time = a.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        a = Amenity()
        a.name = "Tu"
        a.number = 1987
        d = a.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        a = Amenity()
        a.name = "Tu"
        a.number = 1987
        d = a.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        a = Amenity()
        a.name = "Tim"
        a.number = 1993
        d = a.to_dict()
        new_a = Amenity(**d)
        self.assertEqual(a.id, new_a.id)
        self.assertEqual(a.created_at, new_a.created_at)
        self.assertEqual(a.updated_at, new_a.updated_at)
        self.assertEqual(a.name, new_a.name)
        self.assertEqual(a.number, new_a.number)
        self.assertEqual(type(new_a.id), str)
        self.assertEqual(new_a.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
