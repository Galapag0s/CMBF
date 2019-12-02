#------------------------------------------------------------------------------------
#
#	Creston Package
#
#	Contains Important Funcitons
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

urllib3.disable_warnings()

def network_scan(ip_range)
	#Create List To Hold All Possible Hosts On The Network
	allHosts=[]

	#Add All Possible Hosts To List
	for ip in ipaddress.ip_network(str(ip_range)):
		allHosts.append(ip)

	#Drop Newtork ID and Broadcast Address
	allHosts.pop(0)
	del allHosts[-1]

	#Create List To Hold Live Hosts
	onlineHosts =[]

	#Send HTTPS requests to See if port is open
	for hosts in allHosts:
		url="https://" + str(hosts) + "/"
		try:
			#Sends Rquest
			check = requests.get(url = url, timeout=5,verify=False)
			#Grabs Hash of Request
			systemOnline = hashlib.md5(check.text.encode())
			#Checks if Response is Same As Known Projector Samples
			if(systemOnline):
			print("PROJECTOR: " + url)
			onlineHosts.append(str(ipaddress.IPv4Address(hosts)))
			#Generate a random wait time
			waitTime = random.random() * 3.0
			#Wait the Random Time (This is done to try to Look less suspicious to Firewalls)
			time.sleep(waitTime)
			#Handle Any Exceptions (Generally Caused by Port being closed
		except requests.exceptions.RequestException as e:
			pass
	#Clean UP onlineHosts So Its Only IPs
	return onlineHosts

def model_type(hosts)
	#Send HTTPS requests to See if port is open
	model_dictionary = {}
	for host in hosts:
		tswURL = "http://" + host + "/webView/CommonUI"
		tswTest = requests.get(tswURL, verify=False)
		theOGurl = "http://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginDownload.html"
		theOGTest = requests.get(theOGurl, verify=False)
		air2url = "http://" + host + "/index_airmedia.html"
		air2Test = requests.get(air2url, verify=False)
		if "var present_timeout = 1000;" in air2Test.text:
			print(host + " is a AirMedia2")
			model_dictionary[host] = 'AirMedia2'
		elif theOGTest.status_code == 200:
			print(host + " is an OG")
			model_dictionary[host] = 'OG'
		elif  "Display the application" in tswTest.text:
			print(host + " is a tsw760")
			mode_dictionary[host] = 'TSW760'
		elif "DispBlock OvHidden FontLatoLight Fs30 Blue" in air2Test.text:
			print(host + " is the one we did dev for")
			model_dictionary[host] = 'Ignore'
	return model_dictionary
