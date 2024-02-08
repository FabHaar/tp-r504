import re
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
	message = ''

	if request.method == 'POST':                                       # En attente d'une requête de type POST
	     	username = request.form['username']                        # Récupère l'identifiant saisi dans le formulaire HTML
		email = request.form['email']                              # Récupère l'email saisi dans le formulaire HTML
		password = request.form['password']                        # Récupère le mot de passe saisi dans le formulaire HTML
		#LeReturn = validate_password(password)
		#if validate_username(username) and validate_email(email) and validate_password(password):  # Valide les champs
		#    message = 'Données valides !'
		if validate_password(password):                            # Valide le mot de passe en utilisant la fonction validate_password
			message = 'Mot de passe valide !'
		else:
			message = 'Le mot de passe doit contenir au moins 6 caractères, au moins 1 chiffre, une majuscule et une minuscule.'
    
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
