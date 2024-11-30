import numpy as np

def checkSolutionType(A, B):
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
    
if __name__ == "__main__":
    A = np.array([
    [1, 1, 1],
    [1, 1.000001, 1],
    [1, 1, 1.000002]
    ])
    B = np.array([3, 3.000001, 3.000002])
    size = 3
    sig_figs = 8
    result = checkSolutionType(A, B)
    print(result)