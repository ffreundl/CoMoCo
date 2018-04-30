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
    P_params.L = .5  # To change the default length of the pendulum
    P_params.mass = 5.  # To change the default mass of the pendulum
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
###
########################################## 3a ########################################
#    
#    # Define a huge mass, such that the pendulum goes up to pi/2 and up t -pi/2
#    P_params.mass = 15000.  
#    # Defines 3 different origins and 3 different insertions for each muscle
#    origins1 = [-0.01, -0.05, -0.10, -0.15, -0.2]
#    origins2 = map(lambda x: -(x), origins1)
#    insertions1 = [-0.15, -0.20, -0.25, -0.30]
#    insertions2 = insertions1[:] # Just for visibility
#    legendsertion =np.array(['Insertion at -15 cm', 'Insertion at -20 cm', 'Insertion at -25 cm', 'Insertion at -30 cm'])
#    legleg = np.array(['Insertion at -15 cm', 'Insertion at -15 cm', 'Insertion at -20 cm', 'Insertion at -20 cm', 'Insertion at -25 cm', 'Insertion at -25 cm', 'Insertion at -30 cm', 'Insertion at -30 cm'])
#    cols = ('blue', 'red', 'olive', 'purple')
##    length1 = np.array()
#    
#    for o1,o2 in zip(origins1, origins2):
#        fig, (ax1, ax2) = plt.subplots(1,2, sharex = True)
#        fig.suptitle('Origin of muscles: o1 = {}, o2 = {}'.format(o1,o2), fontsize='26')
#        for i,j in enumerate(insertions1):
#            # Define Muscle Attachment points
#            m1_origin = np.array([o1, 0.0])  # Origin of Muscle 1
#            m1_insertion = np.array([0.0, j])  # Insertion of Muscle 1
#
#            m2_origin = np.array([o2, 0.0])  # Origin of Muscle 2
#            m2_insertion = np.array([0.0, j])  # Insertion of Muscle 2
#
#            # Attach the muscles
#            muscles.attach(np.array([m1_origin, m1_insertion]),
#                           np.array([m2_origin, m2_insertion]))
#
#            # Create a system with Pendulum and Muscles using the System Class
#            # Check System.py for more details on System class
#            sys = System()  # Instantiate a new system
#            sys.add_pendulum_system(pendulum)  # Add the pendulum model to the system
#            sys.add_muscle_system(muscles)  # Add the muscle model to the system
#
#            ##### Time #####
#        
#            dt=0.01
#            t_max = 1.  # Maximum simulation time
#            time = np.arange(0., t_max, dt)  # Time vector
#        
#        
#        
#            ##### Model Initial Conditions #####
#            x0_P = np.array([np.pi/2. - 0.00001,0.])  # Pendulum initial condition
#        
#            # Muscle Model initial condition
#            x0_M = np.array([0., M1.l_CE, 0., M2.l_CE])
#        
#            x0 = np.concatenate((x0_P, x0_M))  # System initial conditions
#        
#            ##### System Simulation #####
#            # For more details on System Simulation check SystemSimulation.py
#            # SystemSimulation is used to initialize the system and integrate
#            # over time
#        
#            sim = SystemSimulation(sys)  # Instantiate Simulation object
#        
#            # Add muscle activations to the simulation
#            # Here you can define your muscle activation vectors
#            # that are time dependent
#            
#            act1=np.ones((len(time),1))*0.05
#            act2=np.ones((len(time),1))*0.05
#        
#            activations = np.hstack((act1, act2))
#            
#            # Method to add the muscle activations to the simulation
#        
#            sim.add_muscle_activations(activations)
#        
#            # Simulate the system for given time
#        
#            sim.initalize_system(x0, time)  # Initialize the system state
#        
#            # Integrate the system for the above initialized state and time
#            sim.simulate()
#        
#            # Obtain the states of the system after integration
#            # res is np.array [time, states]
#            # states vector is in the same order as x0
#            res = sim.results()
#        
#            # In order to obtain internal paramters of the muscle
#            # Check SystemSimulation.py results_muscles() method for more information
#            res_muscles = sim.results_muscles()
#            length1 = np.array(map(lambda x: np.sqrt(o1**2. + j**2. + 2.*o1*j*np.sin(x)), res[:,1])) # muscle 1 length
#            length2 = np.array(map(lambda x: np.sqrt(o2**2. + j**2. + 2.*o2*j*np.sin(x)), res[:,1])) # muscle 2 length
#            # moment arm of muscles calculation
#            h1lambda = np.array(map(lambda x: np.abs(o1)*np.abs(j)*np.cos(x), res[:,1]))
#            h2lambda = np.array(map(lambda x: np.abs(o2)*np.abs(j)*np.cos(x), res[:,1]))
#            h1 = h1lambda/length1
#            h2 = h2lambda/length2
#            # Plotting the result for the current origins
#            ax1.plot(res[:, 1], length1)
#            ax2.plot(res[:, 1], h1)
#            if o1 == -0.1:
#                plt.figure('Muscles\' moment arm for insertions at {} and {}'.format(o1, o2))
#                if j == -0.15:
#                    temp = 0.0
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = ':')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = ':')
#                elif j == -0.2:
#                    temp = 0.3
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = '--')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = '--')
#                elif j == -0.25:
#                    temp = 0.7
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = '-.')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = '-.')
#                else:
#                    temp = 1.0
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0))
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.))
#                plt.legend(legleg)
#                plt.xlabel('Pendulum position [rad]', fontsize = '18')
#                plt.ylabel('Muscle moment arm [m]', fontsize = '18')
#                plt.title('Muscles\' moment arm for insertions at {} and {}.\nRedish = muscle 1 (left), Blueish = muscle 2 (right)'.format(o1, o2), fontsize='26')
#                plt.grid('ON')
#        
#        ax1.legend(legendsertion)
#        ax2.legend(legendsertion)
#        ax1.set_xlabel('Position [rad]', fontsize='18')
#        ax2.set_xlabel('Position [rad]', fontsize='18')
#        ax1.set_ylabel('Muscle length [m]', fontsize='18') # Here we computed length 1 but muscle 2 has the same behaviour for identical params
#        ax2.set_ylabel('Muscle moment arm [m]', fontsize='18')
#        ax1.set_title('Muscle-tendon unit length in terms of pendulum position', fontsize='20')
#        ax2.set_title('Muscle\'s moment arm', fontsize='20')
#        ax1.grid()
#        ax2.grid()
#    
######################################## End OF 3a ######################################## 
##        
########################################## 3b ########################################
#    
#    # Define a huge mass, such that the pendulum goes up to pi/2 and up t -pi/2
#    P_params.mass = 1500.  
#    # Defines 3 different origins and 3 different insertions for each muscle
#    origins1 = [-0.01, -0.05, -0.10, -0.15, -0.2]
#    origins2 = map(lambda x: -(x), origins1)
#    insertions1 = [-0.15, -0.20, -0.25, -0.30]
#    insertions2 = insertions1[:] # Just for visibility
#    legendsertion =np.array(['Insertion at -15 cm', 'Insertion at -20 cm', 'Insertion at -25 cm', 'Insertion at -30 cm'])
#    legleg = np.array(['Insertion at -15 cm', 'Insertion at -15 cm', 'Insertion at -20 cm', 'Insertion at -20 cm', 'Insertion at -25 cm', 'Insertion at -25 cm', 'Insertion at -30 cm', 'Insertion at -30 cm'])
#    cols = ('blue', 'red', 'olive', 'purple')
##    length1 = np.array()
#    
#    for o1,o2 in zip(origins1, origins2):
#        fig, (ax1, ax2) = plt.subplots(1,2, sharex = True)
#        fig.suptitle('Origin of muscles - passive: o1 = {}, o2 = {}'.format(o1,o2), fontsize='26')
#        for i,j in enumerate(insertions1):
#            # Define Muscle Attachment points
#            m1_origin = np.array([o1, 0.0])  # Origin of Muscle 1
#            m1_insertion = np.array([0.0, j])  # Insertion of Muscle 1
#
#            m2_origin = np.array([o2, 0.0])  # Origin of Muscle 2
#            m2_insertion = np.array([0.0, j])  # Insertion of Muscle 2
#
#            # Attach the muscles
#            muscles.attach(np.array([m1_origin, m1_insertion]),
#                           np.array([m2_origin, m2_insertion]))
#
#            # Create a system with Pendulum and Muscles using the System Class
#            # Check System.py for more details on System class
#            sys = System()  # Instantiate a new system
#            sys.add_pendulum_system(pendulum)  # Add the pendulum model to the system
#            sys.add_muscle_system(muscles)  # Add the muscle model to the system
#
#            ##### Time #####
#        
#            dt=0.01
#            t_max = 1.  # Maximum simulation time
#            time = np.arange(0., t_max, dt)  # Time vector
#        
#        
#        
#            ##### Model Initial Conditions #####
#            x0_P = np.array([np.pi/2. - 0.00001,0.])  # Pendulum initial condition
#        
#            # Muscle Model initial condition
#            x0_M = np.array([0., M1.l_CE, 0., M2.l_CE])
#        
#            x0 = np.concatenate((x0_P, x0_M))  # System initial conditions
#        
#            ##### System Simulation #####
#            # For more details on System Simulation check SystemSimulation.py
#            # SystemSimulation is used to initialize the system and integrate
#            # over time
#        
#            sim = SystemSimulation(sys)  # Instantiate Simulation object
#        
#            # Add muscle activations to the simulation
#            # Here you can define your muscle activation vectors
#            # that are time dependent
#            
#            act1=np.ones((len(time),1))*0.00 # Passive muscles, unactivated.
#            act2=np.ones((len(time),1))*0.00
#        
#            activations = np.hstack((act1, act2))
#            
#            # Method to add the muscle activations to the simulation
#        
#            sim.add_muscle_activations(activations)
#        
#            # Simulate the system for given time
#        
#            sim.initalize_system(x0, time)  # Initialize the system state
#        
#            # Integrate the system for the above initialized state and time
#            sim.simulate()
#        
#            # Obtain the states of the system after integration
#            # res is np.array [time, states]
#            # states vector is in the same order as x0
#            res = sim.results()
#        
#            # In order to obtain internal paramters of the muscle
#            # Check SystemSimulation.py results_muscles() method for more information
#            res_muscles = sim.results_muscles()
#            length1 = np.array(map(lambda x: np.sqrt(o1**2. + j**2. + 2.*o1*j*np.sin(x)), res[:,1])) # muscle 1 length
#            length2 = np.array(map(lambda x: np.sqrt(o2**2. + j**2. + 2.*o2*j*np.sin(x)), res[:,1])) # muscle 2 length
#            # moment arm of muscles calculation
#            h1lambda = np.array(map(lambda x: np.abs(o1)*np.abs(j)*np.cos(x), res[:,1]))
#            h2lambda = np.array(map(lambda x: np.abs(o2)*np.abs(j)*np.cos(x), res[:,1]))
#            h1 = h1lambda/length1
#            h2 = h2lambda/length2
#            # Plotting the result for the current origins
#            ax1.plot(res[:, 1], length1)
#            ax2.plot(res[:, 1], h1)
#            if o1 == -0.1:
#                plt.figure('Muscles\' moment arm for insertions at {} and {} - passive'.format(o1, o2))
#                if j == -0.15:
#                    temp = 0.0
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = ':')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = ':')
#                elif j == -0.2:
#                    temp = 0.3
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = '--')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = '--')
#                elif j == -0.25:
#                    temp = 0.7
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0), linestyle = '-.')
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.), linestyle = '-.')
#                else:
#                    temp = 1.0
#                    plt.plot(res[:, 1], h1, color=(1.0, temp, 0.0))
#                    plt.plot(res[:, 1], h2, color=(temp, .5, 1.))
#                plt.legend(legleg)
#                plt.xlabel('Pendulum position [rad]', fontsize = '18')
#                plt.ylabel('Muscle moment arm [m]', fontsize = '18')
#                plt.title('Muscles\' moment arm for insertions at {} and {} - passive.\nRedish = muscle 1 (left), Blueish = muscle 2 (right)'.format(o1, o2), fontsize='26')
#                plt.grid('ON')
#        
#        ax1.legend(legendsertion)
#        ax2.legend(legendsertion)
#        ax1.set_xlabel('Position [rad]', fontsize='18')
#        ax2.set_xlabel('Position [rad]', fontsize='18')
#        ax1.set_ylabel('Muscle length [m]', fontsize='18') # Here we computed length 1 but muscle 2 has the same behaviour for identical params
#        ax2.set_ylabel('Muscle moment arm [m]', fontsize='18')
#        ax1.set_title('Muscle-tendon unit length in terms of pendulum position', fontsize='20')
#        ax2.set_title('Muscle\'s moment arm', fontsize='20')
#        ax1.grid()
#        ax2.grid()
#    
######################################## End OF 3b ######################################## 
######################################## Part 3c,d,e,f ##########################################
    
    LC = True # Limit Cycle ON => LC True, Limit Cyle OFF => LC False

    if LC == True:
        P_params.mass = 10.
    else:
        P_params.mass = 100. 
        
    # For point 3f, we changed max forces up here (line 55 and 57)

    
    # Define Muscle Attachment points
    m1_origin = np.array([-0.17, 0.0])  # Origin of Muscle 1
    m1_insertion = np.array([0.0, -0.17])  # Insertion of Muscle 1

    m2_origin = np.array([0.17, 0.0])  # Origin of Muscle 2
    m2_insertion = np.array([0.0, -0.17])  # Insertion of Muscle 2

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
   
    act1 = np.arange(0.,t_max,dt)
    act2 = np.arange(0.,t_max,dt) 
    
    if LC == True:
        act1=(np.sin(2.*np.pi/t_max*5.*act1)+1.)*.5 # acts = time
        act2=(-np.sin(2.*np.pi/t_max*5.*act2)+1.)*.5 # by increasing frequency, we don't let the time to gravity to make its office and contribute to the system's equilibrium, so the amplitude of the pendulum diminues.
        act1=act1.reshape(len(act1),1)
        act2=act2.reshape(len(act2),1)
    else:
        act1=np.ones((len(time),1))*0.25
        act2=np.ones((len(time),1))*0.25

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
#    plt.title('Pendulum Phase')
    plt.title('Limit cycle behaviour for a max force of {} N'.format(M1.F_max), fontsize = '22')
#    plt.plot(res[:, 1], res[:, 2])
    plt.plot(time, res[:,1])
#    plt.xlabel('Position [rad]')
#    plt.ylabel('Velocity [rad.s]')
    plt.xlabel('Time [s]')
    plt.ylabel('Pendulum position [rad]')
    plt.grid()
    
    # Plotting activation
    legact = ("Muscle 1 - left", "Muscle 2 - right")
    plt.figure('Activations')
#    plt.title('Pendulum Phase')
    plt.title('Muscle activation patterns', fontsize = '22')
#    plt.plot(res[:, 1], res[:, 2])
    plt.plot(time, act1, color='red')
    plt.plot(time, act2, color='green')
#    plt.xlabel('Position [rad]')
#    plt.ylabel('Velocity [rad.s]')
    plt.xlabel('Time [s]')
    plt.ylabel('Activation [-]')
    plt.legend(legact)
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

