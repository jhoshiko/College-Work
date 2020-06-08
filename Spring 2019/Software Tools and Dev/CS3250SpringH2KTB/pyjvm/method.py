"""This module instantiates methods for a Java .class file."""
import io
from .reader import Reader
from .attribute import Attribute
from .code import Code
from .util import *


def access_mode(flags):
    """This function returns the access type of a method."""
    if flags & 0x08:
        return "static "
    return ""



class Method(object):
    """
    This class instantiates methods values for Java .class file.

    Attributes:
        access_flags:   The access type of the method.
        name_index:     The name index of the method within the ConstantPool.
        desc_index:     The description index of the method.
        attributes:     The attributes of the method.
        name:           The name of the method.
        desc:           The method's arguments.
        cpool:          The class file's ConstantPool.
        code:           The method's code.
    """
    def __init__(self, r, cpool):
        """
        The constructor for Method class.

        :param r: Bytecode interpreter.
        :param cpool: ConstantPool.
        """
        self.access_flags = r.u16()
        self.name_index = r.u16()
        self.desc_index = r.u16()
        self.attributes = [Attribute(r, cpool) for _ in range(r.u16())]
        self.name = cpool[self.name_index].string
        self.desc = cpool[self.desc_index].string
        self.cpool = cpool
        self.code = self._code()

    def _code(self):
        """
        This function parses the code of the method.

        :return c: Returns the code.
        """
        c = None
        for attr in self.attributes:
            if attr.name == 'Code':
                bytecode = io.BytesIO(attr.data)
                r = Reader(bytecode)
                c = Code(r, self)
        return c

    def dump(self, prefix=''):
        """
        This function prints a representation of the method.
        :param prefix: The prefix of the method.
        """
        print(prefix, end='')
        print(access_mode(self.access_flags), end='')
        print(desc_ret(self.desc), end='')
        print(self.name, end='')
        print(desc_arg(self.desc), end='')
        print(";")
        print(prefix + '  Code:')
        self.code.dump(prefix + '     ')
