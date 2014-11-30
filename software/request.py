import requests
import serial

puerto = "/dev/ttyUSB0"

xbee = serial.Serial(puerto, 9600)



while (1):
	status = 1
	
	print ""
	print "+++++++++++++++++"
	print "Waiting...."

#	while (status == 1):
#		line = xbee.readline()
#		print line
#		if (line.strip() == "box1"):
#			status = 0

	while (status == 1):
		line =xbee.readline()
		print line
		lineNew = line.strip()
		data = lineNew.split(":")
		try:
			print data[0], data[1]
			if( data[0] == "box"):
				status = 0
		except IndexError:
			print "Invalido"
		


	print "comando recibido"

	peticion =  "http://192.168.1.194:8000/hola?box=" + data[1]
	print "Peticion a enviar: " + peticion
	r = requests.get(url = peticion)
	status = r.status_code
	print status
	content = r.text
	print content
