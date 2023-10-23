#!/bin/bash
while read v_nom v_passwd
do
	echo "nom=$v_nom passwd=$v_passwd" 
	adduser --disabled-password --gecos "" $v_nom
	echo "$v_nom":"$v_passwd" | chpasswd
done < liste2.txt
