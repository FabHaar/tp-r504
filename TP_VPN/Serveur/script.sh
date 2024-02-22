#!/bin/bash

openssl genrsa 2048 > ca-key.pem

opensll req -new -x509 -nodes -days 365000 \
	-key ca-key.pem \
	-out ca-cert.pem
	
openssl req -newkey rsa:2048 -nodes -days 365000 \
	-keyout server-key.pem \
	-out server-req.pem
	
openssl x509 -req -days 365000 -set_serial 01 \
	-in server-req.pem \
	-out server-cert.pem \
	-CA ca-cert.pem \
	-CAkey ca-key.pem
	
openssl verify -CAfile ca-cert.pem \
	ca-cert.pem \
	server-cert.pem

openvpn genkey secret ta.key

openssl dhparams -out dhparams.pem 2048

scp ca-cert.pem haar@192.168.0.11:/home/haar/ca-cert.pem
