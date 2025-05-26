import sys
from operations import *

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Error: Two commandline arguments a, b required")
        exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print("Error: Values must be numbers")

    # Add implemented operations
    opers = []
    for oper in opers:
        print(f"Result of {oper.__name__} between a: {a}\
              and b: {b} is = {oper(a, b)}")