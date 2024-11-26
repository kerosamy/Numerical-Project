import numpy as np

def Round_off(x, sf): 
    if x == 0:
        return 0
    return round(x, sf - int(np.floor(np.log10(abs(x)))) - 1)
