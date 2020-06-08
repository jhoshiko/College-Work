#!/usr/bin/env python3

import unittest
import sys
import os
from pyjvm.classfile import ClassFile
from pyjvm.machine import Machine
from pyjvm.javalib.loader import load_javalib_classes
from pyjvm.checkbounds import *
from pyjvm.cpool import ConstantPool
from pyjvm.reader import Reader
from pyjvm.opcodes import OpCode
from unittest.mock import patch


class JVMTest(unittest.TestCase):

    def setUp(self):
        self.jvm = Machine()
        load_javalib_classes(self.jvm)
        self.jvm.load_class_file('example/Test.class')

    def test_return0(self):
        self.assertEqual(self.jvm.call_function('Test/return0'), 0)

    def test_return42(self):
        self.assertEqual(self.jvm.call_function('Test/return42'), 42)

    def test_iadd(self):
        self.assertEqual(self.jvm.call_function('Test/iadd', 7, 8), 15)

    def test_isub(self):
        self.assertEqual(self.jvm.call_function('Test/isub', 15, 8), 7)

    def test_imul(self):
        self.assertEqual(self.jvm.call_function('Test/imul', 7, 8), 56)

    def test_print(self):
        self.assertEqual(self.jvm.call_function('Test/print5'), 0)

    def test_iconst(self):
        self.assertEqual(self.jvm.call_function('Test/iconst_m1'), -1)
        self.assertEqual(self.jvm.call_function('Test/iconst_1'), 1)
        self.assertEqual(self.jvm.call_function('Test/iconst_2'), 2)
        self.assertEqual(self.jvm.call_function('Test/iconst_3'), 3)
        self.assertEqual(self.jvm.call_function('Test/iconst_4'), 4)

    def test_istore(self):
        self.assertEqual(self.jvm.call_function('Test/istore'), 6)

    def test_iload(self):
        self.assertEqual(self.jvm.call_function('Test/iload'), 35)

    def test_astore_aload_0(self):
        self.assertEqual(self.jvm.call_function('Test/astore_aload_0'), 'hi')

    def test_astore_aload_1(self):
        self.assertEqual(self.jvm.call_function('Test/astore_aload_1'), 'bye')

    def test_astore_aload_2(self):
        self.assertEqual(self.jvm.call_function('Test/astore_aload_2'), 'NO!')

    def test_astore_aload_3(self):
        self.assertEqual(self.jvm.call_function('Test/astore_aload_3'), 'YES!')

    def test_i2l(self):
        self.assertEqual(self.jvm.call_function('Test/i2l'), 20)

    def test_i2c(self):
        self.assertEqual(self.jvm.call_function('Test/i2c'), 'a')

    def test_i2s(self):
        self.assertEqual(self.jvm.call_function('Test/i2s'), 10 & 0xffff)

    def test_i2b(self):
        self.assertEqual(self.jvm.call_function('Test/i2b'), bytes([4 & 0xff]))

    def test_lstore(self):
        self.assertEqual(self.jvm.call_function('Test/lstore'), 1)

    def test_i2f(self):
        self.assertEqual(self.jvm.call_function('Test/i2f'), None)

    def test_intLdc(self):
        self.assertEqual(self.jvm.call_function('Test/intLdc'), 120000)

    def test_dconst_0(self):
        self.assertEqual(self.jvm.call_function('Test/dconst_0'), 0)
        
    def test_dconst_1(self):
        self.assertEqual(self.jvm.call_function('Test/dconst_1'), 1)

    def test_freturn(self):
        self.assertEqual(self.jvm.call_function('Test/fReturn'), 0.0)

    def test_fstore_fload_0(self):
        self.assertEqual(self.jvm.call_function('Test/fstore_fload_0'), 0.0)

    def test_fstore_fload_1(self):
        self.assertEqual(self.jvm.call_function('Test/fstore_fload_1'), 1.0)

    def test_fstore_fload_2(self):
        self.assertEqual(self.jvm.call_function('Test/fstore_fload_2'), 2.0)

    def test_fstore_fload_3(self):
        self.assertEqual(self.jvm.call_function('Test/fstore_fload_3'), 3.0)

    def test_f2i(self):
        self.assertEqual(self.jvm.call_function('Test/f2i'), 10)

    def test_f2l(self):
        self.assertEqual(self.jvm.call_function('Test/f2l'), 10.0)

    def test_fadd(self):
        self.assertEqual(self.jvm.call_function('Test/fadd'), 15.0)

    def test_fdiv(self):
        self.assertEqual(self.jvm.call_function('Test/fdiv'), 2.0)

    def test_fmul(self):
        self.assertEqual(self.jvm.call_function('Test/fmul'), 50.0)

    def test_frem(self):
        self.assertEqual(self.jvm.call_function('Test/frem'), 3.0)

    def test_fsub(self):
        self.assertEqual(self.jvm.call_function('Test/fsub'), 5.0)

    def test_fneg(self):
        self.assertEqual(self.jvm.call_function('Test/fneg'), -10.0)

    def test_lreturn(self):
        self.assertEqual(self.jvm.call_function('Test/lReturn'), 0.0)

    def test_lstore_lload_0(self):
        self.assertEqual(self.jvm.call_function('Test/lstore_lload_0'), 0.0)

    def test_lstore_lload_1(self):
        self.assertEqual(self.jvm.call_function('Test/lstore_lload_1'), 1.0)

    def test_lstore_lload_2(self):
        self.assertEqual(self.jvm.call_function('Test/lstore_lload_2'), 2.0)

    def test_lstore_lload_3(self):
        self.assertEqual(self.jvm.call_function('Test/lstore_lload_3'), 3.0)

    def test_l2i(self):
        self.assertEqual(self.jvm.call_function('Test/l2i'), 10)

    def test_l2f(self):
        self.assertEqual(self.jvm.call_function('Test/l2f'), 10.0)

    def test_ladd(self):
        self.assertEqual(self.jvm.call_function('Test/ladd'), 15.0)

    def test_ldiv(self):
        self.assertEqual(self.jvm.call_function('Test/ldiv'), 2.0)

    def test_lmul(self):
        self.assertEqual(self.jvm.call_function('Test/lmul'), 50.0)

    def test_lrem(self):
        self.assertEqual(self.jvm.call_function('Test/lrem'), 3.0)

    def test_lsub(self):
        self.assertEqual(self.jvm.call_function('Test/lsub'), 5.0)

    def test_lneg(self):
        self.assertEqual(self.jvm.call_function('Test/lneg', 10), -10)

    def test_land(self):
        self.assertEqual(self.jvm.call_function('Test/land', 15.0, 10.0), 10.0)

    def test_lor(self):
        self.assertEqual(self.jvm.call_function('Test/lor', 15, 10), 15)

    def test_lxor(self):
        self.assertEqual(self.jvm.call_function('Test/lxor', 15.0, 10.0), 5.0)

    def test_lshl(self):
        self.assertEqual(self.jvm.call_function('Test/lshl'), 327680.0)

    def test_lshr(self):
        self.assertEqual(self.jvm.call_function('Test/lshr'), 7.0)

    def test_bounds(self):
        self.assertEqual(integer_boundaries(4000000000), 1852516352)
        self.assertEqual(integer_boundaries(-12000000000, ), 884901888)
        self.assertEqual(integer_boundaries(8), 8)
        self.assertEqual(long_boundaries(10000000000000000000), 776627963145224192)
        self.assertEqual(long_boundaries(-10000000000000000000), 8446744073709551616)
        self.assertEqual(long_boundaries(8), 8)
        self.assertEqual(float_boundaries(1.3 * 10**-45), 0.0)
        self.assertEqual(float_boundaries(4.1 * 10**50), float('inf'))
        self.assertEqual(float_boundaries(3.0), 3.0)

    @patch('pyjvm.javalib.inputstream.input', return_value='4')
    def test_classfile(self, value1):
        args = './example/AddTwo.class'
        cf = ClassFile(args)
        self.assertEqual(cf.dump(), None)

        if cf.has_method('main', '([Ljava/lang/String;)V'):
            jvm = Machine()
            jvm.load_class(cf)
            load_javalib_classes(jvm)
            main = '{}/main'.format(cf.name())
            jargs = args
            jvm.call_function(main, jargs)
        else:
            print('error: couldn\'t find main(String[]) in class {}'.format(cf.name()))


if __name__ == '__main__':
    unittest.main()

