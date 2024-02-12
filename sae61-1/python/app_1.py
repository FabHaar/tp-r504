import fonctions
#import argon2
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

# Route pour la page d'accueil
@app.route('/')
def index():
	return render_template('index.html')


# Route pour la page de création de nouveau compte
@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
	message_mdp = ''
	message_email = ''
	message_username = ''
	
	if request.method == 'POST':                                       # En attente d'une requête de type POST
		username = request.form['username']                        # Récupère l'identifiant saisi dans le formulaire HTML
		email = request.form['email']                              # Récupère l'email saisi dans le formulaire HTML
		password = request.form['password']                        # Récupère le mot de passe saisi dans le formulaire HTML
		
		validation_mdp = fonctions.validate_password(password)                   #rempli la variable validation avec tout ce qu'il faut pour le traitement de chaque critère selon password
		
		check_p = True	#initilaisation d'un compteur qui servira à valider si toutes les regex sont respectées
		message_mdp ="Le mot de passe ne respecte pas les criteres suivants : "			
		if not validation_mdp[0]:
			check_p = False
			message_mdp = message_mdp + "Entre 6 et 15 caracteres "
		if not validation_mdp[1]:
			check_p = False
			message_mdp = message_mdp + "Au moins un chiffre "
		if not validation_mdp[2]:
			check_p = False
			message_mdp = message_mdp + "Au moins une minuscule"
		if not validation_mdp[3]:
			check_p = False
			message_mdp = message_mdp + "Au moins une majuscule "
		if not validation_mdp[4]:
			check_p = False
			message_mdp = message_mdp + "Au moins un de ces caractères : #%{}@"
		
		if check_p:
			message_mdp = "Mot de passe valide"
		
		validation_username = fonctions.validate_username(username)
		check_u = True
		
		message_username = "Le username respecte pas les criteres suivants : "
		if not validation_username[0] :
			message_username = message_username + "Entre 6 et 10 caractères "
			check_u = False
		if not validation_username[1] :
			message_username = message_username + "Pas de majuscule "
			check_u = False
		if not validation_username[2] :
			message_username = message_username + "Doit conbtenir seulement des caractères alphanumérique ascii"
			check_u = False
		
		if check_u:
			message_username = "Username valide"

		check_e = fonctions.validate_email(email)
		message_email = "email valide"
		
		if not check_e :
			message_email = "email non valide"
		
		if check_u and check_p and check_e:
			hashed_password = fonctions.hash_password(password)
			query = "INSERT INTO utilisateurs (identifiant, email, password) VALUES ('{}', '{}', '{}')"
			query = query.format(username, email, hashed_password)
			
			fonctions.sql_insert(query)

	return render_template('newuser.html', message_mdp=message_mdp, message_email=message_email, message_username=message_username)            # Renvoie la page HTML 'newuser.html' avec le message à afficher


	
@app.route('/liste')
def liste():
	data = fonctions.sql_select("SELECT identifiant FROM utilisateurs")
	return render_template('liste.html', data=data)

@app.route('/connect')
def connect():
	return render_template('connect.html')



# Point d'entrée pour l'exécution de l'application Flask
if __name__ == '__main__':
	app.run(debug=True)
