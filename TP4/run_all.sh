#!/bin/bash

#Script pour réaliser toutes les étapes du tp

#Etape 1 : création du réseau
./create_network.sh

if [ $? != 0 ]
then
	exit 1
fi

#Etape 2 : Création du conteneur mysql
./run_mysql.sh

if [ $? != 0 ]
then
	exit 2
fi

#Etape 3 : Création de contenu dans la base de données : 
sleep 60
./filldb.sh

if [ $? != 0 ]
then

	exit 3
fi

#Etape 4 : Construction de l'image pour l'application flask
./build2.sh

if [ $? != 0 ]
then
	exit 4
fi

#Etape 5 : Lancement du conteneur de l'application flask
./run_app2.sh

if [ $? != 0 ]
then
	exit 5
fi

#Terminé, vérifier avec un navigateur sur localhost:5000 que ça fonctionne
