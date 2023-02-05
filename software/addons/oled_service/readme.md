Default Python script for running OLED and its service for executing on startup.

The script should be placed in: /usr/share/pyshared/ 
This ensures the display runs properly if the workspace is deleted for some reason.
It requires ina219.py, which is included, in the same directory to run the current sensor.

The service file goes in directory: /lib/systemd/system/ 

* Use the command 'sudo systemctl daemon-reload' to register the changes. 
* Use the command 'sudo systemctl status oled.service' to check the status of your service. 
* Use the command 'sudo systemctl enable oled.service' to enable your service on every reboot. 
