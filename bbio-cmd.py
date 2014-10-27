from sys import argv
import serial
import serial.tools.list_ports



cmdON = []

cmdOFF = []

listaIO = [0,1,2,3,4]
listaCmd = ["on","off"]

prompt = '>'
separador = "++++++++++++++++++++++++++++++"
pattern = '\/dev\/tty[A-Z]{3}[0-0]*'


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

def ingresarPin(lista):
	statusIO = 1

	print separador
	print 

	while statusIO:
		print "IO disponibles:"

		for i in lista:
			print lista[i]

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

def ingresarComando(lista):
	statusCMD = 1

	while statusCMD:
		print "Comandos disponibles"
		print
		for i in lista:
			print i	
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
#		print "Puerto %s, abierto" % puerto
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


######### execution ##########

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

ioIndex = ingresarPin(listaIO)

print "IO seleccionado : %d" % listaIO[ioIndex]

cmdIndex = ingresarComando(listaCmd)

print "Comando seleccionado : %s" % listaCmd[cmdIndex]

 
terminarBoard(board)
if board.isOpen():
	print "sigue abierto"
else:
	print "ya no esta"

#print "Exit"	
