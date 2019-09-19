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

#Admin Creds
username="admin"
password="admin"

#Target
host="10.103.36.87"

#URL of Projector
url="https://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginAdmin.html"

#POST Data
data = {
    'login': 'admin',
    'account': 'admin',
    'password':'admin',
    'Login.x':'56',
    'Login.y':'16'

}

#Send Login Request
login = requests.post(url = url, data = data, verify=False)

#Pull Out Cookie So You Can Keep Making Requests
cookieStart=login.text.split("document.write(\"<form name=\'form0\' action=\'/cgi-bin/reboot.cgi?lang=en&")
cookieMid=cookieStart[1].split("'")
cookie=cookieMid[0]
print(cookie)

#Turn Remove View Off
url = "https://"+ host + "/cgi-bin/return.cgi"
#data = {
#    "command":"<Send><seid>"+ cookie +"</seid><name>SLIDES_ALWAYS_SEND</name><value>1</value><name>SLIDES_PASSWORD</name><value>0</value><name>SLIDES_SECOND</name><value>0</value></Send>"
#}
data = {
    "command" :	"<Send><seid>" + cookie + "</seid><Factory>reboot</Factory></Send>"
}
remoteViewOn = requests.post(url=url,data=data, verify=False)