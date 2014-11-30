import serial
import sys

puerto = "/dev/ttyUSB0"

xbee = serial.Serial(puerto,9600)

string_ = sys.argv[1]

xbee.write(string_)

