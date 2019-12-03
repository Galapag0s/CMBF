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
  - This function will scan the ip range that is given to the function.  The results will be stored by the system for the duration of the session.
  - The IP range should be passed in as CIDR notation.
#### add_host [ip]
  - This command can be used to add a projector manually.
  - The ips must be passed one at a time.
#### print_hosts
#### model_scan
#### print_model
#### reboot
#### pass_change
#### host_name
#### restore
#### web_dos
#### code_cycle

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
