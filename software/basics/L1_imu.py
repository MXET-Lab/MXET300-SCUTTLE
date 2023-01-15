# This code is intended to calculate and print the compass heading based off of the calibrated magnetometer matrix.
# Calibration of the magnetometer is to be done with the "Magnetometer_Compass_Calibration.ipynb" jupyter notebook.

# Import external libraries
import time
import board
import numpy as np
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

    x -= mag_calibration[0]
    y -= mag_calibration[1]
    z -= mag_calibration[2]

    heading = np.degrees(np.arctan2(y,x))-declination_angle         # Calculate the compass heading in degrees

    return heading

if __name__ == "__main__":
    while True:
        print(round(get_heading(),2))           # Print the compasss heading in degrees
        time.sleep(0.1)