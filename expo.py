from math import factorial
from matrix import *

fun_arr = ["EXP", "COS", "SIN", "COSH", "SINH"]

def ope(fun, res, next, n):
    if fun == "EXP":
        return (expo(res, next))
    elif fun == "COS":
        return (cosi(res, next, n))
    elif fun == "SIN":
        return (sinu(res, next, n))
    elif fun == "COSH":
        return (cosh(res, next, n))
    elif fun == "SINH":
        return (sinh(res, next, n))
    exit(84)

def expo(res, next):
    res = matrix_add(res, next)
    return (res)

def cosi(res, next, n):
    if (n % 2 == 0):
        if ((n / 2) % 2 == 0):
            res = matrix_add(res, next)
        else:
            res = matrix_sub(res, next)
    return (res)

def sinu(res, next, n):
    if (n % 2 != 0):
        if (((n - 1) / 2) % 2 == 0):
            res = matrix_add(res, next)
        else:
            res = matrix_sub(res, next)
    return (res)


def cosh(res, next, n):
    if (n % 2 == 0):
        res = matrix_add(res, next)
    return (res)

def sinh(res, next, n):
    if (n % 2 != 0):
        res = matrix_add(res, next)
    return (res)

def calc(matrix, end, fun):
    n = 0
    res = [[0.00 for col in range(len(matrix))] for row in range(len(matrix))]
    numerator = matrix
    while (n < end):
        #print("N^", n)
        if (n == 0):
            numerator = [[1.00 for col in range(len(matrix))] for row in range(len(matrix))]
        elif (n == 1):
            numerator = matrix
        else:
            numerator = matrix_product(numerator, matrix)
        tmp_numerator = xcopy(numerator)
        curr = div_matrix(tmp_numerator, factorial(n))
        #print_matrix(curr)
        res = ope(fun, res, curr, n)
        n += 1
    return (res)
