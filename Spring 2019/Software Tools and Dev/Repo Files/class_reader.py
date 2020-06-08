import unittest
from collections import deque
from unittest.mock import mock_open, patch


class ClassFile:
    def __init__(self):
        with open('test.class', 'rb') as binary_file:
            self.data = binary_file.read()

    def get_magic(self):
        magic = ""
        for i in range(4):
            magic += format(self.data[i], '02X')
        return magic

    def get_minor(self):
        return self.data[4] + self.data[5]

    def get_major(self):
        return self.data[6] + self.data[7]

    def get_constant_pool_count(self):
        return self.data[8] + self.data[9]

    def get__access_flags(self):
        return self.data[147] + self.data[148]

    def get_this_class(self):
        return self.data[149] + self.data[150]

    def get_super_class(self):
        return self.data[151] + self.data[152]

    def get_interfaces_count(self):
        return self.data[153] + self.data[154]

    def get_interfaces_table(self):
        return self.data[155] + self.data[156]

    def get_methods_count(self):
        return self.data[160] + self.data[161]

    def get_methods_info(self):
        return self.data[162] + self.data[163] + self.data[164] \
               + self.data[165] + self.data[166] + self.data[167]

    def get_attributes_count(self):
        return self.data[168] + self.data[169]

    def get_attribute_info(self):
        return self.data[170] + self.data[171] + self.data[172] \
               + self.data[173] + self.data[174] + self.data[175]


