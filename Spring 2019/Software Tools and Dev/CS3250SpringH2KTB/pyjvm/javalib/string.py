"""This module emulates the Java String library."""

from .javaclass import JavaClass


class String(JavaClass):
    """
    This class serves to emulate functionality of the String class.

    Attributes:
        class_name:     The name of the class.
    """
    def __init__(self):
        """This is the constructor for String class."""
        super().__init__()
        self.class_name = 'java/lang/String'

    def has_method(self, name, desc):
        """
        This function checks if Scanner is in a .class file.

        :param name:    The name of the method to be found.
        :param desc:    The description of the method.
        :return name:   The name of the found method.
        """
        return name in ['length', 'charAt']

    def run_method(self, name, desc, frame):
        """
        This function runs the Scanner class.

        :param name:    The name of the method to be run.
        :param desc:    The description of the method.
        :param frame:   The frame relative to the method.
        :return s:      The string at 'index'.
        """
        super().run_method(name, desc, frame)
        if name == 'length':
            val = frame.pop()
            return len(val)
        elif name == 'charAt':
            index = frame.pop()
            s = frame.pop()
            return s[index]
