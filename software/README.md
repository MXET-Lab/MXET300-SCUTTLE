# MXET-300 SCUTTLE Software
This folder contains software geared toward the MXET-300 Mobile Robotics lab. Below are some useful SHELL and Linux commands to know for working in the Linux terminal.
<br>

## SHELL Processes:

### Check if you have a live internet connection
  ```
ping google.com
  ```
  Below is an example of the expected output if connection is live after running the abouve command
  ```
PING google.com (216.58.194.110) 56(84) bytes of data.
64 bytes from dfw06s48-in-f14.1e100.net (216.58.194.110): icmp_seq=1 ttl=55 time                                       =10.5 ms
64 bytes from dfw06s48-in-f14.1e100.net (216.58.194.110): icmp_seq=2 ttl=55 time                                       =16.3 ms
64 bytes from dfw06s48-in-f14.1e100.net (216.58.194.110): icmp_seq=3 ttl=55 time                                       =17.8 ms
64 bytes from dfw06s48-in-f14.1e100.net (216.58.194.110): icmp_seq=4 ttl=55 time                                       =16.5 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 10.521/15.320/17.869/2.835 ms
  ```
<br>

### Clone a github repository to a local device
  ```
git clone THE URL OF REPOSITORY
  ```
  This will copy all of the contents of SCUTTLE repo into a folder called SCUTTLE in the working directory.

<br> 
 
### GitHub - push updates from local to online repository
  ```
git add .
  ```
  This will add your changes to your local git repository's staging area.
  ```
git commit -m "A BRIEF MESSAGE HERE"
  ```
  This will commit your changes to your local git repository with a message describing the commited changes.
  ```
git push
  ```
  This will push the updates from your local repository back to the remote/online repository.

<br>

### GitHub - pull updates from online to local repository
  ```
git pull
  ```
  This will pull updates from online.  If it has conflicts and you want to force it, follow the steps in [this link](https://learn.adafruit.com/an-introduction-to-collaborating-with-version-control/https-credential-caching-and-ssh-keys).

<br>

### Report devices active on the i2c bus
```
sudo i2cdetect -y -r 1
  ```
  The parts of this command are described below:
  ```
  sudo:       Executes the command following as root user
  i2cdetect:  A program to scan an I2C bus for devices
  -y  :       Does not prompt
  -r 1:       I2C bus to read from. Here we read from I2C bus 1.
  ```

<br>
  
### List USB devices connected
  ```
lsusb
  ```
  An example of the output:
  ```
Bus 001 Device 003: ID 2f24:0091
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
  ```

<br>

# Linux Commands:

### File System Navigation and Information

`ls` - **List** - List the files and folders in a directory.<br>
`cd` - **Change Directory** - Move into a folder.<br>
`pwd` - **Print Working Directory** - Prints your current location to the terminal.<br>
`cp` - **Copy** - Copies a file from a location, to a location.<br>
`mv` - **Move** - Moves a file from a location, to a location.<br>
`touch` - **Touch** - Create a file.<br>
`mkdir` - **Make Directory** - Make a directory with given name.<br>
`nano` - File editor.<br>
`cat` - **Concatenate** - Concatenate files and print file contents to the terminal.<br>
`head` - Output the first part of files.<br>
`tail` - Output the last part of files.<br>
`more` - View a file and scroll through it.<br>
`less` - View a file and scroll through it. (Consumes less resources than `more`)<br>
`rm` - **Remove** - Remove files or directories.<br>
`rmdir` - **Remove Directory** - Remove empty directories.<br>
`file` - Determine file type.<br>

### System and User Info

`whoami` - **Who Am I?** - Print current user.<br>
`date` - Print or set the system date and time.<br>
`df` - Report file system disk space usage.<br>
`which` - Locate a command.<br>
`whereis` - Locate the binary, source, and manual page files for a command.<br>

### Searching

`grep` - Print lines that match patterns.<br>
`locate` - Find files by name.<br>

### Administrator

`sudo` - **Superuser Do** - Execute a command as root(superuser).<br>
`sudo su` - Switch to the root user.<br>

### Modify Permissions

`chown` - **Change Owner** - Change ownership of a file.<br>
`chmod` - **Change Mode** - Change file mode bits.<br>

### Network Information

`ping` - Send ICMP ECHO_REQUEST to network hosts.<br>
`ifconfig` - Configure a network interface.<br>
`iwconfig` - Configure a wireless network interface.<br>
`connmanctl` - **Connection Manager** - WiFi connection Utility.<br>

### Web Tools

`wget` - **Web Get** - Get a file from a server.<br>

### Process Management and Resource Monitoring

`top` - Display Linux processes & CPU (processor) load.<br>
`htop` - Interactive process viewer.<br>
`kill` - Kill a process.<br>
`time` - Run programs and summarize system resource usage.<br>

### Installing Programs and Libraries

`apt-get` - APT package handling utility.<br>
`pip` - A tool for installing and managing Python packages.<br>
`pip2` - A tool for installing and managing Python2 packages.<br>
`pip3` - A tool for installing and managing Python3 packages.<br>

### Running Code and Scripts

`sh` - **SHell** - Command interpreter.<br>
`bash` - **Bourne Again SHell** - Command interpreter. (More updated than `sh`)<br>
`python` - Python interpreter (typically defaults to python2).<br>
`python2` - Python2 interpreter.<br>
`python3` - Python3 interpreter.<br>

### USB Information

`lsusb` - **List USB** - list USB devices.<br>

### Script Commands

`echo` - Display a line of text.<br>
`sleep` - Sleep for a specified number of seconds.<br>

### Command Help

`man` - **Manual** - an interface to the on-line reference manuals.<br>
`whatis` - **What Is** - display one-line manual page descriptions.<br>

### Power

`reboot` - Restart the device.<br>
`shutdown` - Power-off the device.<br>

### Other Helpful Commands

`ssh` - **Secure SHell** - OpenSSH SSH client. (remote login program)<br>
`git` - Code version control suite.<br>
