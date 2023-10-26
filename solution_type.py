import numpy as np
from sympy import Matrix, pprint, nsimplify

# from solution_infinite import interpret_rref
def interpret_rref(rref_matrix):
    print ("Hi I am entering the interpretation")
    num_rows, num_cols = rref_matrix.shape
    solutions = []
    free_vars_positions = set(range(num_cols - 1))  # Excluding the constant column

    # Identify pivot variables and remove them from the free_vars_positions set
    for i in range(num_rows):
        row = rref_matrix[i, :]
        leading_entry_index = next((index for index, val in enumerate(row) if val != 0), None)
        if leading_entry_index is not None:  # If there's a leading entry
            free_vars_positions.discard(leading_entry_index)

    # Express solution in terms of free variables
    for i in range(num_rows):
        row = rref_matrix[i, :]
        leading_entry_index = next((index for index, val in enumerate(row) if val != 0), None)

        if leading_entry_index is None:  # All zero row
            continue

        # Construct the expression for the leading variable in terms of free variables
        expression = f"x{leading_entry_index + 1} = "
        for j in free_vars_positions:
            if row[j] != 0:
                expression += f"{-row[j]}x{j + 1} + "
        expression = expression.rstrip(" + ")
        solutions.append(expression)

    for free_var_pos in free_vars_positions:
        solutions.append(f"x{free_var_pos + 1} is a free variable")
    print (solutions)

    return solutions

def get_solution_type(a_mat, b):
    det_a = np.linalg.det(a_mat)
    # Print the determinant of the matrix A
    print("The determinant of the matrix A is : ", det_a)

    if det_a == 0:
        augmented_a = Matrix(np.column_stack((a_mat, b)))
        # To rationalize the augmented matrix (solves the floating point precision problem
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
            interpret_rref(rref_matrix)
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
