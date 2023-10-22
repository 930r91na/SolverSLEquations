import numpy as np
import sympy as sp
from sympy import Matrix, pprint, nsimplify

from solution_infinite import interpret_rref


def get_solution_type(a_mat, b):
    det_a = np.linalg.det(a_mat)
    # Print the determinant of the matrix A
    print ("The determinat of the matrix A is : ", det_a)

    if det_a == 0:
        augmented_a = Matrix(np.column_stack((a_mat, b)))
        augmented_a = augmented_a.applyfunc(lambda x: nsimplify(x, rational=True))

        # Print the augmented matrix
        print("The augmented matrix is: ")
        pprint(augmented_a)

        rref_matrix = augmented_a.rref()[0]

        # Print the reduced row echelon form of the augmented matrix
        print("The reduced row echelon form of the augmented matrix is: ")
        pprint(rref_matrix)

        if all([elem == 0 for elem in rref_matrix[-1, :-1]]) and rref_matrix[-1, -1] != 0:
            return "The system has no solution."
        elif all([elem == 0 for elem in rref_matrix[-1, :]]):
            # interpret_rref(rref_matrix);
            return "The system has infinitely many solutions."
        else:
            return "The situation is ambiguous. Check the coefficient matrix and the independent term vector."
    else:
        x = np.linalg.solve(a_mat, b)
        return f"The system has a unique solution: {x}"


def input_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            while True:
                try:
                    value = float(input(f"Enter the value for row {i + 1}, column {j + 1}: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Please enter a valid number.")
        matrix.append(row)
    return np.array(matrix)


def input_vector(length):
    vector = []
    for i in range(length):
        while True:
            try:
                value = float(input(f"Enter the value for element {i + 1} of the vector  b: "))
                vector.append(value)
                break
            except ValueError:
                print("Please enter a valid number.")
    return np.array(vector)
