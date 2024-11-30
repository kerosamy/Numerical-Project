from roundOff import Round_off


def back_substitution(size, A, B, sig_figs):
    solutions = [0] * size    
    for k in range(size - 1, -1, -1):
        if A[k][k] == 0:
            raise ValueError("Division by Zero")
        sum_of_terms = B[k]
        for i in range(k + 1, size):
            sum_of_terms = Round_off(sum_of_terms - A[k][i] * solutions[i], sig_figs)
        solutions[k] = Round_off(sum_of_terms / A[k][k], sig_figs)
    return solutions

def forward_substitution(size, L, B, sig_figs):
    solutions = [0] * size
    for k in range(size):
        sum_of_terms = B[k]
        for i in range(k):
            sum_of_terms = Round_off(sum_of_terms - L[k][i] * solutions[i], sig_figs)
        pivot = L[k][k]
        if pivot == 0:
            raise ValueError("Zero pivot")
        
        solutions[k] = Round_off(sum_of_terms / L[k][k], sig_figs)
    return solutions
if __name__ == "__main__":
   L = [
    [0, 0, 0],
    [4, 3, 0],
    [6, 5, 1]
   ]

   B  = [10, 20, 30]
   size = 3
   sig_figs = 8

   solutions = forward_substitution(size, L, B, sig_figs)
   print("Solutions:", solutions)

