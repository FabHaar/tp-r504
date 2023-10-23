#!/bin/bash
users=$(cat liste1.txt) 
for i in $users;
do
	userdel -r $i
done
