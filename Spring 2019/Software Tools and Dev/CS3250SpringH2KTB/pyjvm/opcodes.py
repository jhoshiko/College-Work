"""This module implements OpCode functionality for the HTKBJVM."""
from enum import Enum
from .util import *
from .checkbounds import *


OPCODES = {}


class OpCode(object):
    """
    This class instantiates the OpCodes.

    Attributes:
        fn:     The function.
        name:   The name of the OpCode.
        arglen: The number of arguments in the OpCode.
        ref:    The OpCode's references.
    """
    def __init__(self, fn, arglen=0, ref=False):
        """
        This is the OpCode Constructor.
        """
        self.fn = fn
        self.name = fn.__name__
        self.arglen = arglen
        self.ref = ref


class Inst(Enum):
    """
    This class enumerates the OpCodes.
    """
    ICONST_M1     = 0x02
    ICONST_0      = 0x03
    ICONST_1      = 0x04
    ICONST_2      = 0x05
    ICONST_3      = 0x06
    ICONST_4      = 0x07
    ICONST_5      = 0x08
    LCONST_0      = 0x09
    LCONST_1      = 0x0A
    DCONST_0      = 0x0E
    DCONST_1      = 0x0F
    FCONST_0      = 0x0B
    FCONST_1      = 0x0C
    FCONST_2      = 0x0D
    BIPUSH        = 0x10
    SIPUSH        = 0x11
    LDC           = 0x12
    LDC2_W        = 0x14
    ILOAD         = 0x15
    LLOAD         = 0x16
    DLOAD         = 0x18
    FLOAD         = 0x17
    ILOAD_0       = 0x1A
    ILOAD_1       = 0x1B
    ILOAD_2       = 0x1C
    ILOAD_3       = 0x1D
    LLOAD_0       = 0x1E
    LLOAD_1       = 0x1F
    LLOAD_2       = 0x20
    LLOAD_3       = 0x21
    DLOAD_0       = 0x26
    DLOAD_1       = 0x27
    DLOAD_2       = 0x28
    DLOAD_3       = 0x29
    FLOAD_0       = 0x22
    FLOAD_1       = 0x23
    FLOAD_2       = 0x24
    FLOAD_3       = 0x25
    ALOAD_0       = 0x2A
    ALOAD_1       = 0x2B
    ALOAD_2       = 0x2C
    ALOAD_3       = 0x2D
    IALOAD        = 0x2E
    AALOAD        = 0x32
    ISTORE        = 0x36
    LSTORE        = 0x37
    FSTORE        = 0x38
    DSTORE        = 0x39
    ISTORE_0      = 0x3B
    ISTORE_1      = 0x3C
    ISTORE_2      = 0x3D
    ISTORE_3      = 0x3E
    LSTORE_0      = 0x3F
    LSTORE_1      = 0x40
    LSTORE_2      = 0x41
    LSTORE_3      = 0x42
    DSTORE_3      = 0x4A
    FSTORE_0      = 0x43
    FSTORE_1      = 0x44
    FSTORE_2      = 0x45
    FSTORE_3      = 0x46
    ASTORE_0      = 0x4B
    ASTORE_1      = 0x4C
    ASTORE_2      = 0x4D
    ASTORE_3      = 0x4E
    IASTORE       = 0x4F
    AASTORE       = 0x53
    POP           = 0x57
    DUP           = 0x59
    IADD          = 0x60
    LADD          = 0x61
    DADD          = 0x63
    ISUB          = 0x64
    DSUB          = 0x67
    IMUL          = 0x68
    DMUL          = 0x6B
    DDIV          = 0x6F
    IREM          = 0x70
    IINC          = 0x84
    I2L           = 0x85
    I2F           = 0x86
    I2D           = 0x87
    I2B           = 0x91
    I2C           = 0x92
    I2S           = 0x93

    F2D           = 0x8D
    F2I           = 0x8B
    F2L           = 0x8C
    FADD          = 0x62
    FDIV          = 0x6E
    FMUL          = 0x6A
    FREM          = 0x72
    FSUB          = 0x66
    FNEG          = 0x76

    L2D           = 0x8A
    L2F           = 0x89
    L2I           = 0x88
    LDIV          = 0x6D
    LMUL          = 0x69
    LSUB          = 0x65
    LNEG          = 0x75
    LREM          = 0X71
    LSHL          = 0x79
    LSHR          = 0x7B
    LAND          = 0x7F
    LOR           = 0x81
    LXOR          = 0x83

    DCMPG         = 0x98
    IFNE          = 0x9A
    IFLT          = 0x9B
    IFGE          = 0x9C
    IFLE          = 0x9E
    IF_ICMPLT     = 0xA1
    IF_ICMPGE     = 0xA2
    IF_ICMPGT     = 0xA3
    IF_ICMPLE     = 0xA4
    GOTO          = 0xA7
    IRET          = 0xAC
    LRET          = 0xAD
    DRETURN       = 0xAF
    ARETURN       = 0xB0
    RETURN        = 0xB1
    FRETURN       = 0xAE
    GETSTATIC     = 0xB2
    PUTSTATIC     = 0xB3
    GETFIELD      = 0xB4
    PUTFIELD      = 0xB5
    INVOKEVIRTUAL = 0xB6
    INVOKESPECIAL = 0xB7
    INVOKESTATIC  = 0xB8
    NEW           = 0xBB
    NEWARRAY      = 0xBC
    ANEWARRAY     = 0xBD
    ARRAYLENGTH   = 0xBE


