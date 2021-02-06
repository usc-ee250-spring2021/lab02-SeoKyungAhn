""" EE 250L Lab 02: GrovePi Sensors

List team members here.
Seo Kyung (Brian) Ahn
Insert Github repository link here.
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
import grove_rgb_lcd
# variable declarations
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")
adc_ref = 5
grove_vcc = 5
full_angle = 300
led = 5
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e
PORT = 4    # D4

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':

    while True:
	try:
		#So we do not poll the sensors too quickly which may introduce noise,
		#sleep for a reasonable time of 200ms between each iteration.
		time.sleep(0.2)

		#print(grovepi.ultrasonicRead(PORT))
		ultrasonicVal = grovepi.ultrasonicRead(PORT)
		rotaryVal = grovepi.analogRead(potentiometer)
		grove_rgb_lcd.setText_norefresh(str(ultrasonicVal)+" cm\n"+str(rotaryVal)+" cm")
		if ultrasonicVal <= rotaryVal :
			grove_rgb_lcd.setText_norefresh(str(ultrasonicVal)+" cm OBJ PRES\n"+str(rotaryVal)+" cm")
			grove_rgb_lcd.setRGB(255,0,0)
	except TypeError as e :
		print(str(e))
	except KeyboardInterrupt as e :
		print(str(e))
		break








	




