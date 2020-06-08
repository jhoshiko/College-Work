#!/usr/bin/env python3

import argparse
from pyjvm.machine import Machine
from pyjvm.classfile import ClassFile
from pyjvm.javalib.loader import load_javalib_classes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Java Virtual Machine')
    parser.add_argument('-d', action='store_true', dest='f_dump', default=False, help='dump instead instead of executing')
    parser.add_argument('target', help='target Java class file')
    parser.add_argument('jargs', nargs=argparse.REMAINDER, help='args to be passed to Java program')
    args = parser.parse_args()

    cf = ClassFile(args.target)
    if args.f_dump:
        # cf.dump_cpool()
        cf.dump()
    else:
        if cf.has_method('main', '([Ljava/lang/String;)V'):
            jvm = Machine()
            jvm.load_class(cf)
            load_javalib_classes(jvm)
            main = '{}/main'.format(cf.name())
            jargs = args.jargs
            jvm.call_function(main, jargs)
        else:
            print('error: couldn\'t find main(String[]) in class {}'.format(cf.name()))
