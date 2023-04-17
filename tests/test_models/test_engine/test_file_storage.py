#!/usr/bin/python3
""" Unittest for FileStorage class """
import unittest
import os
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class FileStorage_Test(unittest.TestCase):
    """Tests for File Storge class."""

    def setUp(self):
        """Set up tests."""
        pass

    def tearDown(self):
        """Tear down tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_00_private_attrs(self):
        """Test to validate attributes are private."""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            print(fs.objects)
        with self.assertRaises(AttributeError):
            print(fs.file_path)

    def test_00a_id_attrs(self):
        """Test to validate attributes are private."""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertEqual(type(b.id), str)

    def test_01_all_return_type(self):
        """Test to validate all() returns an object."""
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_01a_all_return_type(self):
        """Test to validate all() returns an empty dict"""
        fs = FileStorage()
        fs.reset()
        self.assertFalse(fs.all())
        fs.new(BaseModel())
        self.assertTrue(fs.all())

    def test_02_working_save(self):
        """Test to validate save works."""
        fs = FileStorage()
        fs.reset()
        fs.new(BaseModel())
        fs.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_03_working_reload(self):
        """Test to validate reload works."""
        b = BaseModel()
        key = "BaseModel" + "." + b.id
        b.save()
        b1 = BaseModel()
        key1 = "BaseModel" + "." + b1.id
        b1.save()
        self.assertTrue(storage.all()[key] is not None)
        self.assertTrue(storage.all()[key1] is not None)
        with self.assertRaises(KeyError):
            storage.all()[12345]

    def test_03a_working_reload(self):
        """Checks reload functionality if file_path doesn't exist"""
        fs = FileStorage()
        b = BaseModel()
        key = "BaseModel" + '.' + b.id
        fs.new(b)
        fs.save()
        fs.reset()
        fs.reload()
        self.assertTrue(fs.all()[key])

    def test_04_working_new(self):
        """Test to validate if new works."""
        fs = FileStorage()
        fs.new(BaseModel())
        self.assertTrue(fs.all())

    def test_05_new_int(self):
        """Passes int to new"""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(1)

    def test_06_new_float(self):
        """Passes foat to new"""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(1.1)

    def test_07_new_unknown(self):
        """Passes unknown to new"""
        fs = FileStorage()
        with self.assertRaises(NameError):
            fs.new(b)

    def test_08_new_inf(self):
        """Passes inf to new"""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(float("inf"))

    def test_09_new_nan(self):
        """Passes nan to new"""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new(float("nan"))

    def test_10_new_string(self):
        """Passes string to new"""
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.new("string")


if __name__ == '__main__':
    unittest.main()