def opcode(inst, arglen=0, ref=False):
    """
    The OpCode decorator.

    :param inst: The instruction object.
    :param arglen: The length of OpCode.
    :param ref: The reference indicator.
    :return inner: The nested function.
    """
    def inner(fn):
        """
        This function decorates OpCodes.

        :param fn: Function to be decorated.
        :return fn: Returns the function.
        """
        OPCODES[inst] = OpCode(fn, arglen, ref)
        return fn
    return inner


@opcode(Inst.ICONST_M1)
def iconst_m1(frame, class_files=[]):
    """This function pushes -1 to frame stack."""
    frame.push(-1)


@opcode(Inst.ICONST_0)
def iconst_0(frame, class_files=[]):
    """This function pushes 0 to frame stack."""
    frame.push(0)


@opcode(Inst.ICONST_1)
def iconst_1(frame, class_files=[]):
    """This function pushes 1 to frame stack."""
    frame.push(1)


@opcode(Inst.ICONST_2)
def iconst_2(frame, class_files=[]):
    """This function pushes 2 to frame stack."""
    frame.push(2)


@opcode(Inst.ICONST_3)
def iconst_3(frame, class_files=[]):
    """This function pushes 3 to frame stack."""
    frame.push(3)


@opcode(Inst.ICONST_4)
def iconst_4(frame, class_files=[]):
    """This function pushes 4 to frame stack."""
    frame.push(4)


@opcode(Inst.ICONST_5)
def iconst_5(frame, class_files=[]):
    """This function pushes 5 to frame stack."""
    frame.push(5)


@opcode(Inst.IADD)
def iadd(frame, class_files=[]):
    """This function performs addition."""
    frame.push(integer_boundaries(frame.pop() + frame.pop()))


@opcode(Inst.ISUB)
def isub(frame, class_files=[]):
    """This function performs subtraction."""
    a = frame.pop()
    b = frame.pop()
    frame.push(integer_boundaries(b - a))


@opcode(Inst.IMUL)
def imul(frame, class_files=[]):
    """This function performs multiplication."""
    a = frame.pop()
    b = frame.pop()
    frame.push(integer_boundaries(a * b))


@opcode(Inst.DCONST_0)
def dconst_0(frame, class_files=[]):
    """This function pushes a double 0.0 to frame stack."""
    frame.push(0.0)


@opcode(Inst.DCONST_1)
def dconst_1(frame, class_files=[]):
    """This function pushes a double 1.0 to frame stack."""
    frame.push(1.0)


@opcode(Inst.FCONST_0)
def fconst_0(frame, class_files=[]):
    """This function pushes a float 0.0 to frame stack."""
    frame.push(float(0.0))


@opcode(Inst.LCONST_0)
def lconst_0(frame, class_files=[]):
    """This function pushes a double 0 to frame stack."""
    frame.push(0)


@opcode(Inst.LCONST_1)
def iconst_1(frame, class_files=[]):
    """This function pushes a double 1 to frame stack."""
    frame.push(1)


@opcode(Inst.FCONST_1)
def fconst_1(frame, class_files=[]):
    """This function pushes a double 1.0 to frame stack."""
    frame.push(float(1.0))


@opcode(Inst.FCONST_2)
def fconst_2(frame, class_files=[]):
    """This function pushes a double 2.0 to frame stack."""
    frame.push(float(2.0))


