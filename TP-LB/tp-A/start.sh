#!/bin/bash

docker build -t im-nginx-lb .

mkdir shared1
mkdir shared2

echo "<h1>Hello 1</h1>" > shared1/index.html
echo "<h1>Hello 2</h1>" > shared2/index.html

docker run -d \
	-p 81:80 \
	--mount type=bind,source=$(pwd)/shared1,target=/usr/share/nginx/html \
	--name nginx1 \
	nginx

docker run -d \
	-p 82:80 \
	--mount type=bind,source=$(pwd)/shared2,target=/usr/share/nginx/html \
	--name nginx2 \
	nginx

docker run -d \
	-p 83:80 \
	--name nginx3 \
	im-nginx-lb 
