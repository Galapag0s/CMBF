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

print("Trying to Reboot.")

host = "10.103.36.88"

data = {
    b"{Device: {DeviceOperations: {Reboot: true}}}"
}


url = "https://" + host + "/Device/DeviceOperations"

# Send Login Request
reboot = requests.post(url=url, data=data, verify=False)
print (reboot.status_code)



