#!/bin/bash
users=$(cat liste1.txt) 
groupadd t_users
for i in $users;
do
	adduser --disabled-password --gecos "" $i
	usermod -G t_users $i
done
