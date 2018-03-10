""" Lab 1 - Exercise 1 """

from ex1_functions import function, function_rk, analytic_function
from ex1_integration import (
    example_integrate,
    euler_integrate,
    ode_integrate,
    ode_integrate_rk,
    plot_integration_methods
)
from ex1_errors import compute_error

import numpy as np
import matplotlib.pyplot as plt

import biolog
from biopack import Result, DEFAULT




def exercise1():
    """ Exercise 1 """
    # Setup
    biolog.info("Running exercise 1")

    # Setup
    time_max = 5  # Maximum simulation time
    time_step = 0.2  # Time step for ODE integration in simulation
    x0 = np.array([1.])  # Initial state

    # Integration methods (Exercises 1.a - 1.d)
    biolog.info("Running function integration using different methods")

    # Example
    biolog.debug("Running example plot for integration (remove)")
    example = example_integrate(x0, time_max, time_step)
    example.plot_state(figure="Example", label="Example", marker=".")

    # Analytical (1.a)
    time = np.arange(0, time_max, time_step)  # Time vector
    x_a = analytic_function(time)
    analytical = Result(x_a, time) if x_a is not None else None

    # Euler (1.b)
    euler = euler_integrate(function, x0, time_max, time_step)
    eulerErr = np.zeros(len(analytical.state))
    for i in range(0, len(analytical.state)):
        eulerErr[i] = np.abs(analytical.state[i]-euler.state[i])
    meanEulErr = np.mean(eulerErr)
    stdEulErr = np.std(eulerErr)
    print("The mean and standard deviation of the error between the analytical result and the euler method is: {}, {}".format(meanEulErr, stdEulErr))

    # ODE (1.c)
    ode = ode_integrate(function, x0, time_max, time_step)
    odeErr = np.zeros(len(analytical.state))
    for i in range(0, len(analytical.state)):
        odeErr[i] = np.abs(analytical.state[i]-ode.state[i])
    meanOdeErr = np.mean(odeErr)
    stdOdeErr = np.std(odeErr)
    print("The mean and standard deviation of the error between the analytical result and the Lsoda method is: {}, {}".format(meanOdeErr, stdOdeErr))

    
    # ODE Runge-Kutta (1.c)
    ode_rk = ode_integrate_rk(function_rk, x0, time_max, time_step)
    rkErr = np.zeros(len(analytical.state))
    for i in range(0, len(analytical.state)):
        rkErr[i] = np.abs(analytical.state[i]-ode_rk.state[i])
    meanRkErr = np.mean(rkErr)
    stdRkErr = np.std(rkErr)
    print("The mean and standard deviation of the error between the analytical result and the RK method is: {}, {}".format(meanRkErr, stdRkErr))

    # Plot of the errors
    # Create a new figure window
    plt.figure()
    # Plot time and euler error
    plt.plot(time, eulerErr, label='Euler Integration Error')
    # Plot time and Lsoda error
    plt.plot(time, odeErr, marker = 'o', label='Lsoda Integration Error')
    # Plot time and Lsoda error
    plt.plot(time, rkErr, marker = 'x', label='Runge-Kutta Integration Error')
    # Turn on grid
    plt.grid('on')
    # X axis label
    plt.xlabel('Time')
    # Y axis label
    plt.ylabel('Error')
    # Title of the plot
    plt.title('Error of integration methods compared to the analytical function')
    # Legend of the plot
    plt.legend()
    # Show the figure
    plt.show()
    
    # Plot of the errors for Lsoda and RK alone, since they are not visible on the first plot
    # Create a new figure window
    plt.figure()
    # Plot time and Lsoda error
    plt.plot(time, odeErr, marker = 'o', label='Lsoda Integration Error')
    # Plot time and Lsoda error
    plt.plot(time, rkErr, marker = 'x', label='Runge-Kutta Integration Error')
    # Turn on grid
    plt.grid('on')
    # Transform y scale in logarithmical scale to increase visibility
    plt.yscale('log')
    # X axis label
    plt.xlabel('Time')
    # Y axis label
    plt.ylabel('Error')
    # Title of the plot
    plt.title('Error of integration methods compared to the analytical function')
    # Legend of the plot
    plt.legend()
    # Show the figure
    plt.show()
    
    # Euler with lower time step (1.d)
    biolog.info("Euler with smaller ts implemented")
    euler_time_step = 0.002
    euler_ts_small = (
        euler_integrate(function, x0, time_max, euler_time_step)
        if euler_time_step is not None
        else None
    )
    eulerSTSErr = np.zeros(len(analytical.state))
    for i in range(0, len(analytical.state)):
        eulerSTSErr[i] = np.abs(analytical.state[i]-euler_ts_small.state[i])
    meanEulSTSErr = np.mean(eulerSTSErr)
    stdEulSTSErr = np.std(eulerSTSErr)
    print("The mean and standard deviation of the error between the analytical result and the euler method with a time step of %f is: {}, {}".format(meanEulErr, stdEulErr)) % euler_time_step
    
    # Plot of the errors for Euker with smaller time step and RK alone
    # Create a new figure window
    plt.figure()
    # Plot time and Euler w/ smaller ts error
    plt.plot(time,  eulerSTSErr, color = 'skyblue', label='Euler Integration Error with a time step of %f' % euler_time_step)
    # Plot time and RK error
    plt.plot(time, rkErr, color = 'green', label='Runge-Kutta Integration Error with a time step of %f' % time_step)
    # Turn on grid
    plt.grid('on')
    # Transform y scale in logarithmical scale to increase visibility
    plt.yscale('log')
    # X axis label
    plt.xlabel('Time')
    # Y axis label
    plt.ylabel('Error')
    # Title of the plot
    plt.title('Error of integration methods compared to the analytical function')
    # Legend of the plot
    plt.legend()
    # Show the figure
    plt.show()

    # Plot integration results
    plot_integration_methods(
        analytical=analytical, euler=euler,
        ode=ode, ode_rk=ode_rk, euler_ts_small=euler_ts_small,
        euler_timestep=time_step, euler_timestep_small=euler_time_step
    )

    # Error analysis (Exercise 1.e)
    biolog.warning("Error analysis must be implemented")
    # Here I chose to implement the error in function of the time steps only for RK method, since it is the most accurate method we have.
    dt_list = [1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002]
    compute_error(function_rk, analytic_function, ode_integrate_rk, x0, dt_list)

    # Show plots of all results
    if DEFAULT["save_figures"] is False:
        plt.show()
    return


if __name__ == "__main__":
    from biopack import parse_args
    parse_args()
    exercise1()