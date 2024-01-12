import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
from io import StringIO

class TestRectangle(unittest.TestCase):
    def test_create_instance(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        r = Rectangle(2, 2)
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            self.assertEqual(buffer.getvalue(), '##\n##\n')

    def test_str(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(str(r), '[Rectangle] (1) 3/4 - 1/2')

    def test_display_with_xy(self):
        r = Rectangle(2, 2, 1, 1)
        with StringIO() as buffer, redirect_stdout(buffer):
            r.display()
            self.assertEqual(buffer.getvalue(), '\n ##\n ##\n')

    def test_update(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4)
        dictionary = r.to_dictionary()
        self.assertEqual(dictionary, {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

if __name__ == '__main__':
    unittest.main()

