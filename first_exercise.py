#!/usr/bin/env python3

# Read and validate input
try:
    rows, cols = [ int(x) for x in input('Please enter the dimensions of the matrix: ').split() ]
except ValueError:
    raise SystemExit('Please enter two whitespace-separated integers. ')

# Create an empty list to store the matrix
matrix = []

# Populate the matrix from input
for row in range(rows):
    current_row = [ int(x) for x in input(f'{row} row: ').split() ]

    if not len(current_row) == cols:
        raise SystemExit(f'Please enter {cols} columns, not {len(current_row)} ')

    matrix.append(current_row)

print(matrix)
