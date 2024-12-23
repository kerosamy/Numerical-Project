import numpy as np
import math  

def Round_off(x, sf): 
    if(sf=='none'):
        return x
    if x == 0:
        return 0
    sf = int(sf)
    return round(x, sf - int(np.floor(np.log10(abs(x)))) - 1)



def calculate_significant_figures(error):
    if error == 0:
        return float('inf')  # Infinite significant figures if no error
    try:
        return max(0, int(-math.log10(error)))  # Ensure the result is non-negative
    except ValueError:
        return 0  # In case of a math domain error (if error > 1 or error < 0)

