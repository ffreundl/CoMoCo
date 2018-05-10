""" Load results data """

import numpy as np
from matplotlib import pyplot as plt

def load_data():
    """ Load results data """
    ankle_l_trajectory = np.load("ankle_l_trajectory.npy")
    ankle_r_trajectory = np.load("ankle_r_trajectory.npy")
    return [ankle_l_trajectory, ankle_r_trajectory]

def plots(L, R):
    legs = ("Left ankle", "Right ankle")
    """ Plots the trajectory of both ankles """
    
    # Trajectory on Y-axis
    plt.figure('Ankle trajectory X')
    plt.plot(L[:,0])
    plt.plot(R[:,0])
    plt.title('Ankle Trajectory on X', fontsize = '26')
    plt.xlabel('Time [ms]', fontsize = '20')
    plt.ylabel('Ankle trajectory [-]', fontsize = '20')
    plt.legend(legs, fontsize = '20')
    plt.grid()
    
    # Trajectory on Y-axis
    plt.figure('Ankle trajectory Y')
    plt.plot(L[:,1])
    plt.plot(R[:,1])
    plt.title('Ankle Trajectory on Y', fontsize = '26')
    plt.xlabel('Time [ms]', fontsize = '20')
    plt.ylabel('Ankle trajectory [-]', fontsize = '20')
    plt.legend(legs, fontsize = '20')
    plt.grid()
    
    # Trajectory on Z-axis
    plt.figure('Ankle trajectory Z')
    plt.plot(L[:,2])
    plt.plot(R[:,2])
    plt.title('Ankle Trajectory on Z', fontsize = '26')
    plt.xlabel('Time [ms]', fontsize = '20')
    plt.ylabel('Ankle trajectory [-]', fontsize = '20')
    plt.legend(legs, fontsize = '20')
    plt.grid()
    
    # Trajectory XY
    plt.figure('Ankle bimodal XY')
    plt.plot(L[:,0], L[:,1])
    plt.plot(R[:,0], R[:,1])
    plt.title('Trajectory XY', fontsize = '26')
    plt.xlabel('X [-]', fontsize = '20')
    plt.ylabel('Y [-]', fontsize = '20')
    plt.legend(legs, fontsize = '20')
    plt.grid()
    return


def main():
    """ Main """
    ankle_l_trajectory, ankle_r_trajectory = load_data()
    print("ankle_l_trajectory:\n{}\nankle_r_trajectory:\n{}".format(
        ankle_l_trajectory,
        ankle_r_trajectory
    ))
    plots(ankle_l_trajectory, ankle_r_trajectory)
    return


if __name__ == '__main__':
    main()
