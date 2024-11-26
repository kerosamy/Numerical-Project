from roundOff import Round_off

def forward_substitution(size, L, B, sig_figs):
    solutions = [0] * size
    for k in range(size):
        sum_of_terms = B[k]
        for i in range(k):
            sum_of_terms -= Round_off(L[k][i] * solutions[i], sig_figs)
        solutions[k] = Round_off(sum_of_terms / L[k][k], sig_figs)
    return solutions
if __name__ == "__main__":
    size = 3
    L = [
        [158, 0, 0],
        [12, 246, 0],
        [47, 2, 12]
    ]
    B = [52, 53, 156]
    sig_figs = 4  
    solutions = forward_substitution(size, L, B, sig_figs)
    print("Solutions:")
    for i, sol in enumerate(solutions):
        print(f"x{i+1} = {sol}")
