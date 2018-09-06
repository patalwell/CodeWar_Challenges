"""
Author: Pat Alwell
Date: September 6th, 2018
Instructions:

Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

parse("iiisdoso")  ==>  [8, 64]
"""


def parse(data):

    output_array = []
    value = 0

    for digit in data.lower():

        if digit == 'i':
            value += 1

        if digit == 'd':
            value -= 1

        if digit == 's':
            value = value**2

        if digit == 'o':
            output_array.append(value)

        else:
            pass

    return output_array
