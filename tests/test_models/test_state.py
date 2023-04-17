#!/usr/bin/python3
""" Unittest for State class """
import unittest
import re
from time import sleep
from models import storage
from models.state import State


class State_Test(unittest.TestCase):
    """Tests for State class."""
    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        s = State()
        self.assertEqual(s.__class__.__name__, "State")

    def test_01_no_args(self):
        """Test for no arguments passed into State"""
        s = State()
        self.assertTrue(hasattr(s, "id"))
        self.assertTrue(hasattr(s, "created_at"))
        self.assertTrue(hasattr(s, "updated_at"))
        self.assertTrue(hasattr(s, "name"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        s = State()
        self.assertEqual(type(s.id), str)
        self.assertEqual(type(s.name), str)
        self.assertEqual(s.created_at.__class__.__name__, "datetime")
        self.assertEqual(s.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        s = State()
        s.string = "Tu"
        s.number = 1106
        s.list = [1, 2, 3]
        s.dict = {"a": 1}
        self.assertTrue(hasattr(s, "string"))
        self.assertTrue(hasattr(s, "number"))
        self.assertTrue(hasattr(s, "list"))
        self.assertTrue(hasattr(s, "dict"))
        self.assertEqual(type(s.string), str)
        self.assertEqual(type(s.number), int)
        self.assertEqual(type(s.list), list)
        self.assertEqual(type(s.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        s = State()
        p = r'(^\[State]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(s))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        s = State()
        first_time = s.updated_at
        sleep(.5)
        s.save()
        second_time = s.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        s = State()
        s.name = "Tu"
        s.number = 1987
        d = s.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        s = State()
        s.name = "Tu"
        s.number = 1987
        d = s.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        s = State()
        s.name = "Tim"
        s.number = 1993
        d = s.to_dict()
        new_s = State(**d)
        self.assertEqual(s.id, new_s.id)
        self.assertEqual(s.created_at, new_s.created_at)
        self.assertEqual(s.updated_at, new_s.updated_at)
        self.assertEqual(s.name, new_s.name)
        self.assertEqual(s.number, new_s.number)
        self.assertEqual(type(new_s.id), str)
        self.assertEqual(new_s.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
