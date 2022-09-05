# this code is intended to be used to create a path utilising inverse kinematics.
# use this code as a template to create pre-determined paths using known forward speed(m/s), turning speed(rad/s), and motion duration(sec) for each motion to create the path

import L1_log as log
import L2_inverse_kinematics as ik
import L2_speed_control as sc
import numpy as np
from time import sleep

# define some variables that can be used to create the path.
# make use of these definitions in the motions list.
pi = np.pi      # utilize the numpy library to define pi
d1 = 0          # distance in meters of segment 1 in the path
d2 = 0          # distance in meters of segment 2 in the path
x_dot = 0     # forward velocity in m/s of SCUTTLE. NOTE that the max velocity of SCUTTLE is 0.4 m/s

# below is a list setup to run through each motion segment to create the path.
# the list elements within each list are in order as follows: forward speed(m/s), turning speed(rad/s), and motion duration(sec)
# enter the forward speed(m/s), turning speed(rad/s), and motion duration(sec) for each motion to create the path
motions = [
    [0.0, 0.0, 0.0],        # Motion 1
    [0.0, 0.0, 0.0],        # Motion 2
    [0.0, 0.0, 0.0],        # Motion 3
]

# iterate through and perform each open loop motion and then wait the specified duration.
for  count, motion in enumerate(motions):
    print("motion: ", count+1, "\t x_dot (m/s):", motion[0], "\t theta_dot (rad/s):", round(motion[1],2), "\t duration (sec):", motion[2])
    wheel_speeds = ik.getPdTargets(motion[:2])          # take the forward speed(m/s) and turning speed(rad/s) and use inverse kinematics to deterimine wheel speeds
    sc.driveOpenLoop(wheel_speeds)                      # tahke the calculated wheel speeds and use them to run the motors
    sleep(motion[2])                                    # wait the motion duration