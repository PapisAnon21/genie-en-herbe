#@from anonyme 21


from flask import Flask, request,render_template , jsonify


app = Flask(__name__)


#cette requete se fera une seule fois pour envoyer le nom des equipe et des joueurs
@app.route("/api/receptionsTeamNamePlayersName/", methods = ["POST"])
def donne_recu():
	donnees = request.json
	print(donnees)
	
	equipeA = donnees['equipe']['equipeA']
	equipeB = donnees['equipe']['equipeB']
	JoueursA = donnees['joueurs']['joueursA']
	JoueursB = donnees['joueurs']['joueursB']
	#maintenant nous allons mettre ces nouveaux donne dans un dict
	
	global my_donne 
	my_donne = {
		'equipeA' : equipeA,
		'equipeB' : equipeB,
		'joueursA' : JoueursA,
		'joueursB' : JoueursB

	}
	return 'donne_recue'
	
@app.route("/")
def main_page():
	return render_template('page_web.html', **my_donne)


# cette requete d'envoi se fera tout le temps pour envoyer a chaque fois le score
@app.route("/api/receptionsScoreA&ScoreB/", methods = ["POST"])
def autre_donne():
	donnees_score = request.json
	print(donnees_score)
	global scoreA
	global scoreB
	scoreA = donnees_score["scoreA"]
	scoreB = donnees_score["scoreB"]
	return ''

@app.route("/api/demandeScore/", methods = ["GET"])
def envoi_score():
	my_donne["scoreA"] = scoreA 
	my_donne["scoreB"] = scoreB
	new_donne = {'scoreA' : scoreA , 'scoreB' : scoreB}
	return jsonify(new_donne)



if __name__ == "__main__":
	app.run(debug = True , port = 80)


# je voulais importer aussi le render template pour afficher ses donnne dans la page web en question , mais.....
