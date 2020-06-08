""" This class represents a JVM and provides a way to load and run Java code. The main interface
    consist of a couple of methods that allow loading Java classes into the Machine. This can be
    any class that inherits from JavaClass (including ClassFile).
    Once the Machine is loaded with Java classes, a 'call_function' method is provided that allows
    us to call any function from any loaded class (typically we want to call the main function
    in the main class)."""
from .opcodes import *
from .classfile import ClassFile
from .frame import Frame


class Machine:
    """
    This class provides a way to load and run Java code.

    Attributes:
        class_files:    The variable holding class files.
        current_frame:  The current frame being used.
    """

    def __init__(self):
        """
        The Machine constructor.
        """
        self.class_files = {}
        self.current_frame = None

    def load_class_file(self, path):
        """
        This function loads class file given a path.

        :param path: Given path of file.
        :return: Loads file into cf variable.
        """
        cf = ClassFile(path)
        self.class_files[cf.class_name] = cf

    def load_class(self, cf):
        """
        This function loads a class in the given file.

        :param cf: Variable holding loaded class file.
        :return: Loads class into name variable.
        """
        name = cf.name()
        self.class_files[name] = cf

    def call_function(self, fname, *args):
        """
        This function calls a function within the class.

        :param fname: Function name.
        :param args: Arguments for function.
        :return: Returns execution of frames.
        """
        cname = '/'.join(fname.split('/')[:-1])
        mname = fname.split('/')[-1]
        if cname in self.class_files:
            cf = self.class_files[cname]
            for m in cf.methods:
                if m.name == mname:
                    frame = Frame(m, self)
                    for i, arg in enumerate(args):
                        frame.set_local(i, arg)
                    self.current_frame = frame
                    return self.execute(frame)

    def execute(self, frame):
        """
        This function executes defined functions.

        :param frame: Given frame to execute.
        :return: Returns popped frame or error message.
        """
        while True:
            op = frame.u08()
            if op is None:  # pragma: no cover
                print("-- NOOP --")
                break
            inst = Inst(op)

            if len(frame.stack) > frame.max_stack:
                print("-- MAX STACK --")
                break

            if inst in OPCODES:
                OPCODES[inst].fn(frame, self.class_files)
            else:
                print("-- UNDEFINED INSTRUCTION: ", inst, " --")
                break

            if inst in [Inst.IRET, Inst.LRET, Inst.ARETURN, Inst.DRETURN, Inst.FRETURN]:
                return frame.pop()
            elif inst == Inst.RETURN:
                return

    def dump(self):  # pragma: no cover
        """
        This function dumps contents of class files to cf variable.
        :return: Dumped contents.
        """
        print("*** MACHINE ***")
        for name in self.class_files:
            cf = self.class_files[name]
            cf.dump()

    def dump2(self):  # pragma: no cover
        """
        This function dumps contents of class files to cf variable.
        :return: Dumped contents.
        """
        print('*** Machine Dump ***')

        print('>> Loaded Classes:')
        for name in self.class_files:
            print('  ', name)
            cf = self.class_files[name]

            for m in cf.methods:
                print('    [METHOD]', m.name, '->', m.desc)
                for attr in m.attributes:
                    print('      [ATTR] {} ({} bytes)'.format(attr.name, len(attr.data)))
                    if attr.name == 'Code':
                        print('     ', vars(m.code))
            print()

            for field in cf.fields:
                print('    [FIELD]', field.name, ':', field.desc)
                for attr in field.attributes:
                    print('      [ATTR] {} ({} bytes)'.format(attr.name, len(attr.data)))
                    if attr.name == 'ConstantValue':
                        index = struct.unpack('!H', attr.data)[0]
                        print('      ', cf.cpool[index - 1].string)
            print()

            for attr in cf.attributes:
                print('    [ATTR] {} ({} bytes)'.format(attr.name, len(attr.data)))
            print()
