import numpy as np
from sympy import Matrix, pprint
from solution_type import *

def main():
    print("Menu to input a matrix A and its vector b")
    m = int(input("Enter the number of rows/columns for the square matrix A: "))
    A = input_matrix(m, m)
    print("Inputted Matrix A:")
    pprint(Matrix(A))
    b = input_vector(m)
    print("Inputted Vector b:")
    pprint(Matrix(b))
    print(get_solution_type(A, b))

if __name__ == "__main__":
    main()



