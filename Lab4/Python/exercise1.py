""" Lab 4 """

import numpy as np
import matplotlib.pyplot as plt
from biopack import integrate, DEFAULT, parse_args
import biolog
from SystemParameters import PendulumParameters
from lab4_pendulum import pendulum_system

DEFAULT["label"] = [r"$\theta$ [rad]", r"$d\theta/dt$ [rad/s]"]


def pendulum_integration(state, time, *args, **kwargs):
    """ Function for system integration """
    biolog.warning(
        "Pendulum equation with spring and damper must be implemented")  # l_S
    return pendulum_system(state[0], state[1], *args, **kwargs)[:, 0]


def exercise1():
    """ Exercise 1  """
    biolog.info("Executing Lab 4 : Exercise 1")
    parameters = PendulumParameters()
    biolog.info(
        "Find more information about Pendulum Parameters in SystemParameters.py")
    biolog.info("Loading default pendulum parameters")
    biolog.info(parameters.showParameters())

    # Simulation Parameters
    t_start = 0.0
    t_stop = 2.0
    dt = 0.001
    biolog.warning("Using large time step dt={}".format(dt))
    time = np.arange(t_start, t_stop, dt)
    x0 = [np.pi/2., 0.0] # x0[0] = initial position in rad, x0[1] = initial velocity

    res = integrate(pendulum_integration, x0, time, args=(parameters,))
    
    res.plot_phase("Phase")
    res.plot_state("State")

    if DEFAULT["save_figures"] is False:
        plt.show()
        font = {'family':'normal', 'weight':'normal', 'size':16}
        plt.rc('font', **font)
        plt.title(" Init_Pos = $\pi/2$, Init_Vel = {}, K1 = {}, K2 = {},\ntheta_ref_1 = {}, theta_ref_2 = {}, B1 = {}, B2 = {}".format(x0[1], parameters.k1,parameters.k2,parameters.s_theta_ref1,parameters.s_theta_ref2, parameters.b1, parameters.b2))
        plt.minorticks_on()
        plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')
        plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    return


if __name__ == '__main__':
    exercise1()

