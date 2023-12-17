
# cette section de code ajoute les fonctionnalite web et electronic a notre application 
import requests
import time


#import serial
#serial_port = serial.Serial(port = "COM7", baudrate = 9600)
def envoi_donne_au_serveur_players_teams(adresse_serveur,donnee_a_envoyer):
	## donne a en envoyer ici  est un dictionnaire de la forme
	"""
	donne_envoyer = {
	
	'equipe' : {
		'equipeA': 'TC1' , 
		'equipeB': 'TC2'
	},

	'joueurs' : {
		'joueursA' : ['khalifa' , 'Aliou'],
		'joueursB' : ['mouhamed','babacar']
	}

}
	"""
	r = requests.post(adresse_serveur + "/api/receptionsTeamNamePlayersName/" , json = donnee_a_envoyer)
	print(r.status_code)

def envoi_donne_au_serveur_scores(adresse_serveur , donnee_envoyer):
	"""
	la donne a envoyer est de la forme
	donne_score = {'scoreA': i,  'scoreB' :  i + 10}

	"""
	ra = requests.post( adresse_serveur + "/api/receptionsScoreA&ScoreB/" , json = donne_score)
	print(ra.status_code)

"""
dans cette partie , il s'agira de communiquer avec arduino qui va nous envoyer des signaux 
avec le signaux obtenu on met en surbillance l'un des nom du joueur donc a la fin on return le text que l'arduino nous a envoye
"""

"""
def electronics():

	#etablissement de la communication avec l'arduino
	
	
	# réinitialisation
	global serial_port
	serial_port.setDTR(False)
	time.sleep(0.1)
	serial_port.setDTR(True)
	# on vide le buffer
	serial_port.flushInput()
	# lecture des données
	donne_recu = serial_port.readline()
	#print(serial_port.readline())
	#cette instruction retourne la valeur lue dans le port serie et c sur cette valeur qu'on aura a faire des tests
	#serial_port.close()
	return donne_recu
"""