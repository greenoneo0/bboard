bboard
======

##Bboard-io

**Version 0.1**

###Description
Bboard-io is a development board that allows xbee users to have accesss to io pins in the board.
That allows to contror digital enviroments remotely with no need of microcontroller.

###Specs
*5 io pins (D0 to D4).
*Usb port (miniUSB connector)
*Power jack connector
*Xbee state leds (Assoc, RSSI, ON and Power)

###General
IO pins are attached to a level shifter (3.3v to 5v).
Level shifter uses automatic direction detection so can configure pines as input or
output with no restrictions.
USB port is really a USB serial converter on 3.3v maped directly to the RX/TX pins
on Xbee module.
Can be powered used an external 5v power supply (2.1mm connector).

