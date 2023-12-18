#!/bin/bash

chemin="$1"

ok="/"

if [ -e "$chemin" ]; then
    echo "chemin valide"
    
else
	IFS="/"; read -a chemins <<< "$chemin"
	for (( i=1; i<"${chemins[@]"; i++ )) 
	do
		echo "OUI"
	done
    echo "chemin invalide"
fi
