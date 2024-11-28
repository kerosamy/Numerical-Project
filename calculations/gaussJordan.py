import time
from jordanForwElim import elimination
from Elimination import backward_elimination
from roundOff import Round_off

def gauss_jordan_elimination(A, B, size, sig_figs):
    start_time = time.time()
    for i in range(size):
        for j in range(size):
            A[i][j] = Round_off(A[i][j], sig_figs)
    for i in range(size):
            B[i] = Round_off(B[i], sig_figs)
    print("Rounded Matrix A:")
    for row in A:
        print(row)
    
    print("Rounded Vector B:")
    print(B)
    matA, matB = elimination( A, B, size, sig_figs)
    print("HII")
    for row in matA:
        print(row)
    print(" Vector B:")
    print(B)
    solutions = backward_elimination(matA, matB, size, sig_figs)
    end_time = time.time()
    jordan_time = end_time - start_time
    return solutions, jordan_time

if __name__ == "__main__":

    A = [
    [5, 10, 15],
    [2,3,5],
    [2,3,4]]
    B = [20,30,40]
    size = 3
    sig_figs = 8
    solutions, jordan_time = gauss_jordan_elimination(A, B, size, sig_figs)

    print("\nSolutions:")
    for i, sol in enumerate(solutions):
        print(f"x{i+1} = {sol}")

    print(f"\nJordan Time: {jordan_time:.10f} seconds")
