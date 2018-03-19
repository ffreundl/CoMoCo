""" Lab 1 - Exercise 2 """

import numpy as np
import matplotlib.pyplot as plt
import sympy

from biopack import integrate, DEFAULT
import biolog


def ode(x, _=None, A=np.eye(2)):
    """ System x_dot = A*x """
    return np.dot(A, x)


def integration(x0, time, A, name, **kwargs):
    """ System integration """
    labels = kwargs.pop("label", ["State {}".format(i) for i in range(2)])
    sys_int = integrate(ode, x0, time, args=(A,))
    sys_int.plot_state("{}_state".format(name), labels)
    sys_int.plot_phase("{}_phase".format(name))
    return


def exercise2():
    """ Exercise 2 """
    biolog.info("Running exercise 2")
    # System definition
    A = np.array([[1, 4], [-4, -2]])
    # system_analysis of the matrix A
    # Solve for the fixed point
    x = sympy.symbols(["x{}".format(i) for i in range(2)]) # used to denominate the x = (x,y) vector just as follow: x = (x[0], x[1])
    sol = sympy.solve(np.dot(A, x), x) # Use solve() to solve algebraic equations. We suppose all equations are equaled to 0, so solving x**2 == 1 translates into the following code: solve(x**2 - 1, x)
    x0 = sol[x[0]], sol[x[1]]
    biolog.info("Fixed point: {}".format(x0))
    # Solve for the eigenvalues/vectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    biolog.info("Eigenvalues: {}".format(eigenvalues))
    biolog.info("Eigenvectors:\n{}".format(eigenvectors))
    time_total = 10
    time_step = 0.01
    # Reset initial conditions in order to display the phase portrait
    x0, time = [0, 1], np.arange(0, time_total, time_step)

    # Normal run
    biolog.info("System integration implemented")
    integration(x0, time, A, "system_integration")

    # Stable point (Optional)
    biolog.info("Stable point integration implemented")
    x0 = [0,0] # calculated by hand
    integration(x0, time, A, "stable") 

    # Periodic
    biolog.info("Periodic system implemented")
    A = np.array([[2,4],[-4,-2]])
    x0 = [1,0]
    integration(x0, time, A, "periodic")

    # Plot
    if DEFAULT["save_figures"] is False:
        plt.show()
    return


if __name__ == "__main__":
    from biopack import parse_args
    parse_args()
    exercise2()