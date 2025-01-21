#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # crée une nouvelle matrice en utilisant une compréhension de liste
    return [[elem ** 2 for elem in row] for row in matrix]
