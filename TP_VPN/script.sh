#!/bin/bash

openssl req -newkey rsa:2048 -nodes -days 365000 \
	-keyout client-key.pem \
	-out client-req.pem
	
openssl x509 -req -days 365000 -set_serial 01 \
	-in client-req.pem \
	-out client-cert.pem \
	-CA ca-cert.pem \
	-CAkey ca-key.pem
	
openssl verify -CAfile ca-cert.pem \
	ca-cert.pem \
	client-cert.pem
