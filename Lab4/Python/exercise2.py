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


def isometric_contraction(muscle, stretch=np.arange(-0.05, 0.05, 0.001), # ORIGINAL GOES UP TO 0.05
                          activation = 0.25): # activation original = 0.05
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
    t_stop = 0.25  # Stop time
    dt = 0.0001  # Time step
    timesteps = np.arange(t_start,t_stop,dt) # Useless??
    # Empty vectors for further isometric representations
    Fp = np.zeros(np.size(stretch)) # passive force
    Fa = np.zeros(np.size(stretch)) # active force
    F = np.zeros(np.size(stretch)) # total force
    totLen = np.zeros(np.size(stretch)) # total length of the CONTRACTILE ELEMENT (l_CE + stretch)
    stabs = np.zeros(np.size(timesteps))

    biolog.info("Muscle Isometric implemented")
    for i,s in enumerate(stretch):
        for j,t in enumerate(timesteps):
            effect=muscle_integrate(muscle, s, activation, dt)
            stabs[j]=effect['activeForce']
#        effect=muscle_integrate(muscle, s, activation, dt) 
#        effect=muscle_integrate(muscle, s, activation, dt)    
        Fp[i]=effect['passiveForce']
        Fa[i]=effect['activeForce']
        F[i]=effect['force']
        totLen[i]=effect['l_CE']+s
        #print("Length of the contractile element is: {} \n and its TOTAL length+stretch is: {}".format(effect['l_CE'],totLen[i]))
        #print("LIMIT: {} \n {}".format(muscle.l_MTC-muscle.l_CE, muscle.l_slack))   
    c = np.array([totLen,Fp, Fa, F, timesteps, stabs])
    #print(c)
    return c


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
    >>>    # Iterate over the different muscle load values
    >>>    mass_parameters.mass = load_ # Set the mass applied on the muscle
    >>>    state = np.copy(x0) # Reset the state for next iteration
    >>>    for time_ in time:
    >>>         # Integrate for 0.2 seconds
    >>>        # Integration before the quick release
    >>>        res = muscle_integrate(muscle, state[0], activation=1.0, dt)
    >>>    for time_ in time:
    >>>        # Quick Release experiment
    >>>        # Integrate the mass system by applying the muscle force on to it for a time step dt
    >>>        mass_res = odeint(mass_integration, state,  [
    >>>        time_, time_ + dt], args=(muscle.force, load_, mass_parameters))
    >>>        state[0] = mass_res[-1, 0] # Update state with final postion of mass
    >>>        state[1] = mass_res[-1, 1] # Update state with final position of velocity
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
    t_stop = 0.25  # Stop time
    dt = 0.001  # Time step
    timesteps = np.arange(t_start, t_stop, dt)

    x0 = np.array([0.0, 0.0])  # Initial state of the muscle
    
    # Empty vectors for further isotonic representations
    Fp = np.zeros(np.size(load)) # passive force
    Fa = np.zeros(np.size(load)) # active force
    F = np.zeros(np.size(load)) # total force
    V = np.zeros(np.size(load)) # will contain contractile element's velocity for each loads
    temp = np.zeros(np.size(timesteps)) 
    
    for k,l in enumerate(load):
        mass_parameters.mass = l # Set the mass applied on the muscle
        state = np.copy(x0) # reset the state for next iteration
        for t in timesteps:
            effect=muscle_integrate(muscle, state[0], activation=1.0, dt=dt)
        for j,t in enumerate(timesteps):
            mass_res=odeint(mass_integration, state, [t, t+dt], args=(muscle.force, mass_parameters))
            state[0] = mass_res[-1, 0] # Update state with final postion of mass
            state[1] = mass_res[-1, 1] # Update state with final position of velocity    
            effect=muscle_integrate(muscle, state[0], 1.0, dt)
            temp[j]=effect['v_CE']
        print("\n\n {} \n\n {} \n\n".format(temp, effect['l_MTC']))    
        if(effect['l_MTC'] > muscle_parameters.l_opt + muscle_parameters.l_slack):
            V[k] = min(temp)
        else:
            V[k] = max(temp)
    print(V)
    return V


