from math import sqrt

def print_tab_line(tab):
    line = ""
    for nb in tab:
        if (line != ""):
            line += "\t\t"
        line += str(nb)
    print(line)

def print_matrix(matrix):
    for tab in matrix:
        print_tab_line(tab)

def xcreate(row_len, col_len):
    matrix = [[0 for row in range(col_len)] for i in range(row_len)]
    return (matrix)

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
    print_matrix(matrix)
    return (matrix)
