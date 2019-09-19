
#!/usr/bin/python3

#------------------------------------------------------------------------------------
#
#   Purpose: Find all Creston Projectors
#
#
#
#
#
#-------------------------------------------------------------------------------------

import requests
import ipaddress
import hashlib
import time
import random

allHosts=[]
ip_range='10.103.36.0/23'

for ip in ipaddress.ip_network(str(ip_range)):
    allHosts.append(ip)
 
allHosts.pop(0)
del allHosts[-1]

#hosts = '10.103.36.87'
onlineHosts =[]
for hosts in allHosts:
    url="https://" + str(hosts) + "/"
    print(url)
    try:
        check = requests.get(url = url, timeout=5,verify=False)
        systemOnline = hashlib.md5(check.text.encode())
        print(systemOnline.hexdigest())
        hashVal='8805829fe41105187d46c8b7d18f6baa'
        if(systemOnline.hexdigest() == hashVal):
            onlineHosts.append(hosts)
        waitTime = random.random() * 4.0
        time.sleep(waitTime)
    except requests.exceptions.RequestException as e:
        print("Go Fuck Youreself")
print(onlineHosts)