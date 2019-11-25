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

print("Trying to login.")

host = "10.103.36.85"
username = "admin"
newPass = "password"

url = "https://" + host + "/"

# Send Login Request
login = requests.get(url=url, verify=False)

cookieString = str(login.cookies)

cookieMid = cookieString.split(" ")
cookies = cookieMid[1]
print(cookies)

# host is the target, cookies is cookie from login above, loop is True or False
action = "ChangePass"
if action == "ChangePass":
    url = "https://" + host + "/Device/Authentication/"
data = {
    "Device": {
        "Authentication": {
            "AuthenticationState": {
                "AdminUsername": username,
                "AdminPassword": newPass,
                "IsEnabled": "true"
            }
        }
    }
}
changePass = requests.post(url=url, data=data, verify=False, cookies=cookies)
print(changePass.status_code)
print(changePass.text)
print("Password Change Request Sent")
