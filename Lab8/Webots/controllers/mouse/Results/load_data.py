""" Load results data """

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def load_data():
    """ Load results data """
    time = np.load("time.npy")
    ankle_l_trajectory = np.load("ankle_l_trajectory.npy")
    ankle_r_trajectory = np.load("ankle_r_trajectory.npy")
    foot_l_contact = np.load("foot_l_contact.npy")
    foot_r_contact = np.load("foot_r_contact.npy")
    muscle_lh_activations = np.load("muscle_lh_activations.npy")
    muscle_rh_activations = np.load("muscle_rh_activations.npy")
    muscle_lh_forces = np.load("muscle_lh_forces.npy")
    muscle_rh_forces = np.load("muscle_rh_forces.npy")
    joint_lh_positions = np.load("joint_lh_positions.npy")
    joint_rh_positions = np.load("joint_rh_positions.npy")
    return [time,
            ankle_l_trajectory,
            ankle_r_trajectory,
            foot_l_contact,
            foot_r_contact,
            muscle_lh_activations,
            muscle_rh_activations,
            muscle_lh_forces,
            muscle_rh_forces,
            joint_lh_positions,
            joint_rh_positions]

# Plotting ground contact gait


def y_options(**kwargs):
    """ Return y options """
    y_size = kwargs.pop("y_size", 4)
    y_sep = 1.0 / (y_size + 1)

    def y_pos(y): return (y + (y + 1) * y_sep) / (y_size + 1)

    return y_size, y_sep, y_pos


def add_patch(ax, x, y, **kwargs):
    """ Add patch """
    y_size, y_sep, y_pos = y_options(**kwargs)
    width = kwargs.pop("width", 1)
    height = kwargs.pop("height", y_sep)
    ax.add_patch(
        patches.Rectangle(
            (x, y_pos(y)),
            width,
            height,
            hatch='\\' if (y % 2) else '/'
        )
    )
    return


def plot_gait(time, gait, dt, **kwargs):
    """ Plot gait """
    figurename = kwargs.pop("figurename", "gait")
    fig1 = plt.figure(figurename)
    ax1 = fig1.add_subplot("111", aspect='equal')
    for t, g in enumerate(gait):
        for l, gait_l in enumerate(g):
            if gait_l:
                add_patch(ax1, time[t], l, width=dt, y_size=len(gait[0, :]))
    y_values = kwargs.pop(
        "y_values",
        [
            "Left\nFoot",
            "Right\nFoot",
            "Left\nHand",
            "Right\nHand"
        ][:len(gait[0, :])]
    )
    _, y_sep, y_pos = y_options(y_size=len(gait[0, :]))
    y_axis = [y_pos(y) + 0.5 * y_sep for y in range(4)]
    plt.yticks(y_axis, y_values)
    plt.xlabel("Time [s]")
    plt.ylabel("Gait")
    plt.axis('auto')
    plt.grid(True)
    return


def main():
    """ Main """
    [time,
     ankle_l_trajectory,
     ankle_r_trajectory,
     foot_l_contact,
     foot_r_contact,
     muscle_lh_activations,
     muscle_rh_activations,
     muscle_lh_forces,
     muscle_rh_forces,
     joint_lh_positions,
     joint_rh_positions] = load_data()
