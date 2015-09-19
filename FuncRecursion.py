# Functions and Recursion


def count_down(n):
    if n == 0:
        print "Blast Off !!"
    else:
        print n
        count_down(n - 1)


def print_lines(n):
    if n > 0:
        print
        print_lines(n - 1)


def Infinite_recursion(n):
    print n
    Infinite_recursion(n + 1)


print_lines(5)
count_down(5)
Infinite_recursion(1)
