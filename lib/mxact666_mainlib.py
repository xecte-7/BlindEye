#!/usr/bin/python2

''' ini merupakan library tambahan pertama untuk Tools
berisi segala hal untuk membantu berjalannya tools
memiliki sub-fungsi untuk melakukan berbagai jenis proses '''

import httplib,socket,time,os,platform,datetime

error_blank = "[!] Error: Don't leave it blank!"
error_cantconnect = "[!] Error: Can't connect with Target!"
error_cantread = "[!] Error: Can't open or read the File!"
error_choice = "[!] Error: Invalid choice!"
error_command = "[!] Error: Invalid command!"
error_import = "[!] Error: Failed to Import some module or library!"
error_ipaddress = "[!] Error: Can't get IP Address!"
error_offline = "[!] Error: You are Offline!"
error_portclosed = "[!] Error: Port is not open!"
error_unknown = "[!] Error: Unknown Error has been occured!"

opsys = platform.system()

kini = datetime.datetime.now()
jam = kini.hour
menit = kini.minute
detik = kini.second
waktufull = "{}_{}_{}".format(jam,menit,detik)

def clearscreen():
	if platform.system() == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
def jeda():
	print ""
	raw_input(">>> Press [ENTER] to Continue...")
def keluar():
	print ""
	print "[*] Stopping Program..."
	time.sleep(1)
	print "[^] Assalamualaikum :)"
	exit()

def cek_koneksi():
	a = httplib.HTTPConnection("www.google.com",80,timeout=1.5)
	a.request("HEAD","/")
	b = a.getresponse()
	return b.status
def cek_ip(host):
	try:
		ip = socket.gethostbyname(host)
		print ip
	except:
		print error_ipaddress
def cek_port(ip,port):
	a = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	a.settimeout(1)
	b = a.connect_ex((ip,port))
	if b == 0:
		print "OPEN"
	else:
		print "CLOSED"
def cek_arch():
	if platform.machine() == "AMD64" or platform.machine() == "amd64":
		print "x64"
	else:
		print "x86"