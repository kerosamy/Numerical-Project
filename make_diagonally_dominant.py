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
    for i in range(size):
        if abs(A[i][i]) < sum(abs(A[i][j]) for j in range(size) if j != i):
            return False, A, B
    
    return True, A, B