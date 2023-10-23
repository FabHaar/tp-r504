#!/bin/bash

function creation {
	adduser --disabled-password --gecos "" $1
	echo "$1":"$2" | chpasswd
}

while IFS=";" read v_nom v_passwd
do
	passwd=$(pwgen --num-passwords=1)
	echo "nom=$v_nom passwd=$passwd" 
	
	creation $v_nom $passwd
done < liste3.txt
