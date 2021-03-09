#!/usr/bin/env python3

import sys

def populate_matrix(args):
    matrix = []

    ## When no arguments are given
    if not len(args):
        ## Read and validate input
        try:
            rows, cols = [ int(x) for x in input('Please enter the dimensions of the matrix: ').split() ]
        except ValueError:
            raise SystemExit('Please enter two whitespace-separated integers. ')

        ## Populate the matrix from input
        for row in range(rows):
            current_row = input(f'{row} row: ').split()

            if not len(current_row) == cols:
                raise SystemExit(f'Please enter {cols} columns, not {len(current_row)} ')

            matrix.append(current_row)
    ## When the matrix is provided from stdin
    else:
        for file in args:
            with open(file, 'r') as reader:
                for line in reader:
                    matrix.append(line.strip('\n').split())

        rows, cols = [ int(x) for x in matrix[0] ]
        matrix[:] = matrix[1:]

    return matrix

# Function to check if a cell `(i, j)` is valid or not
def is_valid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix)

def find_size(matrix, i, j):
    # if the cell is invalid
    if not is_valid(matrix, i, j):
        return 0

    # construct a unique dictionary key from dynamic elements of the input
    key = (i, j)

    if key not in is_marked:
        is_marked[key] = True
    elif key in is_marked and is_marked[key]:
        return 0
    else:
        is_marked[key] = True

    # string to store size starting `(i, j)`
    size = 0
    temp_size = 0

    # recur top cell if its value is +1 of value at `(i, j)`
    if i > 0 and matrix[i - 1][j] == matrix[i][j]:
        temp_size = find_size(matrix, i - 1, j)
        if temp_size > size:
            size = temp_size

    # recur right cell if its value is +1 of value at `(i, j)`
    if j + 1 < len(matrix) and matrix[i][j + 1] == matrix[i][j]:
        temp_size = find_size(matrix, i, j + 1)
        if temp_size > size:
            size = temp_size

    # recur bottom cell if its value is +1 of value at `(i, j)`
    if i + 1 < len(matrix) and matrix[i + 1][j] == matrix[i][j]:
        temp_size = find_size(matrix, i + 1, j)
        if temp_size > size:
            size = temp_size

    # recur left cell if its value is +1 of value at `(i, j)`
    if j > 0 and matrix[i][j - 1] == matrix[i][j]:
        temp_size = find_size(matrix, i, j - 1)
        if temp_size > size:
            size = temp_size

    is_marked[key] = False
    size += 1

    # return size starting from `(i, j)`
    return size

if __name__ == '__main__':
    res_size = -1
    is_marked = {}

    args = sys.argv[1:]
    matrix = populate_matrix(args)

    # Find longest adjasent sequence in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            s = find_size(matrix, i, j)

            if s > res_size:
                res_size = s

    print(res_size)