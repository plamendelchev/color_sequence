#!/usr/bin/env python3

import sys
from collections import deque

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

def find_size(matrix, i, j, is_marked):
    queue = deque()

    key = (i, j)
    is_marked[key] = True
    queue.append(key)

    count = 0

    while queue:
        key_index = queue.popleft()
        count += 1
        i, j = key_index

        key = (i - 1, j)
        if i > 0 and matrix[i - 1][j] == matrix[i][j]:
            if key not in is_marked:
                queue.append(key)
                is_marked[key] = True

        key = (i, j + 1)
        if j + 1 < len(matrix) and matrix[i][j + 1] == matrix[i][j]:
            if key not in is_marked:
                queue.append(key)
                is_marked[key] = True

        key = (i + 1, j)
        if i + 1 < len(matrix) and matrix[i + 1][j] == matrix[i][j]:
            if key not in is_marked:
                queue.append(key)
                is_marked[key] = True

        key = (i, j - 1)
        if j > 0 and matrix[i][j - 1] == matrix[i][j]:
            if key not in is_marked:
                queue.append(key)
                is_marked[key] = True

    return count

if __name__ == '__main__':
    res_size = -1
    is_marked = {}

    args = sys.argv[1:]
    matrix = populate_matrix(args)

    # Find longest adjasent sequence in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            key = (i, j)

            if key not in is_marked:
                s = find_size(matrix, i, j, is_marked)

                if s > res_size:
                    res_size = s

    print(res_size)
