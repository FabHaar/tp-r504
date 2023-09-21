#!/bin/bash

lettre="$1"

for fichier in /etc/$lettre*; 
do
    if [ -f "$fichier" ]; 
    then
        type_fichier=$(file -b "$fichier")
        echo "Fichier: $fichier - Type: $type_fichier"
    fi
done

