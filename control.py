import numpy as np
from phase_1.CheloskyDecomposition import choleskyDecomposition
from phase_1.Crout import croutDecomposition
from phase_1.Doolittle_Working import doolittle_lu_solve
from phase_1.gaussElimination import gauss_elimination
from phase_1.gaussJordan import gauss_jordan_elimination
from phase_1.GaussSeidel import gaussSeidel
from phase_1.Jacobi import jacobiMethod
from phase_2.bisection import bisection_method
from phase_2.false_reguli import regula_falsi_method
from phase_2.fixed_point_iteration import fixed_point_iteration
from phase_2.NewtonRaphson import newton_raphson
from phase_2.ModifiedNewtonRaphson import modified_newton_raphson
from phase_2.Secant import secant_method
from phase_2.ModifiedSecant import modified_secant_method
from phase_2.Secant import secant_method
from phase_2.ModifiedSecant import modified_secant_method



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
     

def choose_the_method_phase_2(method,equation,X0,X1,sig,it=100,r_error=1e-5):
   if method == 'Bisecting':
        return bisection_method(func_str=equation,xl=X0,xu=X1,tol=r_error,max_iter=it,sf=sig)
   elif method == 'Regula_Falsi': 
        return regula_falsi_method(func_str=equation,xl=X0,xu=X1,tol=r_error,max_iter=it,sf=sig)
   elif method == 'Fixed_Point': 
        return fixed_point_iteration(func_str=equation,x0=X0,tol=r_error,max_iter=it,sf=sig)
   elif method == 'Newton_Raphson': 
       return newton_raphson(func=equation,x0=X0,tol=r_error,max_iter=it,sig=sig)     
   elif method == 'Newton_Raphson_Modified': 
       return modified_newton_raphson(func=equation,x0=X0,tol=r_error,max_iter=it,sig=sig)    
   elif method == 'Secant':   
       return secant_method(func=equation, x0=X0, x1=X1, tol=r_error, max_iter=it, sig=sig)
   elif method == 'Modified_Secant':
       return modified_secant_method(func=equation, x0=X0, tol=r_error, max_iter=it, sig=sig)
     