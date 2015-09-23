# Place to test and verify new things

# Keyboard input
# There is difference between inut and raw_input
# function.
input = input('Enter a number:')
print input

input = raw_input('Enter a string:')
print input


def sum(a, b):
    return a + b


def another_sum_func(a, b):
    a + b


sum(2, 3)
print 'sum function called !!'
# Following resulted in Traceback:
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# print 'another_sum_func called', another_sum_func(1, 2) + 7

# Testing while with else block
number = 0
while number < 5:
    print "number = {0}".format(number)
    number += 1
else:
    print "number {0} is no longer less than 5".format(number)
