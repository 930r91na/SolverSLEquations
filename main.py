from solution_type import *


def main():
    print("\n------------------- Menu to input a matrix mat_a and its vector b ------------------\n")
    m = int(input("Enter the number of rows/columns for the square matrix mat_a: "))
    mat_a = input_matrix(m, m)
    print("Inputted Matrix mat_a:")
    pprint(Matrix(mat_a))
    b = input_vector(m)
    print("Inputted Vector b:")
    pprint(Matrix(b))
    print(get_solution_type(mat_a, b))


if __name__ == "__main__":
    while True:
        main()

        ent = input("Do you wish to enter another augmented matrix? (Enter 'y' or 'Y' to keep going): ")

        if ent.lower() != 'y':
            break
