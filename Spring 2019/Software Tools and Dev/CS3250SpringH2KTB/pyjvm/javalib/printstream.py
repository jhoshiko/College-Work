"""This module emulates the printStream Java library for HTKBJVM."""

from .javaclass import JavaClass
from ..util import *


class PrintStream(JavaClass):
    """
    This class emulates functionality for the printStream library.

    Attributes:
        class_name:    The name of the class.
    """
    def __init__(self):
        """The constructor for PrintStream class."""
        super().__init__()
        self.class_name = 'java/io/PrintStream'

    def has_method(self, name, desc):
        """
        This function determines if printStream is in a .class file.

        :param name:    The name of the method to be found.
        :param desc:    The description of the method to be found.
        :return name:   The name of the method in the list.
        """
        return name in ['print', 'println']

    def run_method(self, name, desc, frame):
        """
        This function serves to run printStream.

        :param name:    The method name to be run.
        :param desc:    The description of the method.
        :param frame:   The frame relative to the method.
        """
        if name == 'print':
            for i in range(desc_nargs(desc)):
                print(frame.pop(), end='')
        elif name == 'println':
            for i in range(desc_nargs(desc)):
                print(frame.pop())

