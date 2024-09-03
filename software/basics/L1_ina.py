# This basic code samples voltage and uses auto-ranging.
# WARNING: configure ina sensor for address 0x44. Encoder occupies 0x40.

import time                 # for keeping time
from adafruit_ina219 import INA219
import board

# Set up the INA219 sensor
i2c = board.I2C()
ina219 = INA219(i2c, 0x44)

def read():
    bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
    shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
    current = ina219.current  # current in mA
    power = ina219.power  # power in watts

    # INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
    print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
    print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
    print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
    print("Shunt Current  : {:7.4f}  A".format(current / 1000))
    print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
    print("Power Register : {:6.3f}   W".format(power))
    print("")

    # Check internal calculations haven't overflowed (doesn't detect ADC overflows)
    if ina219.overflow:
        # Current out of device range with specified shunt resistor
        print("Internal Math Overflow Detected!")
        print("")

def readVolts():
    battery_voltage = ina219.bus_voltage + ina219.shunt_voltage
    volts = round(battery_voltage, 2)
    return volts


if __name__ == "__main__":
    read()
    while True:
        myBatt = readVolts()                            # collect a reading
        print("Battery Voltage: %6.2f   V" % myBatt)    # print the reading
        time.sleep(1)                                   # pause
