import numpy as np
from phase_1.CheloskyDecomposition import choleskyDecomposition
from phase_1.Crout import croutDecomposition
from phase_1.Doolittle_Working import doolittle_lu_solve
from phase_1.gaussElimination import gauss_elimination
from phase_1.gaussJordan import gauss_jordan_elimination
from phase_1.GaussSeidel import gaussSeidel
from phase_1.Jacobi import jacobiMethod



def choose_the_method(method,size,A,B,sig,intial_guess=None,it=100,r_error=1e-8):
   if method == 'Gauss Elimination':
        return   gauss_elimination(size,A,B,sig)
   elif method == 'Gauss-Jordan': 
         return  gauss_jordan_elimination(size,A,B,sig) 
   elif method == 'LU DecompositionDoolittle Form': 
         return  doolittle_lu_solve(size,A,B,sig) 
   elif method == 'LU DecompositionCrout Form': 
         return  croutDecomposition(size,A,B,sig)          
   elif method == 'LU DecompositionCholesky Form': 
         return choleskyDecomposition(size,A,B,sig) 
   elif method == 'Gauss-Seidel':   
      return  gaussSeidel(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,tolerance=r_error,max_iterations=it)    
   elif method == 'Jacobi':      
      return  jacobiMethod(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,tolerance=r_error,max_iterations=it)
     