@opcode(Inst.BIPUSH)
def bipush(frame, class_files=[]):
    """This function pushes a value to frame stack."""
    a = frame.u08()
    frame.push(a)


@opcode(Inst.ALOAD_0)
def aload_0(frame, class_files=[]):
    """This function loads an array reference from the frame stack."""
    a = frame.get_local(0)
    frame.push(a)


@opcode(Inst.ILOAD, 1)
@opcode(Inst.LLOAD, 1)
@opcode(Inst.FLOAD, 1)
def iload(frame, class_files=[]):
    """This function loads numerical values off of the variable table."""
    i = frame.u08()
    a = frame.get_local(i)
    frame.push(a)


@opcode(Inst.ILOAD_0)
@opcode(Inst.LLOAD_0)
@opcode(Inst.FLOAD_0)
def iload_0(frame, class_files=[]):
    """This function loads into index 0 off the variable table."""
    a = frame.get_local(0)
    frame.push(a)


@opcode(Inst.ILOAD_1)
@opcode(Inst.LLOAD_1)
@opcode(Inst.FLOAD_1)
def iload_1(frame, class_files=[]):
    """This function loads into index 1 off the variable table."""
    a = frame.get_local(1)
    frame.push(a)


@opcode(Inst.ILOAD_2)
@opcode(Inst.LLOAD_2)
@opcode(Inst.FLOAD_2)
def iload_2(frame, class_files=[]):
    """This function loads into index 2 off the variable table."""
    a = frame.get_local(2)
    frame.push(a)


@opcode(Inst.ILOAD_3)
@opcode(Inst.LLOAD_3)
@opcode(Inst.FLOAD_3)
def iload_3(frame, class_files=[]):
    """This function loads into index 3 off the variable table."""
    a = frame.get_local(3)
    frame.push(a)


@opcode(Inst.ISTORE, 1)
@opcode(Inst.LSTORE, 1)
@opcode(Inst.FSTORE, 1)
def istore(frame, class_files=[]):
    """This function stores value on the variable table."""
    i = frame.u08()
    a = frame.pop()
    frame.set_local(i, a)


@opcode(Inst.ISTORE_0)
@opcode(Inst.LSTORE_0)
@opcode(Inst.FSTORE_0)
def istore_0(frame, class_files=[]):
    """This function stores value on the variable table at index 0."""
    a = frame.pop()
    frame.set_local(0, a)


@opcode(Inst.ISTORE_1)
@opcode(Inst.LSTORE_1)
@opcode(Inst.FSTORE_1)
def istore_1(frame, class_files=[]):
    """This function stores value on the variable table at index 1."""
    a = frame.pop()
    frame.set_local(1, a)


@opcode(Inst.ISTORE_2)
@opcode(Inst.LSTORE_2)
@opcode(Inst.FSTORE_2)
def istore_2(frame, class_files=[]):
    """This function stores value on the variable table at index 2."""
    a = frame.pop()
    frame.set_local(2, a)


@opcode(Inst.ISTORE_3)
@opcode(Inst.LSTORE_3)
@opcode(Inst.FSTORE_3)
def istore_3(frame, class_files=[]):
    """This function stores value on the variable table at index 3."""
    a = frame.pop()
    frame.set_local(3, a)


@opcode(Inst.I2L)
def i2l(frame, class_files=[]):
    """Pops value off of stack and puts it back on."""
    a = frame.pop()
    frame.push(a)


@opcode(Inst.I2F)
@opcode(Inst.I2D)
def i2f(frame, class_files=[]):
    """Pops value off of stack and converts it to a float."""
    a = frame.pop()
    frame.push(float(a))
    frame.push(float(a))


@opcode(Inst.I2B)
def i2b(frame, class_files=[]):
    """Pops value off of stack and converts it to a byte."""
    a = frame.pop()
    frame.push(bytes([a & 0xff]))


@opcode(Inst.I2C)
def i2c(frame, class_files=[]):
    """Pops value off of stack and converts it to a character."""
    a = frame.pop()
    frame.push(chr(a))


@opcode(Inst.I2S)
def i2s(frame, class_files=[]):
    """Pops value off of stack and converts it to a short."""
    a = frame.pop()
    frame.push(a & 0xffff)


@opcode(Inst.L2D)
@opcode(Inst.F2D)
def f2d(frame, class_files=[]):  # pragma: no cover
    """Pops value off of stack and pushes it back on."""
    a = frame.pop()
    frame.push(float_boundaries(a))


