#!/usr/bin/python3
""" Unittest for Review class. """
import unittest
import re
from time import sleep
from models import storage
from models.review import Review


class Review_Test(unittest.TestCase):
    """Tests for Review class."""
    def setUp(self):
        """Set up tests."""
        storage.reset()

    def test_00_valid_user(self):
        """Test to validate a user."""
        r = Review()
        self.assertEqual(r.__class__.__name__, "Review")

    def test_01_no_args(self):
        """Test for no arguments passed into Review"""
        r = Review()
        self.assertTrue(hasattr(r, "id"))
        self.assertTrue(hasattr(r, "created_at"))
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        r = Review()
        self.assertEqual(type(r.id), str)
        self.assertEqual(type(r.place_id), str)
        self.assertEqual(type(r.user_id), str)
        self.assertEqual(type(r.text), str)
        self.assertEqual(r.created_at.__class__.__name__, "datetime")
        self.assertEqual(r.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        r = Review()
        r.string = "Tu"
        r.number = 1106
        r.list = [1, 2, 3]
        r.dict = {"a": 1}
        self.assertTrue(hasattr(r, "string"))
        self.assertTrue(hasattr(r, "number"))
        self.assertTrue(hasattr(r, "list"))
        self.assertTrue(hasattr(r, "dict"))
        self.assertEqual(type(r.string), str)
        self.assertEqual(type(r.number), int)
        self.assertEqual(type(r.list), list)
        self.assertEqual(type(r.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        r = Review()
        p = r'(^\[Review]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(r))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        r = Review()
        first_time = r.updated_at
        sleep(.5)
        r.save()
        second_time = r.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        r = Review()
        r.name = "Tu"
        r.number = 1987
        d = r.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        r = Review()
        r.name = "Tu"
        r.number = 1987
        d = r.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        r = Review()
        r.name = "Tim"
        r.number = 1993
        d = r.to_dict()
        new_r = Review(**d)
        self.assertEqual(r.id, new_r.id)
        self.assertEqual(r.created_at, new_r.created_at)
        self.assertEqual(r.updated_at, new_r.updated_at)
        self.assertEqual(r.name, new_r.name)
        self.assertEqual(r.number, new_r.number)
        self.assertEqual(type(new_r.id), str)
        self.assertEqual(new_r.created_at.__class__.__name__, "datetime")


if __name__ == '__main__':
    unittest.main()
