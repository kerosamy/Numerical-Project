from phase_1.partialPiv import partial_pivoting
from phase_1.roundOff import Round_off

def elimination(A, B, size, sig_figs):
    for k in range(size):
        partial_pivoting(A, B, size, k)
        pivot = A[k][k]
        if pivot == 0:
            raise ValueError("Matrix is singular")
        for j in range(size): 
            A[k][j] = Round_off(A[k][j]/pivot,sig_figs)
        B[k] = Round_off(B[k]/pivot, sig_figs)
        for i in range(k + 1, size):
            factor = A[i][k]
            A[i][k] = 0.0  #element below the pivot 
            for j in range(k+1, size):  
                A[i][j] = Round_off(A[i][j] - factor * A[k][j],sig_figs)          
            B[i] = Round_off(B[i] - factor * B[k],sig_figs) 
    return A, B

if __name__ == "__main__":
    A = [
    [0.1, 0.2, 0.3],
    [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9]]
    B = [0.6, 1.5, 2.4]
    size = 3
    sig_figs = 8

    
    matA, matB = elimination(A, B, size, sig_figs)

    print("Rounded Matrix A:")
    for row in matA:
        print(row)
    
    print("Rounded Vector B:")
    print(matB)