#!/bin/bash

PS3='Entrer votre choix : '
options=("1" "2" "q")

select opt in "${options[@]}"
do
	case $opt in
		"1")
			echo "Entrer le nom utilisateur à trouver : "
			read utilisateur
			result=$(cat /etc/passwd | grep "$utilisateur"*)
	
			if [ $? -eq 0 ]; 
			then
				echo "l utilisateur existe"
				echo "$result"
			else
				echo "l utilisateur n'existe pas"
			fi
			;;
		"2")
			echo "Entrer le nom utilisateur avec id à connaitre : "
			read utilisateur
			result=$(id -u $utilisateur)
	
			if [ $? -eq 0 ]; 
			then
				echo "$result"
			else
				echo "l utilisateur n'existe pas"
			fi
			;;
		"q")
			break
			;;
		*) echo "invalid option $REPLY" ;;
	esac
done
