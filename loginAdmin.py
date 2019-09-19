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
    'password':'admin',
    'Login.x':'56',
    'Login.y':'16'

}

login = requests.post(url = url, data = data, verify=False)
print(login.text)
cookieStart=login.text.split("document.write(\"<form name=\'form0\' action=\'/cgi-bin/reboot.cgi?lang=en&")
cookieMid=cookieStart[1].split("'")
cookie=cookieMid[0]
print(cookie)
