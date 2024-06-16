#!/usr/bin/python3"""Defines class and serializes it"""import pickleclass CustomObject:    """A custom class with attributes and methods for serialization."""    def __init__(self, name, age, is_student):        self.name = name        self.age = age        self.is_student = is_student    def display(self):        """Prints the object's attributes in a formatted way."""        print(f"Name: {self.name}")        print(f"Age: {self.age}")        print(f"Is Student: {self.is_student}")    def serialize(self, filename):        """Serializes the object and saves it to a file using pickle."""        try:            with open(filename, 'wb') as f:                pickle.dump(self, f)            print(f"Object serialized and saved to '{filename}'.")        except FileNotFoundError:            print(f"Error: File '{filename}' not found.")    @classmethod    def deserialize(cls, filename):        """Deserializes an object from a file using pickle."""        try:            with open(filename, 'rb') as f:                return pickle.load(f)        except (FileNotFoundError, pickle.UnpicklingError):            print(f"Error: Failed to deserialize object from '{filename}'.")            return None