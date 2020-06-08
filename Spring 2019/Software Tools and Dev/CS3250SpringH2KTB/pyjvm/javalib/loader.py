"""This module serves as the loader for HTKBJVM's Java library."""

from .javaclass import JavaClass
from .printstream import PrintStream
from .inputstream import InputStream
from .system import System
from .string import String
from .scanner import Scanner


javalibs = [
    JavaClass(),
    PrintStream(),
    InputStream(),
    System(),
    String(),
    Scanner()
]


def load_javalib_classes(machine):
    """
    This function loads relevant javalib classes for use by machine.

    :param machine:     The main module of the HTKBJVM.
    """
    for lib in javalibs:
        machine.load_class(lib)
