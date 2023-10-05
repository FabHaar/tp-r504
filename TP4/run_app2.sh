#!/bin/bash

docker run -d -it\
		-p 5000:5000 \
		--name tp4-app \
		--network net-tp4 \
		--mount type=bind,source="$(pwd)"/app_1.py,target=/srv/app_1.py \
		im-tp4
