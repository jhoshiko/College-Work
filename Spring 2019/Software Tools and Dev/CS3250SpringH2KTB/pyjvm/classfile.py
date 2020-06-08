"""This class  represents a real Java .class file. The ClassFile class inherits from the
   JavaClass, since it represents a Java class. However, this class adds way more
   functionality to the normal JavaClass, since it allows us to load any Java class
   from a .class file. A few other classes have been implemented to help representing
   the different components of a Java class file: Attribute, Code, ConstantPool,
   Field, Method."""
import struct
from .javalib.javaclass import JavaClass
from .cpool import ConstantPool
from .reader import Reader
from .attribute import Attribute
from .field import Field
from .method import Method


class ClassFile(JavaClass):
    """
    This class instantiates attributes for a given Java .class file.

    Attributes:
        file_path:    The directory path to a given .class file.
        magic:        The magic number associated with Java .class files.
        minor:        The minor version number of the .class file.
        major:        The Major version number of the .class file.
        cpool:        The constant pool table of the .class file.
        access_flags: The access flags given by the .class file.
        class_name:   The name of a given class within cpool.
        super_class:  The name of a given super class within cpool.
        interfaces:   The interfaces contained in the .class file.
        fields:       The fields contained in the .class file.
        methods:      The methods contained in the .class file.
        attributes:   The attributes of a given method.
    """

    def __init__(self, path):
        """
        The constructor for ClassFile class.

        :param path: The directory path to a Java .class file.
        """
        super().__init__()

        self.file_path = path
        cfile = open(path, 'rb')

        r = Reader(cfile)

        self.magic = r.u32()
        assert self.magic == 0xcafebabe

        self.minor = r.u16()
        self.major = r.u16()

        self.cpool = ConstantPool(r, self)

        self.access_flags = r.u16()

        self.class_name = self.cpool[r.u16()].name
        self.super_class = self.cpool[r.u16()].name

        ifaces_count = r.u16()
        self.interfaces = []
        for i in range(ifaces_count):  # pragma: no cover
            self.interfaces.append(self.cpool[r.u16()].name)

        self.fields = [Field(r, self.cpool) for _ in range(r.u16())]
        self.methods = [Method(r, self.cpool) for _ in range(r.u16())]
        self.attributes = [Attribute(r, self.cpool) for _ in range(r.u16())]

        for attr in self.attributes:
            if attr.name == 'SourceFile':
                index = struct.unpack('!H', attr.data)[0]
                self.source_file = self.cpool[index].string

        cfile.close()

    def has_method(self, name, desc):
        """
        This function determines if a given method is present in the super class.

        :param name: The name of the method.
        :param desc: The description of the method.
        :return:     Boolean: True if so, False if not.
        """
        if super().has_method(name, desc):
            return True
        for m in self.methods:
            if m.name == name and m.desc == desc:
                return True
        return False  # pragma: no cover

    def dump(self, prefix=''):  # pragma: no cover
        """
        This function prints the Java bytecode representation of the given .class file.

        :param prefix: The prefix of a given class and its methods.
        """
        print(prefix, 'Compiled from: ', self.source_file, end='\n\n')
        print(prefix, 'class {} {{ '.format(self.class_name))
        for m in self.methods:
            m.dump(prefix + '  ')
        print('}')

    def dump_cpool(self):  # pragma: no cover
        """
        This function prints a representation of a .class file's constant pool.
        """
        self.cpool.dump()
