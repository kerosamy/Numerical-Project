from phase_1.roundOff import Round_off
import numpy as np

def createLUCrout(size, A, sig_figs):
    L = np.zeros((size, size))
    U = np.eye(size)

    # Loop through columns
    for j in range(size):
        # Partial pivoting to ensure L[j, j] is not zero
        if abs(A[j, j]) < 1e-10:  # Small threshold to detect near-zero
            for i in range(j + 1, size):
                if abs(A[i, j]) > abs(A[j, j]):
                    A[[j, i]] = A[[i, j]]  # Swap rows in A
                    break

        # Compute the elements of L (below or on the diagonal)
        for i in range(j, size):
            L[i, j] = A[i, j] - sum(
                Round_off(L[i, k] * U[k, j], sig_figs) for k in range(j)
            )
            L[i, j] = Round_off(L[i, j], sig_figs)

        # Compute the elements of U (above the diagonal)
        for i in range(j + 1, size):
            numerator = A[j, i] - sum(
                Round_off(L[j, k] * U[k, i], sig_figs) for k in range(j)
            )
            if L[j, j] == 0:
                raise ValueError("Matrix is singular and cannot be decomposed.")
            U[j, i] = Round_off(numerator / L[j, j], sig_figs)

    return L, U