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
	
# Config mysql-------------------------------------------
db_config = {
    'host': 'serveur-mysql',
    'user': 'root',
    'password': 'foo',
    'database': 'sae61',
	'port': '3306'
}
# Connexion à la bdd
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
# Fin config mysql --------------------------------------

# Route pour la page d'accueil
@app.route('/')
def index():
    return """
    <h1>Accueil</h1>
    <p>Bienvenue sur notre site !</p>
    <p>Pour créer un nouveau compte, veuillez accéder à la <a href="/newuser">page de création de compte</a>.</p>
    """

@app.route('/newuser')
def newuser():
	#return render_template('newuser.html')
	#return render_template('index.html')
	
	
@app.route('/liste')
def liste():
	
@app.route('/connect')
def connect():




# Point d'entrée pour l'exécution de l'application Flask
if __name__ == '__main__':
	app.run(debug=True)
