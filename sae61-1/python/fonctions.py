import mysql.connector
import re

def validate_password(password):
	regex1 = r"^.{6,15}$" #entre 6 et 15 caractères
	regex2 = r".*\d.*" #au moins un chiffre
	regex3 = r".*[a-z].*" #au moins une minuscule
	regex4 = r".*[A-Z].*" #au moins une majuscule
	regex5 = r".*[#%{}@].*" #au moins un de ces caractères
	
	tab_validation = [bool(re.match(regex1, password)), bool(re.match(regex2, password)), bool(re.match(regex3, password)), bool(re.match(regex4, password)), bool(re.match(regex5, password))]
	return tab_validation

def validate_username(uesername):
	regex1 = r"^.{6,10}$" #entre 6 et 10 caractères
	regex2 = r"^[^A-Z]*$" #Pas de majuscule
	regex3 = r"^[a-z0-9]*$" #Seulement les caractères alphanumrique ascii à revoir pour celle là
	
	tab_validation = [bool(re.match(regex1, username)), bool(re.match(regex2, username)), bool(re.match(regex3, username))]
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
