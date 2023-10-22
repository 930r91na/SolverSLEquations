import numpy as np
from sympy import Matrix, pprint, nsimplify


def interpret_rref(rref_matrix):
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

    return solutions
