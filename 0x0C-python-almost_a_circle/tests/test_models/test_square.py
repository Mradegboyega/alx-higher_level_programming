import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
from io import StringIO

class TestSquare(unittest.TestCase):
    def test_create_instance(self):
        s = Square(5, 6, 7, 8)
        self.assertEqual(s.id, 8)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_area(self):
        s = Square(3, 4, 5, 6)
        self.assertEqual(s.area(), 9)

    def test_display(self):
        s = Square(2, 2, 0, 1)
        with StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), '\n\n ##\n ##\n')

    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), '[Square] (4) 2/3 - 1')

    def test_display_with_xy(self):
        s = Square(2, 2, 1, 1)
        with StringIO() as buffer, redirect_stdout(buffer):
            s.display()
            self.assertEqual(buffer.getvalue(), '\n ##\n ##\n')

    def test_update(self):
        s = Square(1, 2, 3, 4)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 30)
        self.assertEqual(s.y, 40)

    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        dictionary = s.to_dictionary()
        self.assertEqual(dictionary, {'id': 4, 'size': 1, 'x': 2, 'y': 3})

if __name__ == '__main__':
    unittest.main()

