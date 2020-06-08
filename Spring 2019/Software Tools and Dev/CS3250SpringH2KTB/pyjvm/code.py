"""The code.py file is responsible for instantiating the code attribute of a Java
   .class file by using the proper constructor and dump method to print a
   representation of said code."""
from .opcodes import *
import struct


class Code:
    """
    Class instantiates the code attribute of a Java .class file.

    Attributes:
         method:        The method contained in the code attribute.
         cpool:         The constant pool of the .class file.
         max_stack:     The given stack size of the code.
         max_locals:    The given variable table size.
         code_length:   The number of the subsequent bytes.
         raw_code:      The raw bytes of the code.
    """
    def __init__(self, r, method):
        """
        The constructor for Code class.

        :param r:       The bytecode interpreter.
        :param method:  The method containing the code.
        """
        self.method = method
        self.cpool = method.cpool
        self.max_stack = r.u16()
        self.max_locals = r.u16()
        self.code_length = r.u32()
        self.raw_code = r.raw(self.code_length)

    def dump(self, prefix=''):  # pragma: no cover
        """
        This function prints a representation of the code.

        :param prefix:  The prefix given by the methods.
        """
        i = 0
        while i < self.code_length:
            print(prefix, '{:>2}: '.format(i), end='')

            inst = struct.unpack_from('!B', self.raw_code, i)[0]
            i += 1
            opcode = OPCODES[Inst(inst)]

            print('{:16}'.format(opcode.name), end='')
            if opcode.arglen == 1:
                arg = struct.unpack_from('!B', self.raw_code, i)[0]
            elif opcode.arglen == 2:
                arg = struct.unpack_from('!H', self.raw_code, i)[0]
            elif opcode.arglen == 4:
                arg = struct.unpack_from('!I', self.raw_code, i)[0]
            elif opcode.arglen == 8:
                arg = struct.unpack_from('!Q', self.raw_code, i)[0]
            else:
                arg = None

            i += opcode.arglen

            if arg is not None:
                if opcode.ref:
                    print('#{}'.format(arg), end='')
                else:
                    print(arg, end='')
            print()
