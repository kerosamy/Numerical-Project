import numpy as np
import math  
import sympy as sp

def Round_off(x, sf): 
    if(sf=='none'):
        return x
    if x == 0:
        return 0
    sf = int(sf)
    return round(x, sf - int(np.floor(np.log10(abs(x)))) - 1)


def calculate_significant_figures(error,sig):
    if(sig=='none'):
        sig = float('inf')
    if error == 0:
        return float(sig)
    try:
        return min(float(sig), int(-sp.log(2 * error * 100) / sp.log(10)))
    except ValueError:
        return 0 

