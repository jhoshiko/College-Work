"""This module is responsible for reading and returning values of certain types."""
import struct


class Reader:
    """
    This class reads and returns desired values.

    Attributes:
        cfile:  The name of the .class file being accessed.
    """

    def __init__(self, cfile):
        """
        Constructor of the Reader class.

        :param cfile: The variable .class file is assigned to.
        """

        self.cfile = cfile

    def get(self, fmt):
        """
        This function returns a read value from cfile.

        :param fmt: Format.
        :return: Returns value.
        """
        size = struct.calcsize(fmt)
        val = struct.unpack(fmt, self.cfile.read(size))
        if len(val) == 1:
            val = val[0]
        return val

    def raw(self, nbytes):
        """
        This function returns a byte value.

        :param nbytes: Number of bytes.
        :return: Returns byte value.
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
