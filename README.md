bboard
======

#Hardware

##Bboard-io
Version 0.1

###Description
Bboard-io is a development board that allows xbee users to have accesss to xbee io pins.
That allows to contror digital enviroments remotely with no need of microcontroller.
Usage is based on Xbee API mode.

###Specs
* 5 io pins (D0 to D4).
* Usb port (miniUSB connector)
* Power jack connector
* Xbee state leds (Assoc, RSSI, ON and Power)

###General
IO pins are attached to a level shifter (3.3v to 5v). So can interface the board to 
standard 5v devices.
Level shifter uses automatic direction detection, so can configure pines as input or
output with no restrictions.
USB port is really a USB serial converter on 3.3v maped directly to the RX/TX pins
on Xbee module, cts and rts lines are also wired.
Can be powered used an external 5v power supply (2.1mm connector).

Schematics wrote on eagle 6.5
[Pictur of the first board](https://flic.kr/p/pqZYEE)

#Software.

##bbio-cmd.py
version 0.1

CLI script that allows user to send frames to the bboard in order to control the 
device. Actual version has frames hardcode user need to generate its own frames
based on the address of the xbee attached to the board.

*To-do.*
* Create a bboard-io class.
* Create methods for dinamic frame creation based on xbee address and the action to perform.
* Handle acknowledge from the xbee.




