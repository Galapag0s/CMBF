#!/bin/usr/python3


import requests
import urllib3

urllib3.disable_warnings()
#This script is designed to identify which model a system is.

hosts = ['10.103.36.88','10.103.36.91','10.103.36.94','10.103.36.106','10.103.36.115','10.103.36.117','10.103.36.118','10.103.36.119','10.103.36.120','10.103.36.121','10.103.36.123','10.103.36.124','10.103.36.125','10.103.36.126','10.103.36.129','10.103.36.131','10.103.36.133','10.103.36.135','10.103.36.136','10.103.36.137','10.103.36.138','10.103.36.141','10.103.36.142','10.103.36.154','10.103.36.156','10.103.36.159','10.103.36.160','10.103.36.161','10.103.36.163','10.103.36.166','10.103.36.83','10.103.36.84','10.103.36.85']

for host in hosts:
	tswURL = "http://" + host + "/webView/CommonUI"
	tswTest = requests.get(tswURL, verify=False)
	theOGurl = "http://" + host + "/cgi-bin/login.cgi?lang=en&src=AwLoginDownload.html"
	theOGTest = requests.get(theOGurl, verify=False)
	air2url = "http://" + host + "/index_airmedia.html"
	air2Test = requests.get(air2url, verify=False)
	if "var present_timeout = 1000;" in air2Test.text:
		print(host + " is a AirMedia2")
	elif theOGTest.status_code == 200:
		print(host + " is an OG")
	elif  "Display the application" in tswTest.text:
		print(host + " is a tsw760")
	elif "DispBlock OvHidden FontLatoLight Fs30 Blue" in air2Test.text:
		print(host + " is the one we did dev for")
#		print(air2Test.text)