################################## 7c ###########################
    
    c = False
    if c == True:
        # Plot joint angles.
        # Feel free to change or use your own plot tools
        legends = ('Left','Right')
        plt.figure('Joint Angles')
        plt.subplot(3,1,1)
        plt.title('Hip Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 0]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 0]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,2)
        plt.title('Knee Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 1]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 1]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,3)
        plt.title('Ankle Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 2]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 2]))
        plt.legend(legends)
        plt.grid('on')
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.xlabel('Time [s]', fontsize = '14')
        
        # Plot muscles activations for left hind limb.
        plt.figure('Muscle Activations for Left Hind Limb (values between 0 and 1)')
        plt.subplot(8,1,1)
        plt.plot(time, muscle_lh_activations[:, 0])
        plt.grid('on')
        plt.ylabel('PMA', fontsize = '14')
        plt.subplot(8,1,2)
        plt.plot(time, muscle_lh_activations[:, 1])
        plt.grid('on')
        plt.ylabel('CF', fontsize = '14')
        plt.subplot(8,1,3)
        plt.plot(time, muscle_lh_activations[:, 2])
        plt.ylabel('SM', fontsize = '14')
        plt.grid('on')
        plt.subplot(8,1,4)
        plt.plot(time, muscle_lh_activations[:, 3])
        plt.ylabel('POP', fontsize = '14')
        plt.grid('on')
        plt.subplot(8,1,5)
        plt.plot(time, muscle_lh_activations[:, 4])
        plt.ylabel('RF', fontsize = '14')
        plt.grid('on')
        plt.subplot(8,1,6)
        plt.plot(time, muscle_lh_activations[:, 5])
        plt.ylabel('TA' , fontsize = '14')
        plt.grid('on')
        plt.subplot(8,1,7)
        plt.plot(time, muscle_lh_activations[:, 6])
        plt.ylabel('SOL', fontsize = '14')
        plt.grid('on')
        plt.subplot(8,1,8)
        plt.plot(time, muscle_lh_activations[:, 7])
        plt.ylabel('LG', fontsize = '14')
        plt.grid('on')
        plt.xlabel('Time [s]', fontsize = '14')
    
        # Plot the ground contact of gait cycle
        contact_data = np.hstack((foot_r_contact, foot_l_contact))
        print(foot_l_contact)
        plot_gait(time, contact_data,  0.01)
        plt.show()


############################ 7d ##################################  
    r = False
    if r == True:
        # Plot joint angles.
        # Feel free to change or use your own plot tools
        legends = ('Left','Right')
        plt.figure('Joint Angles for Uncoupling at Simulation Time = 1.0')
        plt.subplot(3,1,1)
        plt.title('Hip Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 0]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 0]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,2)
        plt.title('Knee Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 1]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 1]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,3)
        plt.title('Ankle Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 2]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 2]))
        plt.legend(legends)
        plt.grid('on')
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.xlabel('Time [s]', fontsize = '14')    
        
        ############################ 7e ##################################  
    legends = ('Left','Right')    
        # For Up or Down hill gait (just change the name in the plot figure title)
    z = False
    if z == True:
        # Plot joint angles.
        # Feel free to change or use your own plot tools
        plt.figure('Uphill walking with an angle of 6 degrees')
        plt.subplot(3,1,1)
        plt.title('Hip Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 0]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 0]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,2)
        plt.title('Knee Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 1]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 1]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,3)
        plt.title('Ankle Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 2]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 2]))
        plt.legend(legends)
        plt.grid('on')
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.xlabel('Time [s]', fontsize = '14')    

        # Plot the ground contact of gait cycle
        contact_data = np.hstack((foot_r_contact, foot_l_contact))
        print(foot_l_contact)
        plot_gait(time, contact_data,  0.01)
        plt.show()
        
    perturbations = False
    if perturbations == True:
        
        # Plots ankles trajectory to assess the perturbations
        plt.figure('Ankle Trajectory With Perturbations')
        plt.plot(time, ankle_l_trajectory[:,1])
        plt.plot(time, ankle_r_trajectory[:,1])
        Y = np.linspace(0, np.max(ankle_l_trajectory[:,1]),np.max(ankle_l_trajectory[:,1]))
        print Y
        X1 = 2.2*(np.ones(np.size(Y)))
        X2 = 8.2*(np.ones(np.size(Y)))
        plt.plot(X1, Y, linestyle = '--', color = 'r')
        plt.plot(X2, Y, linestyle = '--', color = 'r')
        plt.grid('on')
        plt.title('Ankles Trajectory (perturbations at times = 2.2 and 8.2 sec', fontsize='20')
        plt.ylabel('Y-Position [m]', fontsize = '14')
        plt.xlabel('Time [s]', fontsize = '14')    
        plt.legend(legends)
         
        contact_data = np.hstack((foot_r_contact, foot_l_contact))
        print(foot_l_contact)
        plot_gait(time, contact_data,  0.01)
        plt.show()
        
        
############################ 7f ##################################  
    contact_data = np.hstack((foot_r_contact, foot_l_contact))
    print(foot_l_contact)
    plot_gait(time, contact_data,  0.01)
    plt.show() 
       
############################ 7g ##################################    
        # For Up or Down hill gait (just change the name in the plot figure title)
    g = True
    if g == True:
        # Plot joint angles.
        # Feel free to change or use your own plot tools
        plt.figure('Uphill ANKLE = True')
        plt.subplot(3,1,1)
        plt.title('Hip Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 0]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 0]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,2)
        plt.title('Knee Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 1]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 1]))
        plt.legend(legends)
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.grid('on')
        plt.subplot(3,1,3)
        plt.title('Ankle Joint Angle', fontsize='14')
        plt.plot(time, np.rad2deg(joint_lh_positions[:, 2]))
        plt.plot(time, np.rad2deg(joint_rh_positions[:, 2]))
        plt.legend(legends)
        plt.grid('on')
        plt.ylabel('Angle [deg]', fontsize = '14')
        plt.xlabel('Time [s]', fontsize = '14')    

        # Plot the ground contact of gait cycle
        contact_data = np.hstack((foot_r_contact, foot_l_contact))
        print(foot_l_contact)
        plot_gait(time, contact_data,  0.01)
        plt.show()
        
        
        
    return


if __name__ == '__main__':
    main()
