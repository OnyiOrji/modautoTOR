# -*- coding: utf-8 -*-

import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('rpm -q python3-pip', shell=True)
    if str('is not installed') in str(check_pip3):
        raise subprocess.CalledProcessError(returncode=1, cmd='rpm -q python3-pip')
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo yum update', shell=True)
    subprocess.check_output('sudo yum install python3-pip', shell=True)
    print('[!] pip3 installed successfully')



try:
    import requests
except ImportError:
    print('[+] python3 requests is not installed')
    os.system('sudo yum install python3')  # Install Python3 if not installed
    os.system('sudo yum install python3-pip')  # Install pip3 if not installed
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed')
    os.system('sudo yum install tor')  # Install Tor if not installed
    print('[!] tor is installed')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

print('''\033[1;32;40m \n
                _          _______
     /\        | |        |__   __|
    /  \  _   _| |_ ___      | | ___  _ __
   / /\ \| | | | __/ _ \     | |/ _ \| '__|
  / ____ \ |_| | || (_) |    | | (_) | |
 /_/    \_\__,_|\__\___/     |_|\___/|_|
                V 2.1
from mrFD
''')
print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("[+] time to change Ip in Sec [type=60] >> ")
lin = input("[+] how many time do you want to change your ip [type=1000]for infinte ip change type [0] >>")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\nauto tor is closed ')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
