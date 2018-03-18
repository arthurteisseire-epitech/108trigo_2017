from math import sqrt

def print_tab_line(tab):
    line = ""
    for nb in tab:
        if (line != ""):
            line += "\t\t"
        line += str(round(nb, 2))
    print(line)

def print_matrix(matrix):
    for tab in matrix:
        print_tab_line(tab)

def gen_identity_matrix(len):
    matrix = xcreate(len, len)
    i = 0
    while (i < len):
        j = 0
        while (j < len):
            if (i == j):
                matrix[i][j] = 1
            j += 1
        i += 1
        return (matrix)


def xcreate(row_len, col_len):
    matrix = [[0 for row in range(col_len)] for col in range(row_len)]
    return (matrix)

def scale_matrix(A, x):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= x
    return (A)

def div_matrix(A, x):
    return (scale_matrix(A, 1 / x))
    
def matrix_sum(A, row, B, col):
    sum = 0
    for i in range(len(A)):
        sum += A[row][i] * B[i][col]
    return (sum)

def matrix_product(A, B): 
    if (len(A[0]) != len(B)):
        print("INVALID MATRIX DIMENSION")
    row_len = len(A)
    col_len = len(B[0])
    C = [[0 for i in range(col_len)] for i in range(row_len)]
    for row in range(row_len):
        sum_row = 0 
        for col in range(col_len):
            C[row][col] = matrix_sum(A, row, B, col)
    return (C) 

def xcopy(A):
    dim = len(A)
    B = xcreate(dim, dim)
    i = 0
    while (i < dim):
        j = 0
        while (j < dim):
            B[i][j] = A[i][j]
            j += 1
        i += 1
    return (B)

def matrix_sub(A, B):
    dim = len(A)
    C = xcreate(dim, dim)
    i = 0
    while (i < dim):
        j = 0
        while (j < dim):
            C[i][j] = A[i][j] - B[i][j]
            j += 1
        i += 1
    return (C)

def matrix_add(A, B):
    dim = len(A)
    C = xcreate(dim, dim)
    i = 0
    while (i < dim):
        j = 0
        while (j < dim):
            C[i][j] = A[i][j] + B[i][j]
            j += 1
        i += 1
    return (C)

def split_matrix(list):
    xlen = sqrt(len(list))
    matrix = xcreate(int(xlen), int(xlen))
    x = 0
    i = 0
    while (x < xlen):
        y = 0
        while (y < xlen):
            matrix[x][y] = list[i]
            i += 1
            y += 1
        x += 1
    return (matrix)