@opcode(Inst.L2I)
@opcode(Inst.F2I)
def f2i(frame, class_files=[]):
    """Pops value off of stack and pushes it back on."""
    a = frame.pop()
    frame.push(integer_boundaries(int(a)))


@opcode(Inst.F2L)
def f2l(frame, class_files=[]):
    """Pops value off of stack and pushes it back on."""
    a = frame.pop()
    frame.push(long_boundaries(a))


@opcode(Inst.FADD)
def fadd(frame, class_files=[]):
    """Adds two floats."""
    a = frame.pop()
    b = frame.pop()
    frame.push(float_boundaries(a + b))


@opcode(Inst.FDIV)
def fdiv(frame, class_files=[]):
    """Divides two floats."""
    a = frame.pop()
    b = frame.pop()
    frame.push(float_boundaries(b / a))


@opcode(Inst.FMUL)
def fmul(frame, class_files=[]):
    """Multiplies two floats."""
    a = frame.pop()
    b = frame.pop()
    frame.push(float_boundaries(b * a))


@opcode(Inst.FREM)
def frem(frame, class_files=[]):
    """Takes remainder two floats."""
    a = frame.pop()
    b = frame.pop()
    frame.push(float_boundaries(b % a))


@opcode(Inst.FSUB)
def fsub(frame, class_files=[]):
    """Subtracts two floats."""
    a = frame.pop()
    b = frame.pop()
    frame.push(float_boundaries(b - a))

@opcode(Inst.FNEG)
def fneg(frame, class_files=[]):
    """Negates a float."""
    a = frame.pop()
    a = a * -1
    frame.push(float_boundaries(a))


@opcode(Inst.L2F)
def l2f(frame, class_files=[]):
    """Converts long to float."""
    a = frame.pop()
    a = float(a)
    frame.push(float_boundaries(a))


@opcode(Inst.LADD)
def ladd(frame, class_files=[]):
    """Adds two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(a + b))


@opcode(Inst.LDIV)
def ldiv(frame, class_files=[]):
    """Divides two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b / a))


@opcode(Inst.LMUL)
def lmul(frame, class_files=[]):
    """Multiplies two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b * a))


@opcode(Inst.LREM)
def lrem(frame, class_files=[]):
    """Takes the remainder of two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b % a))


@opcode(Inst.LSUB)
def lsub(frame, class_files=[]):
    """Subtracts two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b - a))

@opcode(Inst.LNEG)
def lneg(frame, class_files=[]):
    """Negates a long."""
    a = frame.pop()
    frame.push(long_boundaries(a * -1))


@opcode(Inst.LAND)
def land(frame, class_files=[]):
    """Performs logical AND operation on two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b & a))

@opcode(Inst.LOR)
def lor(frame, class_files=[]):
    """Performs logical OR operation on two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b | a))

@opcode(Inst.LXOR)
def lxor(frame, class_files=[]):
    """Performs logical XOR operation on two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b ^ a))

