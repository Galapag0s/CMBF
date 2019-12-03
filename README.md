# CMBF
Creston Projector Botnet Framework
## Table Of Contents
- Dates of Events (Communications, Tests, etc.)
- Tool documentation
- Code Explanationo/Logic
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
