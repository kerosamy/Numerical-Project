from partialPiv import partial_pivoting
from roundOff import Round_off

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
                A[i][j] -= Round_off(factor * A[k][j],sig_figs)          
            B[i] -= Round_off(factor * B[k],sig_figs) 
    return A, B

if __name__ == "__main__":
    A = [
    [1000, 2000, 3000],
    [4000, 5000, 6000],
    [7000, 8000, 9000]]
    B = [6000, 15000, 24000]
    size = 3
    sig_figs = 8

    
    matA, matB = elimination(A, B, size, sig_figs)

    print("Rounded Matrix A:")
    for row in matA:
        print(row)
    
    print("Rounded Vector B:")
    print(matB)