def exercise2a():
    """ Exercise 2a
    The goal of this exercise is to understand the relationship
    between muscle length and tension.
    Here you will re-create the isometric muscle contraction experiment.
    To do so, you will have to keep the muscle at a constant length and
    observe the force while stimulating the muscle at a constant activation."""

    # Definition of muscles
    parameters = MuscleParameters()
    biolog.warning("Loading default muscle parameters")
    biolog.info(parameters.showParameters())

    # Create muscle object
    muscle = Muscle.Muscle(parameters)
    
    # Isometric contraction, varying the activation between [0-1]
    isoM = isometric_contraction(muscle)
    legend1 = ("Passive Force","Active Force", "Total Force")
    plt.figure('Forces vs Length')
    plt.plot(isoM[0],isoM[1])
    plt.plot(isoM[0],isoM[2])
    plt.plot(isoM[0],isoM[3])
    plt.xlabel('Total length of the contractile element [m]')
    plt.ylabel('Force [N]')
    plt.legend(legend1)
    plt.grid()
    save_figure('F_vs_length')
    
    # Stabilisation has been verified for integrating the muscle for 0.2s. However, to be sure, we integrated it for 0.25s
#    plt.figure("Stab??")
#    plt.plot(isoM[4],isoM[5]) 
    
    # Effect of varying l_opt (fiber length) NOT SURE)
    muscleS=Muscle.Muscle(parameters) # 'short' muscle 
    muscleS.l_opt=0.11 # short fiber length
    muscleL=Muscle.Muscle(parameters) # 'long' muscle
    muscleL.l_opt=0.12 # long fiber length
    isoS = isometric_contraction(muscleS, stretch=np.arange(-0.05, 0.05, 0.001), activation = 0.25)
    isoL = isometric_contraction(muscleL, stretch=np.arange(-0.05, 0.05, 0.001), activation = 0.25)
    legendS = ("Short fibers: {} [m], \n max_total_length: {} [m]".format(muscleS.l_opt, np.max(isoS[0])),"Long fibers: {} [m], \n max_total_length: {} [m]".format(muscleL.l_opt, np.max(isoL[0])))
    plt.figure('Short and Long muscle fibers (l_opt) active force vs length')
    plt.plot((isoS[0])/(np.max(isoS[0])),isoS[2]) # we plot the percentage of total length
    plt.plot((isoL[0])/(np.max(isoL[0])),isoL[2])
    #plt.plot(isoL[0],isoL[2])
    plt.xlabel('Percentage of maximal total length (l_CE + stretching) of the contractile element [m]')
    plt.ylabel('Force [N]')
    plt.legend(legendS)
    plt.grid()
    save_figure('short_vs_long_')
    
    
    # Effect of varying activation (stimulation)
    activations = np.arange(0.0,1.05,0.05)
    max_F_Diff = np.zeros(np.size(activations)) # vectors to assess the evolution of the difference of the maximas of passive and active force
    ratio = np.zeros(np.size(activations)) # to implement the total_force/total_length ratio for every activation value
    plt.figure('Active force vs Length with varying activation time')
    legend2 = list()
    #print(activations)
    for i,a in enumerate(activations):
        muscle1 = Muscle.Muscle(parameters)
        #print("Activation = {} [s]".format(a))
        iso = isometric_contraction(muscle1, activation = a)
        #print("lapin \n {}".format(iso[2]))
        legend2.append("Activation = {} [s]".format(a))
        plt.plot(iso[0],iso[2]) # plot for active force
#        plt.plot(iso[0],iso[3]) # plot for total force
        max_F_Diff[i]=np.abs(np.max(iso[1])-np.max(iso[2]))
        ratio[i]=((np.mean(iso[3]))/(np.mean(iso[0])))/1000
    plt.xlabel('Total length of the contractile element [m]')
    plt.ylabel('Force [N]')
    plt.legend(legend2)
    plt.grid()
    save_figure('F_vs_length')
    
    # Force difference figure
    plt.figure('Difference between the max of the passive and the active force')
    plt.plot(activations, max_F_Diff,  color='black', marker='v', linestyle='dashed', linewidth=1, markersize=5)
    plt.xlabel('Activation value [s]')
    plt.ylabel('Force Difference [N]')
    plt.legend(['$\Delta$'])
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    save_figure('delta_plot')
    
    # Force/length ratio
    plt.figure('Ratio between the total force (active + passive) and the total length of the contractile element')
    plt.plot(activations, ratio,  color='black', marker='v', linestyle='dashed', linewidth=1, markersize=5)
    plt.xlabel('Activation value [s]')
    plt.ylabel('(Total_force/total_length)/1000  [N]/[m]')
    plt.legend(['$Ratio$'])
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    save_figure('ratio_plot')
    
    
    

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
    isoK = isotonic_contraction(muscle)


def exercise2():
    """ Exercise 2 """
#    exercise2a()
    exercise2b()


if __name__ == '__main__':
    exercise2()

