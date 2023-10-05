#!/bin/bash

docker run -d -it\
		-p 5000:5000 \
		--name tp4-app \
		--network net-tp4 \
		im-tp4
