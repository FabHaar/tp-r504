#!/bin/bash

hello1=0
hello2=0

for ((i=1; i<=500; i++))
do
	lecurl=$(curl localhost:83)
	if [ "$lecurl" == "<h1>Hello 1</h1>" ];
	then
		hello1=$((hello1 + 1))
	else
		hello2=$((hello2 + 1))
	fi
done

echo "hello 1 : $hello1"
echo "hello 2 : $hello2"
