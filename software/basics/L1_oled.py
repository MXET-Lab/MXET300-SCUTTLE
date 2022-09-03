#!/usr/bin/python3

# L1_oled program for Raspberry Pi, used in lab 2 exercises. Does not display SSID, for simplicity
# Runs the SSD1306 with I2C and displays a title and IP address that is updated every second
# Before running, make sure to stop the default OLED service with the terminal command: 
#            sudo systemctl stop oled.service

# NOTE!!!
# This code is intended for reference and to demonstrate the the functionality of the OLED display.
# The code temporarily displays on the OLED while it is running and stops displaying when the script
# is terminated. It is not intended to, and should not, replace the oled.py service file for continously
# displaying to the OLED from boot. Please reference and use the oled.py file for this use case.


import board
import digitalio
import netifaces as ni
from time import sleep
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

## Prepare settings and devices ##

# Display Parameters
address = 0x3d                              #I2C address for the display
screenwidth = 128                           #Display screen width in pixels
screenheight = 64                           #Display screen height in pixels
border = 2                                  #Display border in pixels

# Create a display object from the SSD1306_I2C class and call it oled
i2c = board.I2C()
oled_reset = digitalio.DigitalInOut(board.D4)
oled = adafruit_ssd1306.SSD1306_I2C(screenwidth, screenheight, i2c, addr=address, reset=oled_reset)
####


## Functions to get readings for IP and voltage ##

# Get a voltage reading from the INA219
def getVoltage():
    ##########################################
    # Task: Write your own code here to read and return the voltage reading from L1_ina
    #       You must import the necessary python file in order to do this.
    #       Try giving the import an alias similarily done in line 17 above.
    #       This makes it convenient in referencing the import for use.
    
    #       The general format for retrieving the return of a function from another file is:
    #       variable_name = filename_or_alias.function_name()
    #       You can reference lines 31 through 33 as some examples.
    
    #       You should be able to accomplish this task with one line of code.
    ##########################################
    return # Be sure to return your variable name for your getVoltage()

# This function will try to find an IPv4 address from eth0 (ethernet) or wlan0 (wireless), in that order
def getIp():
    for interface in ni.interfaces()[1:]:   #For interfaces eth0 and wlan0
    
        try:
            ip = ni.ifaddresses(interface)[ni.AF_INET][0]['addr']
            return ip
            
        except KeyError:                    #We get a KeyError if the interface does not have the info
            continue                        #Try the next interface since this one has no IPv4
        
    return 'No network found'                        #No interfaces had IPv4, so there's no network available

####


## OLED control functions ##

# Clear the screen by filling it with blank pixels
def clearScreen():
    oled.fill(0)
    oled.show()

# Display some text to the OLED
def displayText():
    ip = getIp()

    image = Image.new("1", (oled.width, oled.height))                       #create a new image to be displayed
    draw = ImageDraw.Draw(image)                                            #create a draw object so text and shapes can be drawn
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)      #draw a blank, filled rectangle the size of the screen to clear it

    font = ImageFont.load_default()                                         #load the default font for text

    #################################################
    # Task: Line 93 will write to the display the robot name specified in the " ". 
    #       Uncomment the line and give it a name of your choice. 
    #       Take notice to the line and understand the format and arguments.
    #################################################
    # draw.text((40, 0), "Robot Name", font=font, fill=255)
    
    # The code in line 96 is drawing the IP text on the image starting at pixel coordinates (0,20) with a default font and no background fill.
    draw.text((0, 20), "IP: " + ip, font=font, fill=255)

    #################################################
    # Task: Write your code here to call getVoltage() to return and add the value to the display.
    #       Use lines 93 and 96 for displaying the robot name and IP to the OLED as a reference guide.
    #       You will draw.text the "Robot Voltage: " starting at pixel coordinates (0,40).
    #       Note that you must convert the voltage float value to a string in order for it to be accepted.
    #       Be sure to include the unit for volts and format the display with a default font and no background fill.
    #################################################

    oled.image(image)                           #set the image to be displayed on the OLED                                        
    oled.show()                                 #show the new image

####


## Only runs if __name__ is __main__, indicating the script was executed directly ##
if __name__ == "__main__":
    clearScreen()                               #clear the screen on startup
    try:
        while True:
            sleep(1)                
            displayText()
            
    finally:
        clearScreen()                           #clear the screen when stopped
