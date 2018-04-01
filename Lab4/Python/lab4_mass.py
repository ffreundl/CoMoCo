""" Force-Velocity Setup """
import numpy as np
import biolog


def mass_equation(pos, vel, force, mass_params):
    """ Mass equation"""
#    biolog.warning("Implement the mass and muscle equation")
    a= -(mass_params.g) + (force/(mass_params.mass)) # returns the acceleration
    return a


def mass_system(pos, vel, force, mass_params):
    """ Muscle-Mass System"""
    return np.array(
        [mass_equation(pos, vel, force, mass_params), vel])  # X point point)

