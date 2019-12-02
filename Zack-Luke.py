#!/usr/bin/python3

# ---------------------------------
# Purpose: Individual Functions

# Version: 1
#
# November 25, 2019
# ----------------------------------

import requests
import urllib3

urllib3.disable_warnings()

# host is projector, username generally admin, password generally admin
host = "10.103.36.88"
getURL = "https://" + host + "/"
get = requests.get(url=getURL, verify=False)

print(get.status_code)

cookieString = str(get.cookies)
cookMid = cookieString.split(" ")
cookie = cookMid[1]

cookie = cookie.split("=")
cookieDict = {}
cookieDict[cookie[0]] = cookie[1]



print("Trying to Reboot.")

data = {
    b"{Device: {DeviceOperations: {Reboot: true}}}"
}

postURL = "https://" + host + "/Device/DeviceOperations"

# Send Login Request
reboot = requests.post(url=postURL, data=data,  verify=False, cookies=cookieDict)

print(reboot.status_code)


