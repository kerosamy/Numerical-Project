import numpy as np
def make_diagonally_dominant(A, B):
    A = np.array(A) 
    B = np.array(B) 
    size = len(A)
    for i in range(size):
        max_row = i
        max_value = abs(A[i][i])
        
        # Check for row with the maximum diagonal value
        for j in range(i + 1, size):
            if abs(A[j][i]) > max_value:
                max_row = j
                max_value = abs(A[j][i])
        
        # Swap rows if necessary
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]  # Swap rows in A
            B[[i, max_row]] = B[[max_row, i]]  # Swap corresponding rows in B
    
    # Verify diagonal dominance
   # Verify diagonal dominance
    strictly_dominant_row_found = False

    for i in range(size):
        row_sum = sum(abs(A[i][j]) for j in range(size) if j != i)
        
        if abs(A[i][i]) > row_sum:
            strictly_dominant_row_found = True  # Found at least one strictly dominant row
        
        if abs(A[i][i]) < row_sum:
            # If any row fails to be weakly dominant, return False immediately
            return False, A, B

    # If no strictly dominant row was found, return False
    if not strictly_dominant_row_found:
        return False, A, B

    # Otherwise, the matrix satisfies the condition
    return True, A, B
    
    return True, A, B