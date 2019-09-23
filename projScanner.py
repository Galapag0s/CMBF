
#!/usr/bin/python3

#------------------------------------------------------------------------------------
#
#   Purpose: Find all Creston Projectors
#
#   Version: 1
#
#   Date: 9/19/2019
#
#-------------------------------------------------------------------------------------

import requests
import ipaddress
import hashlib
import time
import random

#Create list to hold all possible hosts on the network
allHosts=[]

#Network Range For Analysis
ip_range='10.103.36.0/23'

#Add All Possible Hosts To List
for ip in ipaddress.ip_network(str(ip_range)):
    allHosts.append(ip)

#Drop Newtork ID and Broadcast Address
allHosts.pop(0)
del allHosts[-1]

#Create List to Hold Projectors
onlineHosts =[]

#Send HTTPS requests to See if port is open
for hosts in allHosts:
    url="https://" + str(hosts) + "/"
    #print(url)
    try:
        #Sends Rquest
        check = requests.get(url = url, timeout=5,verify=False)
        #Grabs Hash of Request
        systemOnline = hashlib.md5(check.text.encode())
        print(systemOnline.hexdigest())
        hashVal='8805829fe41105187d46c8b7d18f6baa'
        #Checks if Response is Same As Known Projector Samples
        if(systemOnline.hexdigest() == hashVal):
            print(url)
            onlineHosts.append(hosts)
        #Generate a random wait time
        waitTime = random.random() * 4.0
        #Wait the Random Time (This is done to try to Look less suspicious to Firewalls
        time.sleep(waitTime)
    #Handle Any Exceptions (Generally Caused by Port being closed
    except requests.exceptions.RequestException as e:
        print("Go Fuck Youreself")
print(onlineHosts)
