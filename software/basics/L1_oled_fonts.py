#!/usr/bin/python3

# L1_oled program for Raspberry Pi, used in lab 2 exercises.
# Runs the SSD1306 with I2C and displays some text in free sans font
# Before running, make sure to stop the default OLED service with the terminal command: 
#            sudo systemctl stop oled.service

# To restart the default OLED service, run the terminal command: 
#            sudo systemctl restart oled.service


import board
import digitalio
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


## OLED control functions ##

# Clear the screen by filling it with blank pixels
def clearScreen():
    oled.fill(0)
    oled.show()

# Display text block 1 to the OLED
def displayText1():
    image = Image.new("1", (oled.width, oled.height))                       #create a new image to be displayed
    draw = ImageDraw.Draw(image)                                            #create a draw object so text and shapes can be drawn
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)      #draw a blank, filled rectangle the size of the screen to clear it
    
    # Load some fonts: the first is default and the rest are loaded from .ttf files
    # The value is the font size. Default font size cannot be changed.
    default = ImageFont.load_default()
    title = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeSans.ttf',14)
    sans = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeSans.ttf',11)
    sans_bold = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeSansBold.ttf',11)
    
    draw.text((15, 0), "My SCUTTLE", font=title, fill=255)
    draw.text((5, 20), "default", font=default, fill=255)
    draw.text((5, 30), "FreeSans", font=sans, fill=255)
    draw.text((5, 40), "FreeSansBold", font=sans_bold, fill=255)

    oled.image(image)
    oled.show()
####

# Display text block 2 to the OLED
def displayText2():
    image = Image.new("1", (oled.width, oled.height))                       #create a new image to be displayed
    draw = ImageDraw.Draw(image)                                            #create a draw object so text and shapes can be drawn
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)      #draw a blank, filled rectangle the size of the screen to clear it
    
    # The value is the font size. Default font size cannot be changed.
    default = ImageFont.load_default()
    title = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeSans.ttf',14)
    mono = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeMono.ttf',11)
    mono_bold = ImageFont.truetype('/home/pi/MXET300-SCUTTLE/software/fonts/FreeMonoBold.ttf',11)
    
    draw.text((15, 0), "My SCUTTLE", font=title, fill=255)
    draw.text((5, 20), "FreeMono", font=mono, fill=255)
    draw.text((5, 30), "FreeMonoBold", font=mono_bold, fill=255)

    oled.image(image)
    oled.show()
####

## Only runs if our __name__ is __main__, indicating the script was executed directly ##
# By default, the program displays the text and exits, which leaves the text on display until
# another program overwrites the display buffer
if __name__ == "__main__":
    clearScreen()                               #clear the screen on startup
    try:
        while True:
            displayText1()
            sleep(5)
            displayText2()
            sleep(5)
            
    finally:
        clearScreen()                           #clear the screen when stopped