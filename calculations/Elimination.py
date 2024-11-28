from partialPiv import partial_pivoting
from roundOff import Round_off

def forward_elimination(size, A, B, sig_figs):
    multipliers = []  
    for k in range(size):
        partial_pivoting(A, B, size, k)
        for i in range(k + 1, size):
            if A[k][k] == 0:
                raise ValueError("Zero pivot")
            factor = Round_off(A[i][k] / A[k][k],sig_figs)
            multipliers.append(factor)
            A[i][k] = 0.0  #set element below the pivot to zero 
            for j in range(k+1, size):  
                A[i][j] -= Round_off(factor * A[k][j],sig_figs)          
            B[i] -= Round_off(factor * B[k],sig_figs) 
    return A, B, multipliers


def backward_elimination(A, B, size, sig_figs):
    for k in range(size - 1, -1, -1):
        if A[k][k] == 0:
            raise ValueError("Zero pivot")
        for i in range(k - 1, -1, -1):
            factor = A[i][k]
            A[i][k] = 0.0  #set element above the pivot to zero
            for j in range(k+1,size):
                 A[i][j] = Round_off(A[i][j] - factor * A[k][j], sig_figs)
            B[i] = Round_off(B[i] - factor * B[k], sig_figs)
    return B

if __name__ == "__main__":
    A = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]]
    B = [0.6, 1.5, 2.4]
    size = 3
    sig_figs = 8

    
    matA, matB = backward_elimination(A, B, size, sig_figs)

    for row in matA:
        print(row)
    print(matB)
