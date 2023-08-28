#!/usr/bin/python3
# raise an exception with a message


def raise_exception_msg(message):
    raise NameError(message)

# Example usage:
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
