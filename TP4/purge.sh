#!/bin/bash

#Q2.1
#stop tous les conteneurs
docker stop $(docker ps -aq)

#supprime tous les conteneurs
docker rm $(docker ps -aq)

#2.2
#supprime les volumes
docker volume prune

#supprimme les réseaux
docker network prune
