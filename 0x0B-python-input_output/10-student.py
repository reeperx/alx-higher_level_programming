#!/usr/bin/python3
"""
Contains the clas "Student"
"""

class Student:
    """
    Defines a Student by first name, last name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student with the given first name, last name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}
