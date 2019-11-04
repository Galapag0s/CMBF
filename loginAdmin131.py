#!/usr/bin/python3

#---------------------------------
# Admin Login 131
#
# Version: 1
#
# October 21, 2019
#----------------------------------

import requests
import urllib3

urllib3.disable_warnings()

print("Trying to log in.")

#Admin Credentials
username="admin"
password="password"

#Target
host="10.103.36.131"

#URL of projector
url="https://" + host + "/userlogin.html"

#data
data={
    'login': 'admin',
    'passwd': 'password'
}

#Send login request
login = requests.post(url=url, data=data, verify=False)
cookieString = str(login.cookies)
cookMid = cookieString.split(" ")
cookie = cookMid[1]
print(cookie)

action="ChangePass"
if action == "Reboot":
    #Reboot the device
    url = "https://" + host + "/Device/DeviceOperations"
    data = {
        "Reboot": True
    }
    reboot = requests.post(url=url, data=data, verify=False, cookies=cookies)
    print("Reboot Incoming")
elif action == "ChangePass":
    #Change Password of Device
    newPass = "Asteroid01"
    url = "https://" + host + "/Device/Authentication/"
    data = {
        "Name": "admin",
        "Password": newPass
    }
    changePass = requests.post(url=url, data=data, verify=False, cookies=cookies)
    print("Password change request sent.")


