"""The CPInfo class and the ConstantPool class work together to build the constant
   pool for use by the HKTBJVM and parse those constants for a given Java .class file."""


CPTags = {
    0: 'None',
    1: 'Utf8',
    3: 'Integer',
    4: 'Float',
    5: 'Long',
    6: 'Double',
    7: 'Class',
    8: 'String',
    9: 'Field',
    10: 'Method',
    11: 'InterfaceMethod',
    12: 'NameAndType',
    15: 'MethodHandle',
    16: 'MethodType',
    18: 'InvokeDynamic',
    19: 'Module',
    20: 'Package'
}


class CPInfo:
    """
    This class parses constants of the constant pool for a given Java .class file.

    Attributes:
        tag:    The numerical tag of a given constant.
        data:   The data of the given constant.
        refs:   The reference indexes of a given constant to other constants.
    """
    def __init__(self, reader):
        """
        The constructor for CPInfo class.

        :param reader: The hexadecimal byte interpreter.
        """
        if reader is None:
            self.tag = CPTags[0]
        else:
            self.tag = CPTags[reader.u08()]

        self.data = None
        self.refs = []

        tag = self.tag

        if tag == 'None':
            pass #Travis exception
        elif tag == 'Utf8':
            self._parse_utf8(reader)
        elif tag == 'Integer':
            self._parse_integer(reader)
        elif tag == 'Float':
            self._parse_float(reader)
        elif tag == 'Long':
            self._parse_long(reader)
        elif tag == 'Double':
            self._parse_double(reader)
        elif tag == 'Class':
            self._parse_class(reader)
        elif tag == 'String':
            self._parse_string(reader)
        elif tag in ['Field', 'Method', 'InterfaceMethod']:
            self._parse_field(reader)
        elif tag == 'NameAndType':
            self._parse_nat(reader)
        elif tag == 'MethodHandle':
            self._parse_methodhandle(reader)
        elif tag == 'MethodType':
            self._parse_methodtype(reader)
        elif tag == 'Module':
            self._parse_module(reader)
        elif tag == 'Package':
            self._parse_package(reader)
        else:
            self._parse_other(reader)

    def _parse_utf8(self, reader):
        """Parses utf8 constants."""
        vlen = reader.u16()
        self.string = reader.get('!{}s'.format(vlen)).decode('utf-8')
        self.data = self.string

    def _parse_integer(self, reader):
        """Parses integer constants."""
        self.integer = reader.s32()
        self.data = self.integer

    def _parse_float(self, reader):
        """Parses float constants."""
        self.float = reader.get('!f')
        self.data = self.float

    def _parse_long(self, reader):
        """Parses long constants."""
        self.long = reader.u64()
        self.data = self.long

    def _parse_double(self, reader):
        """Parses double constants."""
        self.double = reader.get('!d')
        self.data = self.double

    def _parse_class(self, reader):
        """Parses utf8 constants."""
        self.name_index = reader.u16()
        self.refs.append(self.name_index)

    def _parse_string(self, reader):
        """Parses string constants."""
        self.string_index = reader.u16()
        self.refs.append(self.string_index)

    def _parse_field(self, reader):
        """Parses field constants."""
        self.class_index = reader.u16()
        self.name_and_type_index = reader.u16()
        self.refs.append(self.class_index)
        self.refs.append(self.name_and_type_index)

    def _parse_nat(self, reader):
        """Parses Name and Type constants."""
        self.name_index = reader.u16()
        self.desc_index = reader.u16()
        self.refs.append(self.name_index)
        self.refs.append(self.desc_index)

    def _parse_methodhandle(self, reader):
        """Parses method handle constants."""
        self.ref_kind = reader.u08()
        self.ref_index = reader.u16()
        self.data = self.ref_kind
        self.refs.append(self.ref_index)

    def _parse_methodtype(self, reader):
        """Parses method type constants."""
        self.desc_index = reader.u16()
        self.refs.append(self.desc_index)

    def _parse_module(self, reader):
        """Parses module constants."""
        self.name_index = reader.u16()
        self.refs.append(self.name_index)

    def _parse_package(self, reader):
        """Parses package constants."""
        self.name_index = reader.u16()
        self.refs.append(self.name_index)

    def _parse_other(self, reader):
        """Parses any left over references the cpool may contain."""
        self.refs.append(reader.u16())
        self.refs.append(reader.u16())


class ConstantPool:
    """
    This class builds the constant pool for use by the HKTBJVM.

    Attributes:
        slots:  The list containing entries of the constant pool.
        cf:     The class file object being operated on.
    """
    def __init__(self, reader, class_file):
        """
        The constructor for ConstantPool class.

        :param reader:      The bytecode interpreter.
        :param class_file:  The Java .class file.
        """

        self.slots = []
        self.slots.append(CPInfo(None))
        self.cf = class_file

        size = reader.u16()
        while len(self.slots) < size:
            self._addslot(reader)

        self._resolve()

    def __getitem__(self, item):
        return self.slots[item]

    def __len__(self):
        return len(self.slots)

    def _addslot(self, reader):
        """Adds a constant pool entry into 'slots'."""
        info = CPInfo(reader)
        self.slots.append(info)
        if info.tag in ['Long', 'Double']:
            self.slots.append(info)

    def _resolve(self):
        """Resolves 'slot' entries into strings."""
        for member in self.slots:
            if 'name_index' in member.__dict__:
                member.name = self.slots[member.name_index].string
            if 'desc_index' in member.__dict__:
                member.desc = self.slots[member.desc_index].string
            if 'string_index' in member.__dict__:
                member.string = self.slots[member.string_index].string

    def dump(self):  # pragma: no cover
        """Prints a representation of the constant pool."""
        for s in self.slots:
            print("\t", self.slots.index(s), ': ', end == '')
            if s.tag is None:
                print("None")
                continue
            print(s.tag)
            print("\t\tdata = ", s.data)
            print("\t\trefs = ", s.refs)
