"""These methods work together to determine if any
   read OpCode result is within the valid boundaries of minimum and
   maximum values for the specified data type and if it is not to make it valid."""


def integer_boundaries(op_result):
    """
    Examines a given integer for being in-bounds.

    :param op_result:   The result of an operation.
    :return op_result:  Proper truncated result if applicable.
    """
    if op_result > signed_maxvalue_bitsize(32) or op_result < -signed_maxvalue_bitsize(32):
        return truncate_integers(op_result)
    else:
        return op_result


def truncate_integers(op_result):
    """
    Truncates integers when too large or too small.

    :param op_result:         Integer that needs truncation.
    :return truncated_result: Proper truncated result.
    """
    truncated_result = 0x7FFFFFFF & op_result
    return truncated_result


def long_boundaries(op_result):
    """
    Examines a given long for being in-bounds.

    :param op_result:   The result of an operation.
    :return op_result:  Returns proper truncated result if applicable.
    """
    if op_result > signed_maxvalue_bitsize(64) or op_result < -signed_maxvalue_bitsize(64):
        return truncate_longs(op_result)
    else:
        return op_result


def truncate_longs(op_result):
    """
    Truncates longs when too large or too small.

    :param op_result:         The long that needs truncation.
    :return truncated_result: Returns the proper truncated result.
    """
    truncated_result = 0x7FFFFFFFFFFFFFFF & op_result
    return truncated_result


def float_boundaries(op_result):
    """
    Examines a given float for being in-bounds.

    :param op_result:   The result of an arithmetic operation.
    :return op_result:  Returns proper truncated result if applicable.
    """
    if op_result < 0:
        return float(op_result)
    elif op_result < signed_maxvalue_bitsize(-148):
        return 0.0
    elif op_result > float_max_bitsize(127):
        return float('inf')
    else:
        return float(op_result)


def signed_maxvalue_bitsize(size):
    """
    Returns full signed value.

    :param size:    The given size, i.e. 8, 16, 32, 64, etc.
    :return:        The full signed value.
    """
    return 2**(size - 1)


def float_max_bitsize(size):
    """
    Returns full float singed value.

    :param size:    Given size, i.e. 8, 16, 32, 64, etc.
    :return:        The full float signed value.
    """
    return (2 - (2 ** -23)) * (2 ** size)
