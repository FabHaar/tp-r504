#!/bin/bash

#2.1
#stop tous les conteneurs
docker stop $(docker ps -aq)
if [ $? != 0 ]
then
	exit 1
fi

#supprime tous les conteneurs
docker rm $(docker ps -aq)
if [ $? != 0 ]
then
	exit 2
fi

#2.2
#supprime les volumes
docker volume prune
if [ $? != 0 ]
then
	exit 3
fi

#supprimme les réseaux
docker network prune
if [ $? != 0 ]
then
	exit 4
fi
