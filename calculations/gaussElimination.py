from Elimination import forward_elimination
from Substitution import back_substitution
from roundOff import Round_off
from solutionType import checkSolutionType
import time


def gauss_elimination(size, A, B, sig_figs):
    start_time = time.time()
    for i in range(size):
        for j in range(size):
                A[i][j] = Round_off(A[i][j], sig_figs)
    for i in range(size):
            B[i] = Round_off(B[i], sig_figs)
    A_transformed, B_transformed, multipliers = forward_elimination(size, A, B, sig_figs)
    solutions = back_substitution(size, A_transformed, B_transformed, sig_figs)        
    end_time = time.time()
    gauss_time = end_time - start_time
    return solutions, gauss_time


if __name__ == "__main__":
    A = [
    [1, 1, 1],
    [1, 1.000001, 1],
    [1, 1, 1.000002]
    ]
    B = [3, 3.000001, 3.000002]
    size = 3
    sig_figs = 8
    solution_type = checkSolutionType(A,B)
    if solution_type == "Unique solution":
      solutions, gauss_time = gauss_elimination(size, A, B, sig_figs)
      print("Solutions:")
      for i, sol in enumerate(solutions):
         print(f"x{i+1} = {sol}")
      print(f"\nGauss Time: {gauss_time:.10f} seconds")