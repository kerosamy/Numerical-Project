import time
from jordanForwElim import elimination
from Elimination import backward_elimination
from roundOff import Round_off

def gauss_jordan_elimination(size, A, B, sig_figs):
    start_time = time.time()
    for i in range(size):
        for j in range(size):
            A[i][j] = Round_off(A[i][j], sig_figs)
    for i in range(size):
            B[i] = Round_off(B[i], sig_figs)
    matA, matB = elimination( A, B,size, sig_figs)
    solutions = backward_elimination(size, matA, matB, sig_figs)
    end_time = time.time()
    jordan_time = end_time - start_time
    return solutions, jordan_time

if __name__ == "__main__":
    A = [
    [1, 1, 1],
    [1, 1.000001, 1],
    [1, 1, 1.000002]
    ]
    B = [3, 3.000001, 3.000002]
    size = 3
    sig_figs = 8
    solutions, jordan_time = gauss_jordan_elimination(size, A, B, sig_figs)

    print("\nSolutions:")
    for i, sol in enumerate(solutions):
        print(f"x{i+1} = {sol}")

    print(f"\nJordan Time: {jordan_time:.10f} seconds")
