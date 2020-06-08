"""This module emulates the java library 'inputStream'."""
from .javaclass import JavaClass


class InputStream(JavaClass):
    """
    This class emulates functions of inputStream.

    Attributes:
        class_name:     The name of the class.
    """
    def __init__(self):
        """The constructor for InputStream class."""
        super().__init__()
        self.class_name = 'java/io/InputStream'

    def has_method(self, name, desc):
        """
        This function determines if inputStream is present in a .class file.

        :param name:    The name of the method.
        :param desc:    The description of the method.
        :return name:   The name of the method in the list.
        """
        return name in ['read']

    def run_method(self, name, desc, frame):
        """
        This function runs the inputStream method.

        :param name:    The name of the method.
        :param desc:    The method's description.
        :param frame:   The frame relative to the method.
        :return s:      The string to be printed.
        """
        if name == 'read':
            s = input()
            return s

