from sys import argv
import serial
import serial.tools.list_ports



cmdON = []

cmdOFF = []

prompt = '>'
separador = "++++++++++++++++++++++++++++++"
pattern = '\/dev\/tty[A-Z]{3}[0-0]*'


def listarPuertos(p):
	iterable = serial.tools.list_ports.grep(pattern)
#	p = serial.tools.list_ports.comports()
#	print p
	for i in iterable:
		p.append(i[0])
		print i[0]
	return p

def enviarComando(io, cmd):
	if cmd == "on":
		cmdArray = cmdON
	elif cmd == "off":
		cmdArray = cmdOFF
	else:
		print "comando %r no reconocido" % cmd

	board.write(cmdArray[io])
	print "Comando enviado >> %r\n" % cmdArray[io]

def iniciarBoard(puerto):
	try:
		boardFun = serial.Serial(puerto, 9600)
	except serial.serialutil.SerialException:
		print "Puerto %s, no encontrado" % puerto	
	else:
		print "Puerto %s, abierto" % puerto
		return boardFun

def recibePin():
	pin = raw_input(prompt)
	
def recibeComando():
	comando = raw_input(prompt)

def terminarBoard(board):	
	if board:
		if board.isOpen():
			board.close()
			print "Cerrando board ..."	
		else:
			print "board esta cerrado"
	else:
		print "Board inexistente"

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
	
	print opciones	

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


######### execution ##########

#try:
#	script, puerto = argv
#except ValueError:
#	print "No se proporciona puerto"
#else:
#	listarPuertos()

puertosDisponibles = []

puertosDisponibles = listarPuertos(puertosDisponibles)
print "Salio el puerto, se pasa:"
print puertosDisponibles
for i in puertosDisponibles:
	print i
miIndex = seleccionarPuerto(puertosDisponibles)
print miPuerto[miIndex]


#board = iniciarBoard(puerto)
#terminarBoard(board)
#if board.isOpen():
#	print "sigue abierto"
#else:
#	print "yano esta"

#print "Exit"	
