# This progrom is used to enter the calibrated magnitometer matrix into "mag_calibration" in line 16. 
# Do so after calibrating the magnitemeter using the "Magnetometer_Compass_Calibration.ipynb" jupyter notebook.
# The calibrated magnietometer values can be found in the output from the fourth cell beginning with "Final calibration in uTesla: [ ]"
# The code will then determine the heading angle of the robot in degrees and print it to the terminal.

# Import libraries
import time
import numpy as np
import board
import adafruit_bno055

i2c = board.I2C()
imu = adafruit_bno055.BNO055_I2C(i2c)
imu.mode = adafruit_bno055.MAGONLY_MODE

declination_angle = 7           # define the declination angle for the robot's current geographical location

mag_calibration = [52.4375, 4.0, 123.71875]         #note that you need to put in your calibrated magnitamotor matrix

while True:
        
    x, y, z = imu.magnetic

    x -= mag_calibration[0]
    y -= mag_calibration[1]
    z -= mag_calibration[2]
    
    heading = np.arctan2(y,x)
    print(np.degrees(heading)-declination_angle)
    
    time.sleep(0.2)