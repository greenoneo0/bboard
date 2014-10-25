from sys import argv
import serial

script, puerto = argv

cmdON = []

cmdOFF = []

prompt = '>'

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

board = iniciarBoard(puerto)
terminarBoard(board)
if board.isOpen():
	print "sigue abierto"
else:
	print "yano esta"

print "Exit"	
