#!/bin/bash

docker run --rm -d \
		-p 3306:3306 \
		-v vol-sql-demo:/var/lib/mysql \
		--name serveur-mysql \
		--env MYSQL_ROOT_PASSWORD=foo \
		--env MYSQL_DATABASE=sae61 \
		--network net-sae61 \
		mysql

echo "attente de securite pour acceder au serveur mysql"
sleep 15

mysql -u root -p'foo' -h 127.0.0.1 --port=3306 sae61 < "sql/sae61.sql" 2> /dev/null
