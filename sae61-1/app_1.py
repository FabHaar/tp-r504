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
