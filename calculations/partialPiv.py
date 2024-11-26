def partial_pivoting(A, B, size, k):
    for k in range(size):
        max_row = k
        for i in range(k + 1, size):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i
        if max_row != k:
            A[k], A[max_row] = A[max_row], A[k]
            B[k], B[max_row] = B[max_row], B[k]