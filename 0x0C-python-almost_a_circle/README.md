# Almost a Circle Project

## Description

This project implements a system with classes for handling geometric shapes like Rectangle and Square. It includes features such as creating instances, serialization to JSON and CSV, drawing shapes using Turtle graphics, and more.

## Folder Structure

project-root/
│
├── models/
│ ├── init.py
│ ├── base.py
│ ├── rectangle.py
│ └── square.py
│
├── tests/
│ ├── init.py
│ ├── test_models/
│ │ ├── init.py
│ │ ├── test_base.py
│ │ ├── test_rectangle.py
│ │ └── test_square.py
│ └── ...
│
├── README.md
└── ...


## Requirements

- Python 3.8.5
- pycodestyle 2.8.*
- Ubuntu 20.04 LTS

## How to Run Tests

```bash
$ python3 -m unittest discover tests

Class Descriptions
Base

    Manages the ID attribute for all classes.
    Provides methods for JSON and CSV serialization.
    Supports creating instances from dictionaries.

Rectangle

    Inherits from Base.
    Represents a rectangle with width, height, x, y attributes.
    Implements validation, area calculation, display, and more.

Square

    Inherits from Rectangle.
    Represents a square with a size attribute.
    Inherits all attributes and methods from Rectangle.

Tasks Completed
Task 1: Base class

    Implemented the first class Base.
    Created a folder named models with an empty file __init__.py to make it a Python package.
    Added a private class attribute __nb_objects.
    Created a constructor with logic for managing the id attribute.

Task 2: First Rectangle

    Implemented the class Rectangle that inherits from Base.
    Added private instance attributes __width, __height, __x, and __y.
    Created a constructor that initializes the attributes.
    Implemented private attributes with getters and setters.

Task 3: Validate attributes

    Added validation to setter methods and instantiation in Rectangle class.
    Raised TypeError and ValueError for invalid inputs.

Task 4: Area first

    Added a public method area to calculate the area of the Rectangle instance.

Task 5: Display #0

    Added a public method display to print the Rectangle instance with the character #.

Task 6: str

    Overrode the __str__ method in the Rectangle class.

Task 7: Display #1

    Improved the display method to take care of x and y in the Rectangle class.

Task 8: Update #0

    Added a public method update that assigns arguments to each attribute in the Rectangle class.

Task 9: Update #1

    Updated the update method to accept keyword arguments in the Rectangle class.

Task 10: And now, the Square!

    Implemented the class Square that inherits from Rectangle.
    Created a constructor that initializes attributes using the logic of Rectangle.

Task 11: Square size

    Added public getter and setter methods for size in the Square class.

Task 12: Square update

    Added a public method update that assigns attributes to the Square instance.

Task 13: Rectangle instance to dictionary representation

    Added a public method to_dictionary in the Rectangle class.

Task 14: Square instance to dictionary representation

    Added a public method to_dictionary in the Square class.

Task 15: Dictionary to JSON string

    Updated the Base class with a static method to_json_string for JSON string representation.

Task 16: JSON string to file

    Updated the Base class with a class method save_to_file that writes the JSON string representation to a file.

Task 17: JSON string to dictionary

    Updated the Base class with a static method from_json_string that returns a list of instances from a JSON string.

Task 18: Dictionary to Instance

    Updated the Base class with a class method create that returns an instance with all attributes already set.

Task 19: File to instances

    Updated the Base class with a class method load_from_file that returns a list of instances from a file.

Task 20: JSON ok, but CSV?

    Added class methods save_to_file_csv and load_from_file_csv in the Base class for CSV serialization/deserialization.

Task 21: Let's draw it

    Added a static method draw in the Base class that opens a window and draws all the Rectangles and Squares using Turtle graphics.

How to Use

    Import the classes:

python

from models.rectangle import Rectangle
from models.square import Square

    Create instances and perform operations:

python

# Example for Rectangle
r = Rectangle(2, 3)
print(r.area())  # Output: 6
r.display()      # Output: ##
                 #         ##

# Example for Square
s = Square(4)
print(s.area())  # Output: 16
s.display()      # Output: ####
                 #         ####
                 #         ####
                 #         ####

    Serialization and Deserialization:

python

# Example for saving to JSON file
Rectangle.save_to_file([r])
# Example for loading from JSON file
instances = Rectangle.load_from_file()

# Example for saving to CSV file
Rectangle.save_to_file_csv([r])
# Example for loading from CSV file
instances_csv = Rectangle.load_from_file_csv()

    Drawing Shapes:

python

# Example for drawing shapes using Turtle graphics
Base.draw([r], [s])

Contributing

Feel free to contribute by creating issues or pull requests.


