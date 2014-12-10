# -*- coding: utf-8 -*-
def factorials(n):
    """
    A Recursive Implementation of the Factorial Function
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
    >>>factorials(5)
    120
    """
    if n == 0:
        return 1
    else:
        return n*factorials(n-1)


    