import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
from io import StringIO

class TestBase(unittest.TestCase):
    def test_create_instance(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.id, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_to_json_string(self):
        r = Rectangle(1, 2, 3, 4)
        dictionary = r.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(json_string, '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_save_to_file(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}]')

    def test_load_from_file(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file([r])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 1)
        self.assertEqual(instances[0].height, 2)
        self.assertEqual(instances[0].x, 3)
        self.assertEqual(instances[0].y, 4)

    def test_save_to_file_csv(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, 'id,width,height,x,y\n1,1,2,3,4\n')

    def test_load_from_file_csv(self):
        r = Rectangle(1, 2, 3, 4)
        Rectangle.save_to_file_csv([r])
        instances = Rectangle.load_from_file_csv()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 1)
        self.assertEqual(instances[0].height, 2)
        self.assertEqual(instances[0].x, 3)
        self.assertEqual(instances[0].y, 4)

    def test_create_instance_csv(self):
        r = Rectangle(1, 2, 3, 4)
        Square.save_to_file_csv([r])
        instances = Square.load_from_file_csv()
        self.assertEqual(len(instances), 1)
        self.assertIsInstance(instances[0], Square)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].size, 1)
        self.assertEqual(instances[0].x, 3)
        self.assertEqual(instances[0].y, 4)

    def test_draw(self):
        r = Rectangle(1, 2, 3, 4)
        s = Square(5, 6, 7, 8)
        Base.draw([r], [s])

        # Add assertions based on the expected behavior of the drawing

if __name__ == '__main__':
    unittest.main()

