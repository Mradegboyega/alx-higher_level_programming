# TDD Project

This project focuses on implementing solutions to programming tasks using the Test-Driven Development (TDD) approach. TDD is a software development methodology where tests are written before the actual code. This process helps ensure code correctness, maintainability, and reliability.

## Tasks

### 0. Integers Addition

Implement a function that adds two integers and write corresponding tests. The function must handle edge cases and raise exceptions for invalid input.

- File: `0-add_integer.py`
- Tests: `tests/0-add_integer.txt`

### 1. Divide a Matrix

Write a function that divides all elements of a matrix. Ensure that the function handles various scenarios and exceptions.

- File: `2-matrix_divided.py`
- Tests: `tests/2-matrix_divided.txt`

### 2. Say My Name

Implement a function that prints "My name is <first name> <last name>" and write tests to verify its behavior. Handle exceptions for invalid input.

- File: `3-say_my_name.py`
- Tests: `tests/3-say_my_name.txt`

### 3. Print Square

Create a function that prints a square with the character `#`. Ensure that the function handles different cases and raises exceptions for invalid input.

- File: `4-print_square.py`
- Tests: `tests/4-print_square.txt`

## How to Run Tests

To run the tests for each task, use the following command:

```bash
python3 -m doctest -v ./tests/<test_file>.txt | tail -2


Task 4: Text indentation

The task requires implementing a Python script that defines a function called text_indentation. This function takes a text string as input and prints the text with two new lines after each occurrence of '.', '?', and ':'. The script must adhere to specific requirements regarding spacing and not importing any modules.
Task 5: Max integer - Unittest

This task involves creating a Python script that defines a function named max_integer. The function finds and returns the maximum integer in a list of integers. If the list is empty, the function returns None. The script should also include unittests to ensure the correctness of the function for various cases.
Task 6: Matrix multiplication

In this task, you need to implement a Python script with a function called matrix_mul that multiplies two matrices. The script should include validation checks for the input matrices, raising appropriate exceptions for invalid inputs. The validation checks include ensuring that the matrices are lists of lists, are not empty, have consistent row sizes, and can be multiplied.
Task 7: Lazy matrix multiplication

The goal is to write a Python script that defines a function named lazy_matrix_mul. This function multiplies two matrices using the NumPy module. Similar to the previous task, the script must include validation checks for the input matrices and raise exceptions for invalid inputs. The validation includes ensuring that the matrices are lists of lists, are not empty, have consistent row sizes, and can be multiplied.
Task 8: Printing Python Strings

This C program aims to print information about Python string objects. It includes a function called print_python_string that takes a PyObject* as input and prints information about the string, such as its type, length, and value. The provided test script demonstrates the usage of this function with various string objects, both valid and invalid. The task involves interacting with the Python/C API and handling different types of string objects.

Conclusion

This project provides hands-on experience with Test-Driven Development (TDD), ensuring that code is robust, reliable, and well-tested. Follow the instructions in each task to implement the required functionality and run the corresponding tests.
