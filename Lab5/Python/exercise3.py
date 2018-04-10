""" Lab 5 Exercise 3

This file implements the pendulum system with two muscles attached

"""

from SystemParameters import PendulumParameters, MuscleParameters
from Muscle import Muscle
import numpy as np
import biolog
from matplotlib import pyplot as plt
from biopack import DEFAULT
from biopack.plot import save_figure
from PendulumSystem import Pendulum
from MuscleSystem import MuscleSytem
from SystemSimulation import SystemSimulation
from SystemAnimation import SystemAnimation
from System import System

# Global settings for plotting
# You may change as per your requirement
plt.rc('lines', linewidth=2.0)
plt.rc('font', size=12.0)
plt.rc('axes', titlesize=14.0)     # fontsize of the axes title
plt.rc('axes', labelsize=14.0)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=14.0)    # fontsize of the tick labels
plt.rc('ytick', labelsize=14.0)    # fontsize of the tick labels

def exercise3():
    """ Main function to run for Exercise 3.

    Parameters
    ----------
        None

    Returns
    -------
        None
    """

    # Define and Setup your pendulum model here
    # Check Pendulum.py for more details on Pendulum class
    P_params = PendulumParameters()  # Instantiate pendulum parameters
    P_params.L = 0.5  # To change the default length of the pendulum
    P_params.mass = 15.  # To change the default mass of the pendulum
    pendulum = Pendulum(P_params)  # Instantiate Pendulum object

    #### CHECK OUT PendulumSystem.py to ADD PERTURBATIONS TO THE MODEL #####

    biolog.info('Pendulum model initialized \n {}'.format(
        pendulum.parameters.showParameters()))

    # Define and Setup your pendulum model here
    # Check MuscleSytem.py for more details on MuscleSytem class
    M1_param = MuscleParameters()  # Instantiate Muscle 1 parameters
    M1_param.f_max = 1500  # To change Muscle 1 max force
    M2_param = MuscleParameters()  # Instantiate Muscle 2 parameters
    M2_param.f_max = 1500  # To change Muscle 2 max force
    M1 = Muscle(M1_param)  # Instantiate Muscle 1 object
    M2 = Muscle(M2_param)  # Instantiate Muscle 2 object
    # Use the MuscleSystem Class to define your muscles in the system
    muscles = MuscleSytem(M1, M2)  # Instantiate Muscle System with two muscles
    biolog.info('Muscle system initialized \n {} \n {}'.format(
        M1.parameters.showParameters(),
        M2.parameters.showParameters()))

######################################### 3a ########################################
    
    # Define a huge mass, such that the pendulum goes up to pi/2 and up t -pi/2
    P_params.mass = 1500.  
    # Defines 3 different origins and 3 different insertions for each muscle
    origins1 = [-0.01, -0.05, -0.10, -0.15, -0.2]
    origins2 = map(lambda x: -(x), origins1)
    insertions1 = [-0.15, -0.20, -0.25, -0.30]
    insertions2 = insertions1[:] # Just for visibility
    legendsertion =np.array(['Insertion at -15 cm', 'Insertion at -20 cm', 'Insertion at -25 cm', 'Insertion at -30 cm'])
    cols = ('blue', 'red', 'olive', 'purple')
