#!/bin/bash

#stop tous les conteneurs
docker stop $(docker ps -aq)

#supprime tous les conteneurs
docker rm $(docker ps -aq)
