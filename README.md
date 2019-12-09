# CMBF
Creston Projector Botnet Framework
## Table Of Contents
- Introduction
- Tool documentation
- Dates of Events (Communications, Tests, etc.)
- Code Explanationo/Logic
## Introduction
Within recent years we have seen an explosion of internet connected devices.  With a network connection, these devices can expand their usability.  However, adding the capability to add these devices to the internet, we have also added an unexpected risk. 
Now, devices are vulnerable to network attacks.

In some cases, the impact is minimal.  An attacker may be able to access basic information that is seemingly meaningless to us.  
However, in other cases, these vulnerabilities can lead to the complete take over of the devices.

This semester, we identified a vulnerability in the Creston Projectors which allowed for a complete device take over.  Using our tool, we have been able to ident over 50 vulnerable devices.  Since we are able to reset authentication information, we stand to take complete ownership over these devices.  At a current cost of $1,400 per device, we stand to take control of tens of thousands of dollars of technology.  Considering that these projectors are also used in classes, there is an undetermined loss due to potential down time.  

Our script used python3 to automate web requests.  By utilizing CWE-521, weak password requirements, we were able to obtain access to these devices.  Our script accounts for all models but one type.  Though, it should be noted that this model is not secure.  Rather, the web interface is unable to make administrative changes.  Despite that, an attacker can still access this model via a management port that can identified in Creston's documentation.  This management port also suffers from CWE-521.
## How To Use
### Commands
#### help [command]
  - Display a help menu which lists all available commands.
  - If a command is provided, it will supply additional information about the command.
#### network_scan [ip range]
  - This command will scan the ip range that is given to the function.  The results will be stored by the system for the duration of the session.
  - The IP range should be passed in as CIDR notation.
#### add_host [ip]
  - This command can be used to add a projector manually.
  - The ips must be passed one at a time.
#### print_hosts
  - This command will print out the live hosts.
#### model_scan
  - This command will scan the saved projectors to determine the model type.
#### print_model
  - This command will print the stored models of all hosts from this session.
#### reboot [username] [password]
  - This command will begin rebooting all live hosts.  The model scan must occur before this can run.
  - The username and password will be used to login to the devices.
#### pass_change [username] [password] [newpassword]
  - This command can be used to change the password on a device, if the current password is known.
#### restore [ip]
  - This command will restore the specified ip to factory settings.  This may take the device off line.
#### web_dos [ip] [username] [password] [webserver]
  - This command will tell the speicified IP to begin sending web requets to the specified web server.
#### code_cycle [ip] [username] [password]
  - This command will force the specified ip to begin cycling through random connection codes.  This can make the device unreachable.

## Important Dates
### First Contact
- Mid September
  - Identified Default Credentials on Projectors and Began Exploring Funcitonality
  - 'Accidently' Kicked the Professor Off the Projector (MY CRIME IS THAT OF CUROSITY)
### Initial Development
- November
  - Began Development of Script
### Initial Disclosure
- Late November
  - Discussed The Known Vulnerabilities With The CISO
  - Agreed to Send Finished Code To CISO To Mitigate Risk
### Public Disclosure
- December
  - Presented Script and Attacked Several Machines
## Code Explanation
### gui.py
This code contains all the user interface options you are presented with.  This user interface interfaces with the creston module to run all necessary commands.
### creston.py
This code contains the actual functions used by the user interface.  This package will take various inputs, and perform actions on the projectors based on the IP.

For a more indepth explanation, see the source code comments.
