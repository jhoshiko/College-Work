"""This module serves to emulate the scanner Java library for HTKBJVM."""
from .javaclass import JavaClass


class Scanner(JavaClass):
    """
    This class emulates functionality of the scanner class.

    Attributes:
        class_name:     The name of the class
        instream:       The inputStream used for scanner.
    """
    def __init__(self):
        """The constructor for Scanner class."""
        super().__init__()
        self.class_name = 'java/util/Scanner'
        self.instream = None

    def python_initialize(self, *args):
        """This function has yet to be fully implemented."""
        self.instream = None

    def has_method(self, name, desc):
        """
        This function determines if scanner is in a .class file.

        :param name:    The name of the method to be found.
        :param desc:    The description of the method.
        :return name:   The name of the method if found.
        """
        if name == '<init>' and desc == '(Ljava/io/InputStream;)V':
            return True
        return name in ['nextInt']

    def run_method(self, name, desc, frame):
        """
        This function runs the scanner class.

        :param name:    The name of the method to be run.
        :param desc:    The description of the method.
        :param frame:   The frame relative to the method.
        :return s:      Integer value of the input.
        """
        super().run_method(name, desc, frame)

        if name == 'nextInt':
            if self.instream is not None:
                s = self.instream.run_method('read', '()Ljava/lang/String;', frame)
                return int(s)

        elif name == '<init>' and desc == '(Ljava/io/InputStream;)V':
            ins = frame.pop()
            self.instream = ins

