#!/usr/bin/python3

#------------------------------------------------------------------------------------
#
#   Purpose: Login Script
#
#
#
#
#
#-------------------------------------------------------------------------------------

import requests

print("Trying to login now")

username="admin"
password="admin"

host="10.103.36.87"

url="https://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginAdmin.html"

data = {
    'login': 'admin',
    'account': 'admin',
    'password':'admin'
}

login = requests.post(url = url, data = data, verify=False)
if login.history:
    print("Request was redirected")
    for resp in login.history:
        print(resp.status_code + ", " + resp.url)
    print("Final destination:")
    print(login.status_code + ", " + login.url)
else:
    print("Request was not redirected")
