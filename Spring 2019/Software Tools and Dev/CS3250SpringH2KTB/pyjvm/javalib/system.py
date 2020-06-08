"""This module emulates the Java library System."""

from .javaclass import JavaClass
from .printstream import PrintStream
from .inputstream import InputStream


class System(JavaClass):
    """
    This class serves to emulate functionality of the System class.

    Attributes:
        class_name:        The name of the class.
        instance_fields[]: The list of instance fields.
    """
    def __init__(self):
        """The constructor for System class."""
        super().__init__()
        self.class_name = 'java/lang/System'
        self.instance_fields['out'] = PrintStream()
        self.instance_fields['in'] = InputStream()

    def has_method(self, name, desc):
        """
        This method determines if System is in a .class file.

        :param name:    The name of the method to be found.
        :param desc:    The description of the method.
        :return name:   The name of the method found.
        """
        return name in ['append', 'toString']

    def run_method(self, name, desc, frame):
        """
        This function runs System methods.

        :param name:    The name of the method to be run.
        :param desc:    The description of the method.
        :param frame:   The frame relative to the method.
        """
        if name == 'append':
            v2 = str(frame.pop())
            v1 = str(frame.pop())
            frame.push(v1 + v2)
        elif name == 'toString':
            v1 = frame.pop()
            frame.pop()
            frame.push(v1)
