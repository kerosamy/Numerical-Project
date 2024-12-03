import numpy as np 

def checkSolutionType(A, B):
    if len(A) != len(B):
        raise ValueError("Matrix A and vector B must have the same number of rows.")
    
    A = np.array(A)
    B = np.array(B)
    augmented_matrix = np.hstack([A, B.reshape(-1, 1)])  
    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(augmented_matrix)
    size = A.shape[1]
    
    if rank_A < rank_augmented:
        return "No solution"
    elif rank_A == rank_augmented and rank_A < size:
        return "Infinite solutions"
    elif rank_A == size:
        return "Unique solution"
    else:
        return "Invalid case"