#    length1 = np.array()
    
    for o1,o2 in zip(origins1, origins2):
        fig, (ax1, ax2) = plt.subplots(1,2, sharex = True)
        fig.suptitle('Origin of muscles: o1 = {}, o2 = {}'.format(o1,o2))
        for i,j in enumerate(insertions1):
            # Define Muscle Attachment points
            m1_origin = np.array([o1, 0.0])  # Origin of Muscle 1
            m1_insertion = np.array([0.0, j])  # Insertion of Muscle 1

            m2_origin = np.array([o2, 0.0])  # Origin of Muscle 2
            m2_insertion = np.array([0.0, j])  # Insertion of Muscle 2

            # Attach the muscles
            muscles.attach(np.array([m1_origin, m1_insertion]),
                           np.array([m2_origin, m2_insertion]))

            # Create a system with Pendulum and Muscles using the System Class
            # Check System.py for more details on System class
            sys = System()  # Instantiate a new system
            sys.add_pendulum_system(pendulum)  # Add the pendulum model to the system
            sys.add_muscle_system(muscles)  # Add the muscle model to the system

            ##### Time #####
        
            dt=0.01
            t_max = 1.  # Maximum simulation time
            time = np.arange(0., t_max, dt)  # Time vector
        
        
        
            ##### Model Initial Conditions #####
            x0_P = np.array([np.pi/2. - 0.00001,0.])  # Pendulum initial condition
        
            # Muscle Model initial condition
            x0_M = np.array([0., M1.l_CE, 0., M2.l_CE])
        
            x0 = np.concatenate((x0_P, x0_M))  # System initial conditions
        
            ##### System Simulation #####
            # For more details on System Simulation check SystemSimulation.py
            # SystemSimulation is used to initialize the system and integrate
            # over time
        
            sim = SystemSimulation(sys)  # Instantiate Simulation object
        
            # Add muscle activations to the simulation
            # Here you can define your muscle activation vectors
            # that are time dependent
            
            act1=np.ones((len(time),1))*0.05
            act2=np.ones((len(time),1))*0.05
        
            activations = np.hstack((act1, act2))
            
            # Method to add the muscle activations to the simulation
        
            sim.add_muscle_activations(activations)
        
            # Simulate the system for given time
        
            sim.initalize_system(x0, time)  # Initialize the system state
        
            # Integrate the system for the above initialized state and time
            sim.simulate()
        
            # Obtain the states of the system after integration
            # res is np.array [time, states]
            # states vector is in the same order as x0
            res = sim.results()
        
            # In order to obtain internal paramters of the muscle
            # Check SystemSimulation.py results_muscles() method for more information
            res_muscles = sim.results_muscles()
            length1 = np.array(map(lambda x: np.sqrt(o1**2. + j**2. + 2.*o1*j*np.sin(x)), res[:,1])) # muscle 1 length
            # moment arm of muscle 1 calculation
            h1lambda = np.array(map(lambda x: np.abs(o1)*np.abs(j)*np.cos(x), res[:,1]))
            h1 = h1lambda/length1
            # Plotting the result for the current origins
            ax1.plot(res[:, 1], length1)
            ax2.plot(res[:, 1], h1)
        
        ax1.legend(legendsertion)
        ax2.legend(legendsertion)
        ax1.set_xlabel('Position [rad]')
        ax2.set_xlabel('Position [rad]')
        ax1.set_ylabel('Muscle length [m]') # Here we computed length 1 but muscle 2 has the same behaviour for identical params
        ax2.set_ylabel('Muscle moment arm [m]')
        ax1.grid()
        ax2.grid()
    
####################################### End OF 3a ########################################  

    # Reset the mass to a more normal range
    P_params.mass = 15. 
    
    # Define Muscle Attachment points
    m1_origin = np.array([-0.05, 0.0])  # Origin of Muscle 1
    m1_insertion = np.array([0.0, -0.20])  # Insertion of Muscle 1

    m2_origin = np.array([0.05, 0.0])  # Origin of Muscle 2
    m2_insertion = np.array([0.0, -0.20])  # Insertion of Muscle 2

    # Attach the muscles
    muscles.attach(np.array([m1_origin, m1_insertion]),
                   np.array([m2_origin, m2_insertion]))

    # Create a system with Pendulum and Muscles using the System Class
    # Check System.py for more details on System class
    sys = System()  # Instantiate a new system
    sys.add_pendulum_system(pendulum)  # Add the pendulum model to the system
    sys.add_muscle_system(muscles)  # Add the muscle model to the system

    ##### Time #####

    dt=0.01
    t_max = 5.  # Maximum simulation time
    time = np.arange(0., t_max, dt)  # Time vector



    ##### Model Initial Conditions #####
    x0_P = np.array([2*np.pi/6.,0.])  # Pendulum initial condition

    # Muscle Model initial condition
    x0_M = np.array([0., M1.l_CE, 0., M2.l_CE])

    x0 = np.concatenate((x0_P, x0_M))  # System initial conditions

    ##### System Simulation #####
    # For more details on System Simulation check SystemSimulation.py
    # SystemSimulation is used to initialize the system and integrate
    # over time

    sim = SystemSimulation(sys)  # Instantiate Simulation object

    # Add muscle activations to the simulation
    # Here you can define your muscle activation vectors
    # that are time dependent
    
    act1=np.ones((len(time),1))*0.05
    act2=np.ones((len(time),1))*0.05

    activations = np.hstack((act1, act2))
    # Method to add the muscle activations to the simulation

    sim.add_muscle_activations(activations)

    # Simulate the system for given time

    sim.initalize_system(x0, time)  # Initialize the system state

    # Integrate the system for the above initialized state and time
    sim.simulate()

    # Obtain the states of the system after integration
    # res is np.array [time, states]
    # states vector is in the same order as x0
    res = sim.results()

    # In order to obtain internal paramters of the muscle
    # Check SystemSimulation.py results_muscles() method for more information
    res_muscles = sim.results_muscles()

    # Plotting the results
    plt.figure('Pendulum')
    plt.title('Pendulum Phase')
    plt.plot(res[:, 1], res[:, 2])
    plt.xlabel('Position [rad]')
    plt.ylabel('Velocity [rad.s]')
    plt.grid()

    if DEFAULT["save_figures"] is False:
        plt.show()
    else:
        figures = plt.get_figlabels()
        biolog.debug("Saving figures:\n{}".format(figures))
        for fig in figures:
            plt.figure(fig)
            save_figure(fig)
            plt.close(fig)

    # To animate the model, use the SystemAnimation class
    # Pass the res(states) and systems you wish to animate
    simulation = SystemAnimation(res, pendulum, muscles)
    # To start the animation
    simulation.animate()


if __name__ == '__main__':
    exercise3()

