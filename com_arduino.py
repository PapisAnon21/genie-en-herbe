import serial
import time, threading 



def init_com(port , vitesse):
	serial_port = serial.Serial(port = port, baudrate = vitesse)
"""
def start_com(duree = 2): 
	#serial_port.setDTR(False)
	time.sleep(0.1)
	serial_port.setDTR(True)
	# on vide le buffer
	serial_port.flushInput()
	# lecture des données
	message_recu = serial_port.readline().decode("utf-8")
	#print(message_recu)
	#JOUEURS[message_recu].configure(col)	
	threading.Timer(duree, start_com).start()
	#return message_recu 
"""