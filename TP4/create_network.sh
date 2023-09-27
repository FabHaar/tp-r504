#!/bin/bash

#2.3 créer le réseau net-tp4 en mode bridge
docker network create -d bridge net-tp4

error=$?

if [ $error != 0 ]
then
	exit $error
fi
