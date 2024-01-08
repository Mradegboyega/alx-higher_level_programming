#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
    - obj: The object to which the attribute should be added.
    - attribute: The name of the new attribute.
    - value: The value to assign to the new attribute.

    Raises:
    - TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)

