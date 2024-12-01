import numpy as np
from CheloskyDecomposition import choleskyDecomposition
from Crout import croutDecomposition
from Doolittle_Working import doolittle_lu_solve
from gaussElimination import gauss_elimination 
from gaussJordan import gauss_jordan_elimination
from GaussSeidel import gaussSeidel
from Jacobi import jacobiMethod


def choose_the_method(method,size,A,B,sig,intial_guess=None,it=None,r_error=None):
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
         if(it==""):
            return  gaussSeidel(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,tolerance=r_error)
         elif(r_error==""):
            return  gaussSeidel(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,max_iterations=it) 
   elif method == 'Jacobi': 
          if(it==""):
            return  jacobiMethod(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,tolerance=r_error)
          elif(r_error==""):
            return  jacobiMethod(A=A,B=B,initial_guess=intial_guess,sig_figs=sig,max_iterations=it) 
