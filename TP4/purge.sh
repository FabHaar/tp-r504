#!/bin/bash

#2.1
#stop tous les conteneurs
docker stop $(docker ps -aq)

error=$?
if [ $error != 0 ]
then
	exit $error
fi

#supprime tous les conteneurs
docker rm $(docker ps -aq)
error=$?
if [ $error != 0 ]
then
	exit $error
fi

#2.2
#supprime les volumes
docker volume prune
error=$?
if [ $error != 0 ]
then
	exit $error
fi

#supprimme les réseaux
docker network prune
error=$?
if [ $error != 0 ]
then
	exit $error
fi
