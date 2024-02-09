import fonctions
from flask import Flask, render_template, request

app = Flask(__name__)

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
	message_mdp = ''

	if request.method == 'POST':                                       # En attente d'une requête de type POST
		username = request.form['username']                        # Récupère l'identifiant saisi dans le formulaire HTML
		email = request.form['email']                              # Récupère l'email saisi dans le formulaire HTML
		password = request.form['password']                        # Récupère le mot de passe saisi dans le formulaire HTML
		
		validation = fonctions.validate_password(password)                   #rempli la variable validation avec tout ce qu'il faut pour le traitement de chaque critère selon password
		
		check_p = True	#initilaisation d'un compteur qui servira à valider si toutes les regex sont respectées
		message_mdp ="Le mot de passe ne respecte pas les criteres suivants : "			
		if not validation[0]:
			check_p = False
			message_mdp = message_mdp + "Entre 6 et 15 caracteres "
		if not validation[1]:
			check_p = False
			message_mdp = message_mdp + "Au moins un chiffre "
		if not validation[2]:
			check_p = False
			message_mdp = message_mdp + "Au moins une minuscule"
		if not validation[3]:
			check_p = False
			message_mdp = message_mdp + "Au moins une majuscule "
		if not validation[4]:
			check_p = False
			message_mdp = message_mdp + "Au moins un de ces caractères : #%{}@"
		
		if check_p:
			message_mdp = "Mot de passe valide"
		
		
		#if validate_username(username) and validate_email(email) and validate_password(password):  # Valide les champs
    
	return render_template('newuser.html', message_mdp=message_mdp)            # Renvoie la page HTML 'newuser.html' avec le message à afficher


	
@app.route('/liste')
def liste():
	pass
@app.route('/connect')
def connect():
	pass



# Point d'entrée pour l'exécution de l'application Flask
if __name__ == '__main__':
	app.run(debug=True)
