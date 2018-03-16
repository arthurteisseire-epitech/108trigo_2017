import argparse
import sys

def parse_all():
    fun_arr = ["EXP", "COS", "SIN", "COSH", "SINH"]
    if (sys.argv[1] not in fun_arr)
        exit(84)
    nb_ai = len(sys.argv) - 2
    square = sqrt(nb_ai)
    if (square != int(square))
        exit(84)
    parser = argparse.ArgumentParser()
    parser.add_argument("fun", type=float)
    parser.add_argument("ai", type=float, nargs = len(sys.argv) - 2)
    args = parser.parse_args()
    return (args)
