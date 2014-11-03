from sys import argv
import serial
import serial.tools.list_ports

# estos arrays representan los frames que realizan las acciones en el dispositivo
# remoto, al momento estan staticos, falta implementar modulo que genere los frames
# dinamicamente.

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

#Pines y comandos disponibles
listaIO = [0,1,2,3,4]
listaCmd = ["on","off"]

# Variables que se usan dentro del programa
prompt = '>'
separador = "++++++++++++++++++++++++++++++"
pattern = '\/dev\/tty[A-Z]{3}[0-0]*'

#mientras exit se mantenga en 1 el programa se mantiene en ejecucion.
exit = 1


#########################Funciones###########################################

#Buscamos dentro del sistema los puertos seriales disponibles /dev/ttyXXX##
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

#Selecciona el pin del bboard que deseamos controlar
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

#Selecciona el comando que deseamos enviar al bboard
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
	
#Teniendo un pin y un comando seleccionamos el frame a enviar
def enviarComando(io, cmd):
	if cmd == "on":
		cmdArray = lista_cmdON
	elif cmd == "off":
		cmdArray = lista_cmdOFF
	else:
		print "comando %r no reconocido" % cmd

	board.write(cmdArray[io].decode('hex'))
	print "Comando enviado >> %r\n" % cmdArray[io]

#Valida que el puerto seleccionado este disponible
def iniciarBoard(puerto):
	try:
		boardFun = serial.Serial(puerto, 9600)
	except serial.serialutil.SerialException:
		print "Puerto %s, no encontrado" % puerto	
	else:
#		print "Puerto %s, abierto" % puerto
		return boardFun

#Termina conexione con el servidor.
def terminarBoard(board):	
	if board:
		if board.isOpen():
			board.close()
			print "Cerrando board ..."	
		else:
			print "board esta cerrado"
	else:
		print "Board inexistente"

#pregunta si deseamos terminar la ejecucion.
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
	

#Despliega un listado de los puertos disponibles.
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

