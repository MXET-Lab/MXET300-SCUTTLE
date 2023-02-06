# This program is used to enter the calibrated magnetometer matrix into "mag_calibration" in line 24. 
# Do so after calibrating the magnetometer using the "Magnetometer_Compass_Calibration.ipynb" jupyter notebook.
# The calibrated magnetometer values can be found in the output from the fourth cell beginning with "Final calibration in uTesla: [ ]"
# The code will then determine the heading angle of the robot in degrees and print it to the terminal.

# Import libraries
import time
import numpy as np
import board
import adafruit_bno055

i2c = board.I2C()
imu = adafruit_bno055.BNO055_I2C(i2c)
imu.mode = adafruit_bno055.MAGONLY_MODE

# The magnetic declination used to offset the heading for a more accurate true north. 
# A declination of 7 is used for Mid-East Texas.
declination_angle = 7

# Insert the final calibrated magnetometer matrix in line 14 below. This is gathered from the print statement
# in the "Calibrate the Magnetometer" Section of the "Magnetometer_Compass_Calibration.ipynb" jupyter notebook.
# You can copy the matrix out right from the print statement and paste it into the "mag_calibration" list below.
# Place holders of 0.00 have been used for the x,y,z values.
mag_calibration = [0.00, 0.00, 0.00]

def get_heading():
    
    x, y, z = imu.magnetic
    
    if x is not None and y is not None and z is not None: 
        x -= mag_calibration[0]
        y -= mag_calibration[1]
        z -= mag_calibration[2]

        heading = np.degrees(np.arctan2(y,x))-declination_angle         # Calculate the compass heading in degrees
        
    else:
        heading = 0

    return heading

if __name__ == "__main__":
    while True:
        print(round(get_heading(),2))           # Print the compass heading in degrees
        time.sleep(0.1)