class OpCodes:
    '''
    First step is to create a table of all the integer
    functions that will be implemented. This serves as a
    jump table to access all the functions in the class.
    '''

    def __init__(self):
        self.stack = deque()
        self.table = {
            0x02: 'i_const_m1',
            0x03: 'i_const_0',
            0x04: 'i_const_1',
            0x05: 'i_const_2',
            0x06: 'i_const_3',
            0x07: 'i_const_4',
            0x08: 'i_const_5',
            0x60: 'i_add',
            0x64: 'i_sub',
            0x68: 'i_mul',
            0x6c: 'i_div',
            0x74: 'i_neg',
            0x70: 'i_rem',
            0x78: 'i_shl',
            0x7a: 'i_shr',
            0x7c: 'i_u_shr',
            0x7e: 'i_and',
            0x80: 'i_or',
            0x82: 'i_xor',
        }

        with open("test.class", 'rb') as binary_file:
            self.data = binary_file.read()
        '''
        These go inside self.table next sprint
        0x2e: self.i_a_load(),
        0x4f: self.i_a_store(),
        0x91: self.i_2b(),
        0x92: self.i_2c(),
        0x87: self.i_2d(),
        0x86: self.i_2f(),
        0x85: self.i_2l(),
        0x93: self.i_2s(),
        0xac: self.i_return(),
        0x15: self.i_load(),
        0x1a: self.i_load_0(),
        0x1b: self.i_load_1(),
        0x1c: self.i_load_2(),
        0x1d: self.i_load_3(),
        0x36: self.i_store(),
        0x3b: self.i_store_0(),
        0x3c: self.i_store_1(),
        0x3d: self.i_store_2(),
        0x3e: self.i_store_3()
        '''

        '''
        The binary file must be read into a table of the
        bytes. From the table the bytes can be read
        starting at the end of header index
        '''

    def read_opcodes(self):
        i = 182
        while i < len(self.data):
            if self.data[i] in self.table:
                self.interpret(self.table[self.data[i]])
            else:
                self.stack.append(self.data[i])
            i += 1

    def not_implemented(self):
        return 'not implemented'

    def interpret(self, value):
        self.table.get(value)

    def read_stack(self):
        return self.stack[len(self.stack)-1]

    '''The following are the operations to load integers -1 - 5 into the stack'''

    def i_const_m1(self):
        self.stack.append(-1)

    def i_const_0(self):
        self.stack.append(0)

    def i_const_1(self):
        self.stack.append(1)

    def i_const_2(self):
        self.stack.append(2)

    def i_const_3(self):
        self.stack.append(3)

    def i_const_4(self):
        self.stack.append(4)

    def i_const_5(self):
        self.stack.append(5)

    '''The following are simple arithmetic operations off the stack'''
    'Addition'

    def i_add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a + b
        self.stack.append(c)


    'Subtraction'

    def i_sub(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = int(b) - int(a)
        self.stack.append(c)

    'Multiplication'

    def i_mul(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a * b
        self.stack.append(c)

    'Division'

    def i_div(self):
        a = self.stack.pop()
        b = self.stack.pop()
        if a != 0:
            c = int(b) / int(a)
            self.stack.append(c)
        else:
            self.stack.append('$')

    'Negation'

    def i_neg(self):
        a = self.stack.pop()
        c = a * -1
        self.stack.append(c)

    'Remainder'

    def i_rem(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = b % a
        self.stack.append(c)

    '''The following are bitwise manipulators'''

    'SHIFT LEFT'

    def i_shl(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = int(b) << int(a)
        self.stack.append(c)

    'SHIFT RIGHT'

    def i_shr(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = int(a) >> int(b)
        self.stack.append(c)

    'LOGICAL SHIFT RIGHT'

    def i_u_shr(self):
        a = self.stack.pop()
        b = self.stack.pop()
        if int(b) >= 0:
            c = int(b) >> int(a)
        else:
            c = (int(b) + 0x100000000) >> int(a)
        self.stack.append(c)

    'AND'

    def i_and(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a & b
        self.stack.append(c)

    'OR'

    def i_or(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = int(a) | int(b)
        self.stack.append(c)

    'EXCLUSIVE OR'

    def i_xor(self):
        a = self.stack.pop()
        b = self.stack.pop()
        c = a + b
        self.stack.append(c)

    '''Below is for next sprint'''


'''
    'load an int from an array'
    def i_a_load (self):
    
    'store an int into an array'
    def i_a_store (self):
    
    'convert an int into a byte'
    def i_2b (self):
    
    'convert an int into a character'
    def i_2c (self):
    
    'convert an int into a double'
    def i_2d (self):
    
    'convert an int into a float'
    def i_2f (self):
    
    'convert an int into a long'
    def i_2l (self):
    
    'convert an int into a short'
    def i_2s (self):
    
    'return an integer from a method'
    def i_return (self):
    
    '-> value'
    def i_load (self):
    
    'load an int value from local variable 0'
    def i_load_0 (self):
    
    'load an int value from local variable 1'
    def i_load_1 (self):
    
    'load an int value from local variable 2'
    def i_load_2 (self):
    
    'load an int value from local variable 3'
    def i_load_3 (self):
    
    'value ->'
    def i_store (self):
    
    'store int value into variable 0'
    def i_store_0 (self):
    
    'store int value into variable 1'
    def i_store_1 (self):
    
    'store int value into variable 2'
    def i_store_2 (self):
    
    'store int value into variable 3'
    def i_store_3 (self):
    
'''


class TestClassFile(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x37\x00\x0f\x0a\x00\x03\x00\x0c\x07\x00\x0d\x07\x0e'
                                b'\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00\x03\x28\x29\x56\x01\x00\x04\x43\x6f'
                                b'\x64\x65\x01\x00\x0f\x4c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x54\x61\x62\x6c\x65'
                                b'\x01\x00\x04\x6d\x61\x69\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x61\x2f\x6c\x61\x6e'
                                b'\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a\x53\x6f\x75\x72\x63\x65'
                                b'\x46\x69\x6c\x65\x01\x00\x09\x74\x65\x73\x74\x2e\x6a\x61\x76\x61\x0c\x00\x04\x00'
                                b'\x05\x01\x00\x04\x74\x65\x73\x74\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67'
                                b'\x2f\x4f\x62\x6a\x65\x63\x74\x00\x20\x00\x02\x00\x03\x00\x00\x00\x00\x00\x02\x00'
                                b'\x00\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00\x1d\x00\x01\x00\x01\x00\x00\x00'
                                b'\x05\x2a\xb7\x00\x01\xb1\x00\x00\x00\x01\x00\x07\x00\x00\x00\x06\x00\x01\x00\x00'
                                b'\x00\x01\x00\x08\x00\x08\x00\x09\x00\x01\x00\x06\x00\x00\x00\x26\x00\x01\x00\x02'
                                b'\x00\x00\x00\x06\x04\x3c\x84\x01\x01\xb1\x00\x00\x00\x01\x00\x07\x00\x00\x00\x0e'
                                b'\x00\x03\x00\x00\x00\x03\x00\x02\x00\x04\x00\x05\x00\x05\x00\x01\x00\x0a\x00\x00'
                                b'\x00\x02\x00\x0b')
        with patch(__name__ + '.open', m):
            self.cf = ClassFile()

    def test_magic(self):
        self.assertEqual(self.cf.get_magic(), 'CAFEBABE')

    def test_minor(self):
        self.assertEqual(self.cf.get_minor(), 0)

    def test_major(self):
        self.assertEqual(self.cf.get_major(), 55)

    def test_constant_pool_count(self):
        self.assertEqual(self.cf.get_constant_pool_count(), 15)

    def test_access_flags(self):
        self.assertEqual(self.cf.get__access_flags(), 32)

    def test_this_class(self):
        self.assertEqual(self.cf.get_this_class(), 2)

    def test_super_class(self):
        self.assertEqual(self.cf.get_super_class(), 3)

    def test_interfaces_count(self):
        self.assertEqual(self.cf.get_interfaces_count(), 0)

    def test_interfaces_table(self):
        self.assertEqual(self.cf.get_interfaces_table(), 0)

    def test_methods_count(self):
        self.assertEqual(self.cf.get_methods_count(), 0)

    def test_methods_info(self):
        self.assertEqual(self.cf.get_methods_info(), 10)

    def test_attributes_count(self):
        self.assertEqual(self.cf.get_attributes_count(), 6)

    def test_attribute_info(self):
        self.assertEqual(self.cf.get_attribute_info(), 30)


class TestOpcodes(unittest.TestCase):

    def setUp(self):
        m = mock_open(read_data=b'\xCA\xFE\xBA\xBE\x00\x00\x00\x37\x00\x0f\x0a\x00\x03\x00\x0c\x07\x00\x0d\x07\x0e'
                                b'\x01\x00\x06\x3c\x69\x6e\x69\x74\x3e\x01\x00\x03\x28\x29\x56\x01\x00\x04\x43\x6f'
                                b'\x64\x65\x01\x00\x0f\x4c\x69\x6e\x65\x4e\x75\x6d\x62\x65\x72\x54\x61\x62\x6c\x65'
                                b'\x01\x00\x04\x6d\x61\x69\x6e\x01\x00\x16\x28\x5b\x4c\x6a\x61\x61\x2f\x6c\x61\x6e'
                                b'\x67\x2f\x53\x74\x72\x69\x6e\x67\x3b\x29\x56\x01\x00\x0a\x53\x6f\x75\x72\x63\x65'
                                b'\x46\x69\x6c\x65\x01\x00\x09\x74\x65\x73\x74\x2e\x6a\x61\x76\x61\x0c\x00\x04\x00'
                                b'\x05\x01\x00\x04\x74\x65\x73\x74\x01\x00\x10\x6a\x61\x76\x61\x2f\x6c\x61\x6e\x67'
                                b'\x2f\x4f\x62\x6a\x65\x63\x74\x00\x20\x00\x02\x00\x03\x00\x00\x00\x00\x00\x02\x00'
                                b'\x00\x00\x04\x00\x05\x00\x01\x00\x06\x00\x00\x00\x1d\x00\x01\x00\x01\x00\x00\x00'
                                b'\x05\x2a\xb7\x00\x01\xb1\x00\x00\x00\x01\x00\x07\x00\x00\x00\x06\x00\x01\x00\x00'
                                b'\x00\x01\x00\x08\x00\x08\x00\x09\x00\x01\x00\x06\x00\x00\x00\x26\x00\x01\x00\x02'
                                b'\x00\x00\x00\x06\x04\x3c\x84\x01\x01\xb1\x00\x00\x00\x01\x00\x07\x00\x00\x00\x0e'
                                b'\x00\x03\x00\x00\x00\x03\x00\x02\x00\x04\x00\x05\x00\x05\x00\x01\x00\x0a\x00\x00'
                                b'\x00\x02\x00\x0b')
        with patch(__name__ + '.open', m):
            self.op = OpCodes()
        self.op.read_opcodes()

    'Begin integer operations'

    def test_i_shl(self):
        self.assertEqual(self.op.read_stack(), 0x78)

    def test_i_shr(self):
        self.assertEqual(self.op.read_stack(), 0x7a)

    def test_i_u_shr(self):
        self.assertEqual(self.op.read_stack(), 0x7c)

    def test_i_and(self):
        self.assertEqual(self.op.read_stack(), 0x7e)

    def test_i_or(self):
        self.assertEqual(self.op.read_stack(), 0x80)

    def test_i_xor(self):
        self.assertEqual(self.op.read_stack(), 0x82)

    def test_i_const_m1(self):
        self.op.i_const_m1()
        test = self.op.stack.pop()
        self.assertEqual(test, -1)

    def test_i_const_0(self):
        self.op.i_const_0()
        test = self.op.stack.pop()
        self.assertEqual(test, 0)

    def test_i_const_1(self):
        self.op.i_const_1()
        test = self.op.stack.pop()
        self.assertEqual(test, 1)

    def test_i_const_2(self):
        self.op.i_const_2()
        test = self.op.stack.pop()
        self.assertEqual(test, 2)

    def test_i_const_3(self):
        self.op.i_const_3()
        test = self.op.stack.pop()
        self.assertEqual(test, 3)

    def test_i_const_4(self):
        self.op.i_const_4()
        test = self.op.stack.pop()
        self.assertEqual(test, 4)

    def test_i_const_5(self):
        self.op.i_const_5()
        test = self.op.stack.pop()
        self.assertEqual(test, 5)

    def test_i_add(self):
        self.op.stack.append(256)
        self.op.stack.append(256)
        self.op.i_add()
        self.assertEqual(self.op.stack.pop(), 512)
        self.op.stack.append(1)
        self.op.stack.append(1023)
        self.op.i_add()
        self.assertEqual(self.op.stack.pop(), 1024)
        self.op.stack.append(1)
        self.op.stack.append(-1)
        self.op.i_add()
        self.assertEqual(self.op.stack.pop(), 0)
        self.op.stack.append(-128)
        self.op.stack.append(-256)
        self.op.i_add()
        self.assertEqual(self.op.stack.pop(), -384)

    def test_i_sub(self):
        self.assertEqual(self.op.read_stack(), 0x64)

    def test_i_div(self):
        self.op.stack.append(10)
        self.op.stack.append(5)
        self.op.i_div()
        self.assertEqual(self.op.stack.pop(), 2)
        self.op.stack.append(0)
        self.op.stack.append(4)
        self.op.i_div()
        self.assertEqual(self.op.stack.pop(), 0)
        self.op.stack.append(30)
        self.op.stack.append(-15)
        self.op.i_div()
        self.assertEqual(self.op.stack.pop(), -2)
        self.op.stack.append(1)
        self.op.stack.append(0)
        self.op.i_div()
        self.assertEqual(self.op.stack.pop(), '$')

    def test_i_mul(self):
        self.assertEqual(self.op.read_stack(), 0x68)

    def test_i_neg(self):
        self.assertEqual(self.op.read_stack(), 0x74)

    def test_i_rem(self):
        self.assertEqual(self.op.read_stack(), 0x70)

    ''''Begin next sprint operations'''


'''
        'load an int from an array'
        test_i_a_load(self)
        self.assertEqual(self.op.read_stack(), 0)

        'store an int into an array'
        test_i_a_store(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a byte'
        test_i_2b(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a character'
        test_i_2c(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a double'
        test_i_2d(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a float'
        test_i_2f(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a long'
        test_i_2l(self)
        self.assertEqual(self.op.read_stack(), 0)

        'convert an int into a short'
        test_i_2s(self)
        self.assertEqual(self.op.read_stack(), 0)

        'return an integer from a method'
        test_i_return(self)
        self.assertEqual(self.op.read_stack(), 0)

        '-> value'
        test_i_load(self)
        self.assertEqual(self.op.read_stack(), 0)

        'load an int value from local variable 0'
        test_i_load_0(self)
        self.assertEqual(self.op.read_stack(), 0)

        'load an int value from local variable 1'
        test_i_load_1(self)
        self.assertEqual(self.op.read_stack(), 0)

        'load an int value from local variable 2'
        test_i_load_2(self)
        self.assertEqual(self.op.read_stack(), 0)

        'load an int value from local variable 3'
        test_i_load_3(self)
        self.assertEqual(self.op.read_stack(), 0)

        'value ->'
        test_i_store(self)
        self.assertEqual(self.op.read_stack(), 0)

        'store int value into variable 0'
        test_i_store_0(self)
        self.assertEqual(self.op.read_stack(), 0)

        'store int value into variable 1'
        test_i_store_1(self)
        self.assertEqual(self.op.read_stack(), 0)

        'store int value into variable 2'
        test_i_store_2(self)
        self.assertEqual(self.op.read_stack(), 0)

        'store int value into variable 3'
        test_i_store_3(self)
        self.assertEqual(self.op.read_stack(), 0)
'''


if __name__ == '__main__':
    cf = ClassFile()
    op = OpCodes()
