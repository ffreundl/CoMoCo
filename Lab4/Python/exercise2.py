""" Lab 4 - Exercise 2 """

import numpy as np
import matplotlib.pyplot as plt
from biopack import integrate, DEFAULT, parse_args
from biopack.plot import save_figure
from SystemParameters import MuscleParameters, MassParameters
from lab4_mass import mass_system
import biolog
from scipy.integrate import odeint
# Import muscule model
import Muscle

DEFAULT["label"] = [r"$\theta$ [rad]", r"$d\theta/dt$ [rad/s]"]

# Global settings for plotting
# You may change as per your requirement
plt.rc('lines', linewidth=2.0)
plt.rc('font', size=12.0)
plt.rc('axes', titlesize=14.0)     # fontsize of the axes title
plt.rc('axes', labelsize=14.0)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=14.0)    # fontsize of the tick labels
plt.rc('ytick', labelsize=14.0)    # fontsize of the tick labels


def mass_integration(state, time, *args):
    """ Function to integrate muscle-mass system """
    force = args[0]
    mass_parameters = args[1]
    return mass_system(state[0], state[1], force, mass_parameters)


def muscle_integrate(muscle, deltaLength, activation=0.05, dt=0.001):
    """ Function steps or integrates the muscle model by the specified time_step
    dt.

    Parameters:
    -----
        muscle : <Muscle>
            Instance of Muscle class
        deltaLength : float
            Change in Muscle Tendon Length
        activation : float
            Activation of the muscle
        dt : float
            Time step to integrate (Good value is 0.001)

    Returns:
    --------
        res : dict

        res['l_CE'] :
            Contracticle element length
        res['v_CE'] :
            Contracticle element velocity
        res['l_MTC'] :
            Length of muscle tendon unit
        res['activeForce'] :
            Contracticle element force
        res['passiveForce'] :
            Passive element force
        res['force'] :
            activeForce + passiveForce
        res['tendonForce'] :
            Muscle tendon Force

    Example:
    ========
         >>> res = muscle_integrate(muscle, deltaLength=0.0, activation=0.05,
                                    dt=0.01)
    """
    muscle.stim = activation
    muscle.deltaLength = deltaLength
    muscle.step(dt)
    res = {}
    res['l_CE'] = muscle.l_CE
    res['v_CE'] = muscle.v_CE
    res['l_MTC'] = muscle.l_MTC
    res['activeForce'] = muscle.activeForce
    res['passiveForce'] = muscle.passiveForce
    res['force'] = muscle.force
    res['tendonForce'] = muscle.tendonForce
    return res


def isometric_contraction(muscle, stretch=np.arange(0.0, 0.05, 0.01),
                          activation=0.05):
    """ This function implements the isometric contraction
    of the muscle.

    Parameters:
    -----------
        muscle : <Muscle>
            Instance of Muscle class
        stretch : list/array
            A list/array of muscle stretches to be evaluated
        activation : float
            Muscle activation

    Returns:
    -------
    """
    stretch = np.array(stretch)

    biolog.warning('Exercise 2b isotonic contraction to be implemented')

    # Time settings
    t_start = 0.0  # Start time
    t_stop = 0.2  # Stop time
    dt = 0.001  # Time step

    biolog.warning("Muscle Isometric exercise not implemented")
    return None


def isotonic_contraction(muscle, load=np.arange(1., 100, 10),
                         muscle_parameters=MuscleParameters(),
                         mass_parameters=MassParameters()):
    """ This function implements the isotonic contraction
    of the muscle.

    Parameters:
    -----------
        muscle : <Muscle>
            Instance of Muscle class
        load : list/array
            External load to be applied on the muscle.
            It is the mass suspended by the muscle
        muscle_parameters : MuscleParameters
            Muscle paramters instance
        mass_paramters : MassParameters
            Mass parameters instance


    Since the muscle model is complex and sensitive to integration,
    use the following example as a hint to complete your implementation.

    Example:
    --------

    >>> for load_ in load:
    >>>    # Iterate over the different muscle stretch values
    >>>    mass_parameters.mass = load_ # Set the mass applied on the muscle
    >>>    state = np.copy(x0) # Reset the state for next iteration
    >>>    for time_ in time:
    >>>         # Integrate for 0.2 seconds
    >>>        # Integration before the quick release
    >>>        res = muscle_integrate(muscle, state[0], activation=1.0, dt)
    >>>    for time_ in time:
    >>>        # Quick Release experiment
    >>>        # Integrate the mass system by applying the muscle force on to it
    >>>        for a time step dt
    >>>             mass_res = odeint(mass_integration, state,  [
    >>>             time_, time_ + dt], args=(muscle.force, load_, mass_parameters))
    >>>             state[0] = mass_res[-1, 0] # Update state with final postion of
    >>>             mass
    >>>             state[1] = mass_res[-1, 1] # Update state with final position of
    >>>             velocity
    >>>        # Now update the muscle model with new position of mass
    >>>        res = muscle_integrate(muscle, state[0], 1.0, dt)
    >>>        # Save the relevant data
    >>>        res_[id] = res['v_CE']
    >>>        if(res['l_MTC'] > muscle_parameters.l_opt + muscle_parameters.l_slack):
    >>>             velocity_ce[idx] = min(res_[:])
    >>>         else:
    >>>             velocity_ce[idx] = max(res_[:])

    """
    load = np.array(load)

    biolog.warning('Exercise 2b isotonic contraction to be implemented')

    # Time settings
    t_start = 0.0  # Start time
    t_stop = 0.2  # Stop time
    dt = 0.001  # Time step

    x0 = np.array([0.0, 0.0])  # Initial state of the muscle

    return None


def exercise2a():
    """ Exercise 2a
    The goal of this exercise is to understand the relationship
    between muscle length and tension.
    Here you will re-create the isometric muscle contraction experiment.
    To do so, you will have to keep the muscle at a constant length and
    observe the force while stimulating the muscle at a constant activation."""

    # Defination of muscles
    parameters = MuscleParameters()
    biolog.warning("Loading default muscle parameters")
    biolog.info(parameters.showParameters())

    # Create muscle object
    muscle = Muscle.Muscle(parameters)

    biolog.warning("Isometric muscle contraction to be implemented")

    """ Example for plotting graphs using matplotlib. """
    # plt.figure('fig_name')
    # plt.plot(x, y)
    # plt.plot(x1, y1)
    # plt.title('plot_title')
    # plt.xlabel('x-label')
    # plt.ylabel('y-label')
    # plt.legend(('legend'))
    # plt.grid()
    # save_figure('fig_name')


def exercise2b():
    """ Exercise 2b
    Under isotonic conditions external load is kept constant.
    A constant stimulation is applied and then suddenly the muscle
    is allowed contract. The instantaneous velocity at which the muscle
    contracts is of our interest"""

    # Defination of muscles
    muscle_parameters = MuscleParameters()
    print(muscle_parameters.showParameters())

    mass_parameters = MassParameters()
    print(mass_parameters.showParameters())

    # Create muscle object
    muscle = Muscle.Muscle(muscle_parameters)

    biolog.warning("Isotonic muscle contraction to be implemented")


def exercise2():
    """ Exercise 2 """
    exercise2a()
    exercise2b()


if __name__ == '__main__':
    exercise2()

