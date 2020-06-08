"""Frame is a helper class that is needed to execute Java bytecode. Every time a new method is
   executed, it is the Machine's responsibility to create a new Frame that contains the resources
   needed by the method's code (e.g., stack, local variable array).
   Each frame is linked to a specific method and each method contains code.
   All the opcodes supported by our JVM are implemented in the "opcodes.py" file.
   The opcodes need a frame as their execution environment."""
import struct


class Frame:
    """
    This class is able to manipulate many instances of itself for proper operation

    Attributes:
        stack:          The table of frames.
        cf:             The class file.
        method:         The given function.
        machine:        The given machine instance.
        cpool:          The ConstantPool instance.
        max_stack:      The maximum stack value.
        max_locals:     The maximum of allowed local values.
        code:           The raw bytes of code.
        code_length:    The code length.
        locals:         The specified local values.
        ip:             The instruction pointer.
    """
    def __init__(self, method, machine):
        """
        The Frame constructor.

        :param method: The given function.
        :param machine: The given machine instance.
        """
        self.stack = []
        self.cf = method.cpool.cf
        self.method = method
        self.machine = machine
        self.cpool = method.cpool
        self.max_stack = method.code.max_stack
        self.max_locals = method.code.max_locals
        self.code = method.code.raw_code
        self.code_length = method.code.code_length
        self.locals = [self.cf] + [0 for i in range(self.max_locals)]
        self.ip = 0

    def execute(self):
        """
        This function executes the machine instance.

        :return: None.
        """
        self.machine.execute(self)

    def set_local(self, i, value):
        """
        This function sets a local value.

        :param i: Given index.
        :param value: Specified value.
        :return: None.
        """
        self.locals[i] = value

    def get_local(self, i):
        """
        This function returns a local.
        :param i: Given index.
        :return: Specified index value.
        """
        return self.locals[i]

    def push(self, arg):
        """
        This function pushes given arguments.

        :param arg: Argument.
        :return: None.
        """
        self.stack.append(arg)

    def pop(self):
        """
        This function pops the top of the stack.

        :return: Returns popped value.
        """
        return self.stack.pop()

    def get(self, fmt, seek=False):
        """
        This function returns a value.
        :param fmt: Format.
        :param seek: Desired value.
        :return: Desired value or None.
        """
        size = struct.calcsize(fmt)
        if size > (self.code_length - self.ip):
            return None
        val = struct.unpack_from(fmt, self.code, self.ip)
        if len(val) == 1:
            val = val[0]
        if seek is False:
            self.ip += size
        return val

    def raw(self, nbytes):
        """
        This function returns raw bytes.
        :param nbytes: Bytes.
        :return: Raw byte value.
        """
        val = self.cfile.read(nbytes)
        return val

    def u08(self):
        """
        Returns unsigned 8 bit value.

        :return: Returns unsigned 8 bit value.
        """
        return self.get('!B')

    def s08(self):
        """
        Returns signed 8 bit value.

        :return: Returns signed 8 bit value.
        """
        return self.get('!b')

    def u16(self):
        """
        Returns unsigned 16 bit value.

        :return: Returns unsigned 16 bit value.
        """
        return self.get('!H')

    def s16(self):
        """
        Returns signed 16 bit value.

        :return: Returns signed 16 bit value.
        """
        return self.get('!h')

    def u32(self):
        """
        Returns unsigned 32 bit value.

        :return: Returns unsigned 32 bit value.
        """
        return self.get('!I')

    def s32(self):
        """
        Returns signed 32 bit value.

        :return: Returns signed 32 bit value.
        """
        return self.get('!i')

    def u64(self):
        """
        Returns unsigned 64 bit value.

        :return: Returns unsigned 64 bit value.
        """
        return self.get('!Q')

    def s64(self):
        """
        Returns signed 64 bit value.

        :return: Returns signed 64 bit value.
        """
        return self.get('!q')
