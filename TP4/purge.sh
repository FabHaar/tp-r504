#!/bin/bash

#2.1
#stop tous les conteneurs
docker stop $(docker ps -aq)
if [ $? != 0 ]
then
	echo "erreur sur docker stop"
fi

#supprime tous les conteneurs
docker rm $(docker ps -aq)
if [ $? != 0 ]
then
	echo "erreur sur docker rm"
fi

#2.2
#supprime les volumes
docker volume prune
if [ $? != 0 ]
then
	echo "erreur sur docker volume prune"
fi

#supprimme les réseaux
docker network prune
if [ $? != 0 ]
then
	echo "erreur sur docker network prune"
fi
