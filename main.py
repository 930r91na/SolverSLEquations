import numpy as np
from sympy import Matrix, pprint
from solution_type import *


def main():
    print("Menu to input a matrix mat_a and its vector b")
    m = int(input("Enter the number of rows/columns for the square matrix mat_a: "))
    mat_a = input_matrix(m, m)
    print("Inputted Matrix mat_a:")
    pprint(Matrix(mat_a))
    b = input_vector(m)
    print("Inputted Vector b:")
    pprint(Matrix(b))
    print(get_solution_type(mat_a, b))


if __name__ == "__main__":
    main()
