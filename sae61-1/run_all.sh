#!/bin/bash


# étape d'initialisation
#read -p "Do you want to proceed a purge ? (y/n) " yn

#case $yn in 
#	[yY] ) echo ok, we will proceed a purge;
#	      ./purge.sh;;
#	[nN] ) echo ok maybe later...;
#		exit;;
#	* ) echo invalid response;
#		exit 1;;
#esac


#if [ $? != 0 ] 
#then
#	echo "echec d'initialisation : étape initialisation"
#	exit 1
#fi



#Etape 1 : lancement du serveur mysql
	./run_mysql.sh


#Etape 2 : Construction de l'image pour l'application flask
	./build.sh


	if [ $? != 0 ]
	then
		echo "échec de creation de l'image à partir du Dockerfile : étape 2"
		exit 1
	fi
	
#Etape 3 : Lancement du conteneur de l'application flask
	./run_app.sh
	
	
	if [ $? != 0 ]
	then
		echo "échec de lancement du conteneur app : étape 3"
		exit 1
	fi


## Etape 4 : Résultat
# Ouvre la page http://localhost:5000/ dans le navigateur par défaut
	xdg-open http://localhost:5000/ 2>/dev/null


	if [ $? != 0 ]
	then
		echo "échec de lancement du navigateur, veuillez ouvrir la page http://localhost:5000/ dans votre navigateur "
		exit 1
	fi
