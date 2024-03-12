# JavaScript Coding Tasks

This repository contains solutions for various JavaScript coding tasks.

## Task 0: Rectangle #0

Defines an empty class `Rectangle` using the class notation.

## Task 1: Rectangle #1

Defines a class `Rectangle` that represents a rectangle. The constructor takes two arguments, width and height, and initializes instance attributes accordingly.

## Task 2: Rectangle #2

Enhances the `Rectangle` class from Task 1 by adding a check to create an empty object if width or height is equal to 0 or not a positive integer.

## Task 3: Rectangle #3

Extends the `Rectangle` class from Task 2 by adding an instance method `print()` that prints the rectangle using the character 'X'.

## Task 4: Rectangle #4

Enhances the `Rectangle` class from Task 3 by adding instance methods `rotate()` that exchanges the width and height of the rectangle and `double()` that multiplies the width and height of the rectangle by 2.

## Task 5: Square #0

Defines a class `Square` that inherits from `Rectangle` of Task 4. The constructor takes one argument, size, and calls the constructor of `Rectangle` using `super(size)`.

## Task 6: Square #1

Defines a class `Square` that inherits from `Square` of Task 5. Adds an instance method `charPrint(c)` that prints the square using the character `c`. If `c` is undefined, it defaults to 'X'.

## Task 7: Occurrences

Write a function that returns the number of occurrences in a list.

## Task 8: Esrever

Write a function that returns the reversed version of a list without using the built-in `reverse` method.

## Task 9: Log me

Write a function that prints the number of arguments already printed and the new argument value.

## Task 10: Number conversion

Write a function that converts a number from base 10 to another base passed as an argument without using any new variables.

## Task 11: Factor index (Advanced)

Write a script that imports an array and computes a new array. The script imports a list from the file `100-data.js` and uses the `map` function.

## Task 12: Sorted occurrences (Advanced)

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. The script imports a dictionary from the file `101-data.js` and uses the `reduce` function.

## Task 13: Concat files (Advanced)

Write a script that concatenates two files. The script takes three command line arguments: the file path of the first source file, the file path of the second source file, and the file path of the destination. The content of the source files is concatenated and written to the destination file.

Feel free to refer to individual task sections for more details on each task.