@opcode(Inst.LSHL)
def lshl(frame, class_files=[]):
    """Performs logical left shift operation on two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b << a))

@opcode(Inst.LSHR)
def lshr(frame, class_files=[]):
    """Performs logical right shift operation on two longs."""
    a = frame.pop()
    b = frame.pop()
    frame.push(long_boundaries(b >> a))

@opcode(Inst.GETSTATIC, 2, True)
def getstatic(frame, class_files=[]):
    """Get static field value of a class."""
    field_index = frame.u16()
    mref = frame.cpool[field_index]
    cname = frame.cpool[mref.class_index].name
    nat = frame.cpool[mref.name_and_type_index]
    if cname in class_files:
        cf = class_files[cname]
        if not cf.static_initialized:
            cf.static_initialized = True
            cf.run_method('<clinit>', '()V', frame)
        frame.push(cf.get_field(nat.name))


@opcode(Inst.INVOKEVIRTUAL, 2, True)
def invokevirtual(frame, class_files=[]):
    """Invoke virtual method on an object ref and pushes result to stack."""
    field_index = frame.u16()
    mref = frame.cpool[field_index]
    cname = frame.cpool[mref.class_index].name
    nat = frame.cpool[mref.name_and_type_index]
    if cname in class_files:
        cf = class_files[cname]
        if cf.has_method(nat.name, nat.desc):
            rc = cf.run_method(nat.name, nat.desc, frame)
            frame.pop()
            if not nat.desc.endswith('V'):
                frame.push(rc)
    else:  # pragma: no cover
        print("-- CLASS NOT FOUND: ", cname.string, " --")
        for _ in range(desc_nargs(nat.desc)):
            frame.pop()
        frame.pop()


@opcode(Inst.INVOKESPECIAL, 2, True)
def invokespecial(frame, class_files=[]):
    """Invoke instance method of a object ref and pushes result to stack."""
    field_index = frame.u16()
    mref = frame.cpool[field_index]
    cname = frame.cpool[mref.class_index].name
    nat = frame.cpool[mref.name_and_type_index]
    if cname in class_files:
        cf = class_files[cname]
        if cf.has_method(nat.name, nat.desc):
            cf.run_method(nat.name, nat.desc, frame)
            frame.pop()
    else:  # pragma: no cover
        frame.pop()


@opcode(Inst.LDC, 1, True)
def ldc(frame, class_files=[]):
    """Push a constant at index from the ConstantPool."""
    index = frame.u08()
    val = frame.cpool[index]
    if 'integer' in val.__dict__:
        val = val.integer
    elif 'string' in val.__dict__:
        val = val.string
    else:
        val = val.float
    frame.push(val)


@opcode(Inst.LDC2_W, 2, True)
def ldc2_w(frame, class_files=[]):
    """Push a constant at index from the ConstantPool for longs and doubles."""
    index = frame.u16()
    val = frame.cpool[index]
    if 'double' in val.__dict__:
        val = val.double
    else:
        val = val.long
    frame.push(val)


@opcode(Inst.IINC, 2)
def iinc(frame, class_files=[]):
    """Increments the local variable at given index."""
    index = frame.u08()
    const = frame.s08()
    frame.set_local(index, frame.get_local(index) + const)


@opcode(Inst.NEW, 2)
def new(frame, class_files=[]):
    """Create new object of type by class reference in ConstantPool."""
    index = frame.u16()
    cname = frame.cpool[index].name
    if cname in class_files:
        cf = class_files[cname]
        if cf.file_path:
            obj = cf.__class__(c.file_path)
        else:
            obj = cf.__class__()
        obj.python_initialize()
        frame.push(obj)
    else:
        frame.push(None)


@opcode(Inst.DUP)
def dup(frame, class_files=[]):
    """Duplicate the value."""
    val = frame.pop()
    frame.push(val)
    frame.push(val)


@opcode(Inst.ASTORE_0)
def astore_1(frame, class_files=[]):
    """Store into a reference into local variable 0."""
    obj = frame.pop()
    frame.set_local(0, obj)


@opcode(Inst.ASTORE_1)
def astore_1(frame, class_files=[]):
    """Store a reference into local variable 1."""
    obj = frame.pop()
    frame.set_local(1, obj)


@opcode(Inst.ASTORE_2)
def astore_1(frame, class_files=[]):
    """Store a reference into local variable 2."""
    obj = frame.pop()
    frame.set_local(2, obj)


@opcode(Inst.ASTORE_3)
def astore_1(frame, class_files=[]):
    """Store a reference into local variable 3."""
    obj = frame.pop()
    frame.set_local(3, obj)


@opcode(Inst.ALOAD_0)
def aload_0(frame, class_files=[]):
    """Load a reference onto the stack from local variable 0."""
    obj = frame.get_local(0)
    frame.push(obj)


@opcode(Inst.ALOAD_1)
def aload_1(frame, class_files=[]):
    """Load a reference onto the stack from local variable 1."""
    obj = frame.get_local(1)
    frame.push(obj)


@opcode(Inst.ALOAD_2)
def aload_2(frame, class_files=[]):
    """Load a reference onto the stack from local variable 2."""
    obj = frame.get_local(2)
    frame.push(obj)


@opcode(Inst.ALOAD_3)
def aload_3(frame, class_files=[]):
    """Load a reference onto the stack from local variable 3."""
    obj = frame.get_local(3)
    frame.push(obj)


@opcode(Inst.IRET)
def iret(frame, class_files=[]):
    """Returns an integer."""
    pass


@opcode(Inst.LRET)
def lret(frame, class_files=[]):
    """Returns a long."""
    pass


@opcode(Inst.DRETURN)
def dret(frame, class_files=[]):
    """Returns a double."""
    pass


@opcode(Inst.ARETURN)
def aret(frame, class_files=[]):
    """Returns a reference from a method."""
    pass


@opcode(Inst.RETURN)
def ret(frame, class_files=[]):
    """Return void from a method."""
    pass


@opcode(Inst.FRETURN)
def fret(frame, class_files=[]):
    """Return a float."""
    pass

