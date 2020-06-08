"""This module instantiates fields for a Java .class file."""

from .attribute import Attribute


class Field:
    """
    This class instantiates field values for Java .class fields.

    Attributes:
        access_flags:   The access flags of a field.
        name_index:     The constant pool index of the field name.
        desc_index:     The constant pool index of the field description.
        attributes:     The attributes of a field.
        name:           The name of a field.
        desc:           The description of a field.
    """
    def __init__(self, r, cpool):  # pragma: no cover
        """
        This is the constructor for Field class.

        :param r:       The bytecode interpreter.
        :param cpool:   The constant pool of the .class file.
        """
        self.access_flags = r.u16()
        self.name_index = r.u16()
        self.desc_index = r.u16()
        self.attributes = [Attribute(r, cpool) for _ in range(r.u16())]
        self.name = cpool[self.name_index].string
        self.desc = cpool[self.desc_index].string

    def dump(self):  # pragma: no cover
        """This function prints a representation of a Java field."""
        print("** FIELD **")
        print("name: ", self.name)
        print("access: ", hex(self.access_flags))
        print("desc: ", self.desc)
        print("attrs:")
        for attr in self.attributes:
            attr.dump()
