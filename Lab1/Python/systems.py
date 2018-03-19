""" Systems related codes for exercise 2 (Only for corrections) """

import numpy as np
import biolog

try:
    import sympy
    IMPORT_SYMPY = True
except ImportError:
    IMPORT_SYMPY = False


def fixed_point(A):
    """ Compute fixed point """
    x = sympy.symbols(["x{}".format(i) for i in range(2)]) # used to denominate the x = (x,y) vector just as follow: x = (x[0], x[1])
    sol = sympy.solve(np.dot(A, x), x) # Use solve() to solve algebraic equations. We suppose all equations are equaled to 0, so solving x**2 == 1 translates into the following code: solve(x**2 - 1, x)
    x0 = sol[x[0]], sol[x[1]]
    biolog.info("Fixed point: {}".format(x0))
    biolog.info("x is = to: {}".format(x0))
    return


def eigen(A):
    """ Compute eigenvectors and eigenvalues """
    eigenvalues, eigenvectors = np.linalg.eig(A)
    biolog.info("Eigenvalues: {}".format(eigenvalues))
    biolog.info("Eigenvectors:\n{}".format(eigenvectors))
    return eigenvalues, eigenvectors


def system_analysis(A):
    """ Exercise 2.a - Analyse system """
    if IMPORT_SYMPY:
        fixed_point(A)
        eigen(A)
    return
