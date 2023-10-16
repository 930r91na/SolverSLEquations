import numpy as np
from sympy import Matrix, pprint

def get_solution_type(A, b):
    detA = np.linalg.det(A)

    if detA == 0:
        augmented_A = Matrix(np.column_stack((A, b)))
        rref_matrix = augmented_A.rref()[0]

        if all([elem == 0 for elem in rref_matrix[-1, :-1]]) and rref_matrix[-1, -1] != 0:
            return "The system has no solution."
        elif all([elem == 0 for elem in rref_matrix[-1, :]]):
            return "The system has infinitely many solutions."
        else:
            return "The situation is ambiguous. Check the coefficient matrix and the independent term vector."
    else:
        x = np.linalg.solve(A, b)
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
                value = float(input(f"Enter the value for element {i + 1} of the vector: "))
                vector.append(value)
                break
            except ValueError:
                print("Please enter a valid number.")
    return np.array(vector)
