from roundOff import Round_off

def forward_substitution(size, L, B, sig_figs):
    solutions = [0] * size
    for k in range(size):
        sum_of_terms = B[k]
        for i in range(k):
            sum_of_terms -= Round_off(L[k][i] * solutions[i], sig_figs)
        solutions[k] = Round_off(sum_of_terms / L[k][k], sig_figs)
    return solutions