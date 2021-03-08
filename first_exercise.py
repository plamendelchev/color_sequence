#!/usr/bin/env python3

import sys

## Read and validate input
#try:
    #    rows, cols = [ int(x) for x in input('Please enter the dimensions of the matrix: ').split() ]
    #except ValueError:
        #    raise SystemExit('Please enter two whitespace-separated integers. ')
        #

## Create an empty list to store the matrix
#matrix = []
## Populate the matrix from input
#for row in range(rows):
    #    current_row = input(f'{row} row: ').split()
    #
    #    if not len(current_row) == cols:
        #        raise SystemExit(f'Please enter {cols} columns, not {len(current_row)} ')
        #
        #    matrix.append(current_row)
        #
        #print(matrix)

args = sys.argv[1:]
matrix = []

if not len(args):
    sys.exit('mitko')

for file in args:
    with open(file, 'r') as reader:
        for line in reader:
            matrix.append(line.strip('\n').split())

rows, cols = [ int(x) for x in matrix[0] ]
matrix[:] = matrix[1:]

######

# Function to check if a cell `(i, j)` is valid or not
def is_valid(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix)

def find_size(matrix, i, j):
    # if the cell is invalid
    if not is_valid(matrix, i, j):
        return None

    # construct a unique dictionary key from dynamic elements of the input
    key = (i, j)

    if key not in is_marked:
        is_marked[key] = True
    else:
        return

    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:

        # string to store size starting `(i, j)`
        size = 0
        temp_size = 0

        # recur top cell if its value is +1 of value at `(i, j)`
        if i > 0 and matrix[i - 1][j] == matrix[i][j]:
            size = find_size(matrix, i - 1, j)
            if not size:
                size = 0

        # recur right cell if its value is +1 of value at `(i, j)`
        if j + 1 < len(matrix) and matrix[i][j + 1] == matrix[i][j]:
            temp_size = find_size(matrix, i, j + 1)
            if temp_size:
                if temp_size > size:
                    size = temp_size

        # recur bottom cell if its value is +1 of value at `(i, j)`
        if i + 1 < len(matrix) and matrix[i + 1][j] == matrix[i][j]:
            temp_size = find_size(matrix, i + 1, j)
            if temp_size:
                if temp_size > size:
                    size = temp_size

        # recur left cell if its value is +1 of value at `(i, j)`
        if j > 0 and matrix[i][j - 1] == matrix[i][j]:
            temp_size = find_size(matrix, i, j - 1)
            if temp_size:
                if temp_size > size:
                    size = temp_size

        # note that as the matrix contains all distinct elements,
        # there is only one size possible from the current cell

        is_marked[key] = False
        lookup[key] = size + 1 if size else 1
    else:
        # recur top cell if its value is +1 of value at `(i, j)`
        if i > 0 and matrix[i - 1][j] == matrix[i][j]:
            temp_size = find_size(matrix, i - 1, j)
            if temp_size:
                if temp_size > size:
                    size = temp_size

        # recur left cell if its value is +1 of value at `(i, j)`
        if j > 0 and matrix[i][j - 1] == matrix[i][j]:
            temp_size = find_size(matrix, i, j - 1)
            if temp_size:
                if temp_size > size:
                    size = temp_size

        is_marked[key] = False
        lookup[key] = size + 1 if size else 1

    # return size starting from `(i, j)`
    return lookup[key]

lookup = {}
is_marked = {}
res_size = -1

# Find longest adjasent sequence in matrix
for i in range(len(matrix)):
    for j in range(len(matrix)):

        s = find_size(matrix, i, j)

        if s:
            if s > res_size:
                res_size = s

print(res_size)
