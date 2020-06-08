"""attribute.py is responsible for solely instantiating the attribute
   tables for a Java .class file by a proper constructor and dump method
   to print a representation of said attributes table."""


class Attribute:
    """
    This class instantiates the attribute tables for a Java .class file.

    Attributes:
        name_index:     The index of the attribute name within the constant pool.
        length:         The number of subsequent bytes within the attribute.
        data:           The bytes denoting the information of the attribute.
        name:           The attribute name taken from the constant pool.
    """
    def __init__(self, reader, cpool):
        """
        The constructor for Attribute class.

        :param reader: The bytecode interpreter.
        :param cpool:  The constant pool.
        """
        self.name_index = reader.u16()
        self.length = reader.u32()
        self.data = reader.raw(self.length)
        self.name = cpool[self.name_index].string

    def dump(self):  # pragma: no cover
        """
        This function prints a representation of the attributes table.
        """
        print("** ATTRIBUTE **")
        print("name: ", self.name)
        print("data: ", self.data.hex())
