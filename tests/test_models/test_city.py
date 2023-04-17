#!/usr/bin/python3
""" Unittest for City class """
import unittest
import re
from time import sleep
from models import storage
from models.city import City


class City_Test(unittest.TestCase):
    """Tests for City class."""
    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        c = City()
        self.assertEqual(c.__class__.__name__, "City")

    def test_01_no_args(self):
        """Test for no arguments passed into City"""
        c = City()
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))
        self.assertTrue(hasattr(c, "name"))
        self.assertTrue(hasattr(c, "state_id"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        c = City()
        self.assertEqual(type(c.id), str)
        self.assertEqual(type(c.name), str)
        self.assertEqual(type(c.state_id), str)
        self.assertEqual(c.created_at.__class__.__name__, "datetime")
        self.assertEqual(c.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        c = City()
        c.string = "Tu"
        c.number = 1106
        c.list = [1, 2, 3]
        c.dict = {"a": 1}
        self.assertTrue(hasattr(c, "string"))
        self.assertTrue(hasattr(c, "number"))
        self.assertTrue(hasattr(c, "list"))
        self.assertTrue(hasattr(c, "dict"))
        self.assertEqual(type(c.string), str)
        self.assertEqual(type(c.number), int)
        self.assertEqual(type(c.list), list)
        self.assertEqual(type(c.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        c = City()
        p = r'(^\[City]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(c))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        c = City()
        first_time = c.updated_at
        sleep(.5)
        c.save()
        second_time = c.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        c = City()
        c.name = "Tu"
        c.number = 1987
        d = c.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        c = City()
        c.name = "Tu"
        c.number = 1987
        d = c.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        c = City()
        c.name = "Tim"
        c.number = 1993
        d = c.to_dict()
        new_c = City(**d)
        self.assertEqual(c.id, new_c.id)
        self.assertEqual(c.created_at, new_c.created_at)
        self.assertEqual(c.updated_at, new_c.updated_at)
        self.assertEqual(c.name, new_c.name)
        self.assertEqual(c.number, new_c.number)
        self.assertEqual(type(new_c.id), str)
        self.assertEqual(new_c.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
