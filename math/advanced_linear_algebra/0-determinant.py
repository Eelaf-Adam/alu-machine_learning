#!/usr/bin/env python3
def determinant(matrix):
    # 1. Type validation: ensure it's a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
        
    # 2. Edge case: The list [[]] represents a 0x0 matrix (determinant is 1 by convention)
    if matrix == [[]]:
        return 1
        
    # 3. Square validation: ensure number of rows equals number of columns
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("matrix must be a square matrix")
            
    # 4. Base case for a 1x1 matrix
    if num_rows == 1:
        return matrix[0][0]
        
    # 5. Base case for a 2x2 matrix
    if num_rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
    # 6. Recursive case for N x N matrices using cofactor expansion
    det = 0
    for j in range(num_rows):
        # Create a submatrix by excluding the first row and the current column (j)
        submatrix = [row[:j] + row[j+1:] for row in matrix[1:]]
        
        # Alternating sign (+, -, +, -...)
        sign = (-1) ** j
        
        # Add the cofactor product to the total determinant
        det += sign * matrix[0][j] * determinant(submatrix)
        
    return det
