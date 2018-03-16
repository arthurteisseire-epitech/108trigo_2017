from math import factorial

fun_arr = ["EXP", "COS", "SIN", "COSH", "SINH"]

def add_matrix(res, curr):

def mult_matrix(curr, matrix):

def ope(fun, res, next, n):
    if fun == "EXP":
        return (expo(res, next))
    else if fun == "COS":
        return (cosi(res, next, n))
    else if fun == "SIN":
        return (sinu(res, next, n))
    else if fun == "COSH":
        return (cosh(res, next, n))
    else if fun == "SINH":
        return (sinh(res, next, n))
    exit(84)

def expo(res, next):
    res = add_matrix(res, next)

def calc(matrix, end, fun):
    n = 0
    res = 0.0
    numerator = [1 for i in matrix [1 for j in matrix[i]]]
    while (n < end):
        numerator = mult_matrix(numerator, matrix)
        curr = numerator / factorial(n)
        res = ope(fun, res, curr, n)
        n += 1
    return (res)
