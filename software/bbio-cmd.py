###################################################################################
#bbio-cmd.py
#CLI script to interact with a bboard-io device.
#
#
#Written by: Eden Candelas
#License: GPL 3
#Hackerspace Monterrey.
#
###################################################################################

from sys import argv
import serial
import serial.tools.list_ports

# These arrays are the frames that will be sent to the bboard, they are static by
# you need to generate your own based on the address of the xbee attached to the
# board. Basically they are frame 17 (AT remote comand)

lista_cmdON = [ '7E001017010013A200403B10CDFFFE0244300562',
		'7E001017010013A200403B10CDFFFE0244310561',
		'7E001017010013A200403B10CDFFFE0244320560',
		'7E001017010013A200403B10CDFFFE024433055F',
		'7E001017010013A200403B10CDFFFE024434055E']

lista_cmdOFF = ['7E001017010013A200403B10CDFFFE0244300463',
		'7E001017010013A200403B10CDFFFE0244310462',
		'7E001017010013A200403B10CDFFFE0244320461',
		'7E001017010013A200403B10CDFFFE0244330460',
		'7E001017010013A200403B10CDFFFE024434045F']

#Pins on the board and actions available
listaIO = [0,1,2,3,4]
listaCmd = ["on","off"]

# Some variables for the program
prompt = '>'
separador = "++++++++++++++++++++++++++++++"
pattern = '\/dev\/tty[A-Z]{3}[0-0]*'

#State for the main while loop. if 0 script stops.
exit = 1


#######################  Funciones  ##############################################

#Look for available ports based on "pattern" /dev/ttyXXX##
def listarPuertos(p):
	print "Leyendo puertos"
	iterable = serial.tools.list_ports.grep(pattern)
#	p = serial.tools.list_ports.comports()
#	print p
	print "Puertos encontrados:"
	for i in iterable:
		p.append(i[0])
		print i[0]
	return p

#Select pin to control
def ingresarPin(lista):
	statusIO = 1

	print separador
	print 

	while statusIO:
		print "IO disponibles:"

		for i in lista:
			print "\t %r" % lista[i]

		print "Ingrese pin que desea controlar"
		io = raw_input(prompt)

		try:
			index = lista.index(int(io))
			statusIO = 0
		except ValueError:
			print "Opcion %r desconocida" % io
			statusIO = 1
			print "Ingrese otra opcion"

	return index

#Select comand to send
def ingresarComando(lista):
	statusCMD = 1

	while statusCMD:
		print "Comandos disponibles"
		print
		for i in lista:
			print "\t %r" % i	
		print
		print "Ingresa el comando que deseas enviar"
		
		cmd = raw_input(prompt)
		
		try:
			index = lista.index(cmd)
			statusCMD = 0
		except ValueError:
			print "Opcion %r desconocida" % cmd
			statusCMD = 1
			print "Ingrese otra opcion"

	return index
	
#Once we have a pin and a comand we can select the frame to be sent to the board.
def enviarComando(io, cmd):
	if cmd == "on":
		cmdArray = lista_cmdON
	elif cmd == "off":
		cmdArray = lista_cmdOFF
	else:
		print "comando %r no reconocido" % cmd

	board.write(cmdArray[io].decode('hex'))
	print "Comando enviado >> %r\n" % cmdArray[io]

#Opens selected port
def iniciarBoard(puerto):
	try:
		boardFun = serial.Serial(puerto, 9600)
	except serial.serialutil.SerialException:
		print "Puerto %s, no encontrado" % puerto	
	else:
#		print "Puerto %s, abierto" % puerto
		return boardFun

#End conection to the serial port
def terminarBoard(board):	
	if board:
		if board.isOpen():
			board.close()
			print "Cerrando board ..."	
		else:
			print "board esta cerrado"
	else:
		print "Board inexistente"

#Give exit or continue option
def salir():
	exit = 1
	status = 1
	while status:
		print "Ingrese \'s\' para salir, \'c\' para continuar"
		i = raw_input(prompt)
		if i == 's':
			exit = 0	
			status = 0
		elif i == 'c':
			exit = 1
			status = 0
		else:
			print "Opcion no valida"
	
	return exit	
	

#Display on screen a list for the avalaible ports and select one from them, returns its position.
def seleccionarPuerto(p):
	numero = 1
	opciones = []
	status = 1
	print separador
	print "Seleccione uno de los puertos diponibles"
	
	for i in p:
		print "%d) %r" % (numero,i)
		opciones.append(numero)
		numero = numero + 1
	
#	print opciones	

	while status:
		seleccion = raw_input(prompt)
		try:
			index = opciones.index(int(seleccion))
			status = 0
		except ValueError:
			print "Opcion %r desconocida" % seleccion
			status = 1
			print "Ingrese otra opcion"
	
	return index


###################### execution ######################

#try:
#	script, puerto = argv
#except ValueError:
#	print "No se proporciona puerto"
#else:
#	listarPuertos()

puertosDisponibles = []
puertosDisponibles = listarPuertos(puertosDisponibles)
index = seleccionarPuerto(puertosDisponibles)

print "Puerto seleccionado: %r" % puertosDisponibles[index]

puerto = puertosDisponibles[index]
board = iniciarBoard(puerto)

print "Interface con bboard abierta"

while exit:
	ioIndex = ingresarPin(listaIO)

	print "IO seleccionado : %d" % listaIO[ioIndex]

	cmdIndex = ingresarComando(listaCmd)

	print "Comando seleccionado : %s" % listaCmd[cmdIndex]

	enviarComando(listaIO[ioIndex], listaCmd[cmdIndex])

	exit = salir()
 
terminarBoard(board)
if board.isOpen():
	print "sigue abierto"
else:
	print "bytes"

