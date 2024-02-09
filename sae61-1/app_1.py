import mysql.connector
import re
from flask import Flask, render_template, request

app = Flask(__name__)

def validate_password(password):
	regex1 = r"^.{6,15}$" #entre 6 et 15 caractères
	regex2 = r".*\d.*" #au moins un chiffre
	regex3 = r".*[a-z].*" #au moins une minuscule
	regex4 = r".*[A-Z].*" #au moins une majuscule
	regex5 = r".*[#%{}@].*" #au moins un de ces caractères
	
	tab_validation = [bool(re.match(regex1, password)), bool(re.match(regex2, password)), bool(re.match(regex3, password)), bool(re.match(regex4, password)), bool(re.match(regex5, password))]
	return tab_validation	
#Config mysql-------------------------------------------
db_config = {
	'host': 'serveur-mysql',
	'user': 'python',
	'password': 'python',
	'database': 'sae61',
	'port': '3306'
}

def sql_insert(query):
	# Connexion à la bdd
	conn = mysql.connector.connect(**db_config)
	cursor = conn.cursor()
	
	#Execution de la requete
	cursor.execute(query)
    
	#fin de connexion
	cursor.close()
	conn.close()
    
def sql_select(query):
	# Connexion à la bdd
	conn = mysql.connector.connect(**db_config)
	cursor = conn.cursor()
	
	#Execution de la requete
	cursor.execute(query)
	#Recuperation du select
	data = cursor.fetchall()
	
	#fin de connexion
	cursor.close()
	conn.close()
	return data

# Fin config mysql --------------------------------------

# Route pour la page d'accueil
@app.route('/')
def index():
	return """
	<h1>Accueil</h1>
	<p>Bienvenue sur notre site !</p>
	<p>Pour créer un nouveau compte, veuillez accéder à la <a href="/newuser">page de création de compte</a>.</p>
	"""


# Route pour la page de création de nouveau compte
@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
	message = ''

	if request.method == 'POST':                                       # En attente d'une requête de type POST
		username = request.form['username']                        # Récupère l'identifiant saisi dans le formulaire HTML
		email = request.form['email']                              # Récupère l'email saisi dans le formulaire HTML
		password = request.form['password']                        # Récupère le mot de passe saisi dans le formulaire HTML
		
		validation = validate_password(password)                   #rempli la variable validation avec tout ce qu'il faut pour le traitement de chaque critère selon password
		
		i = 0	#initilaisation d'un compteur qui servira à valider si toutes les regex sont respectées
		message="Le mot de passe ne respecte pas les criteres suivants : "			
		if validation[0]:
			i = i+1
		else:
			message = message + "Entre 6 et 15 caracteres "
		if validation[1]:
			i = i+1
		else:
			message = message + "Au moins un chiffre "
		if validation[2]:
			i = i+1
		else:
			message = message + "Au moins une minuscule"
		if validation[3]:
			i = i+1
		else:
			message = message + "Au moins une majuscule "
		if validation[4]:
			i = i+1
		else:
			message = message + "Au moins un de ces caractères : #%{}@"
		
		if i==5:
			message = "Mot de passe valide"
		
		
		#if validate_username(username) and validate_email(email) and validate_password(password):  # Valide les champs
    
	return render_template('newuser.html', message=message)            # Renvoie la page HTML 'newuser.html' avec le message à afficher


	
@app.route('/liste')
def liste():
	pass
@app.route('/connect')
def connect():
	pass



# Point d'entrée pour l'exécution de l'application Flask
if __name__ == '__main__':
	app.run(debug=True)
