"""These three methods works together to build a proper description
   utf8 constants, proper return types, and a clear list of arguments
   from that description."""


def desc_nargs(desc):
    """
    Examines utf8 constants for specific notations.

    :param desc:    String of characters.
    :return i:      Number of characters in desc.
    """
    args = desc.split(')', 2)[0][1:]
    i = 0
    L = False
    for c in args:
        if c == '[':
            continue
        if L:
            if c == ';':
                L = False
            continue
        if c == 'L':
            L = True
        i += 1
    return i


def desc_ret(desc):
    """
    Examines constant pool entries for return types.

    :param desc:    Description of the utf8 constant.
    :return:        String denoting return type.
    """
    if desc.endswith('V'):
        return "void "
    elif desc.endswith('I'):
        return "int "
    else:
        return "sth "


def desc_arg(desc):
    """
    Builds a list of arguments from desc.

    :param desc:    Description of the constant.
    :return args:   List of args as a string.
    """
    args = desc.split(')', 2)[0][1:]
    return '(' + args + ')'
