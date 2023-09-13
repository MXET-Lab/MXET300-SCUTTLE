# This program contains functions for logging robot parameters to local
# files. The files can be accessed by NodeRed or other programs.
# Nodered can be found by browsing to port 1880 on the shared network AP. ie, 192.168.8.1:1880
# This program works on SCUTTLE with any CPU.

# Import external libraries
import csv      # for handling comma-separated-values file type

# A function for populating 2 text files with updating variables
def logArray(values):                                       # this function takes a 2-element array called val
    txt = open("/home/pi/mxet300_lab/a.txt", 'w+')           # file for generic variable a
    txt2 = open("/home/pi/mxet300_lab/b.txt", 'w+')          # file for generic variable b
    a = round(values[0], 2)
    b = round(values[1], 2)
    txt.write(str(a))
    txt2.write(str(b))
    txt.close()
    txt2.close()

# A function for sending 1 value to a log file of specified name
def uniqueFile(value, fileName):                                    # this function takes a 2-element array called val
    txt = open("/home/pi/mxet300_lab/" + fileName, 'w+')     # file with specified name
    myValue = round(value, 2)
    txt.write(str(myValue))
    txt.close()

# A function for sending 1 value to a log file in a temporary folder
def tmpFile(value, fileName):                               # this function takes a 2-element array called val
    txt = open("/tmp/" + fileName, 'w+')                    # file with specified name
    myValue = round(value, 2)
    txt.write(str(myValue))
    txt.close()
    
# A function for saving a single line string to a log file in a temporary folder
def stringTmpFile(myString, fileName):     # this function takes a string and filename
    txt = open("/tmp/" + fileName, 'w+')   # file with specified name
    txt.write(myString)                    # by default the existing txt is overwritten
    txt.close()

# A function for creating a CSV file from a list of values.
def csv_write(list):
    list = [str(i) for i in list]
    with open('/tmp/excel_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(list)
    csvFile.close()

# A function for creating a row in a csv file
def csv_row(items):
    with open('/tmp/excel_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(items)
    csvFile.close()

# A function to clear an existing CSV file
def clear_file():
    open('/tmp/excel_data.csv', 'w').close()
