#!/bin/bash

docker run --rm -d \
		-p 3306:3306 \
		-v vol-sql-demo:/var/lib/mysql \
		--name serveur-mysql \
		--env MYSQL_ROOT_PASSWORD=foo \
		--env MYSQL_USER=python \
		--env MYSQL_PASSWORD=python \
		--network net-sae61 \
		mysql

		# ne fonctionne pas--env MYSQL_DATABASE=sae61 \

echo "attente de securite pour acceder au serveur mysql"
sleep 15

mysql -u root -p'foo' -h 127.0.0.1 --port=3306 < "sql/sae61.sql" 2> /dev/null

if [ $? != 0 ]
	then
		echo "échec d'import de la BDD"
		exit 1
	fi
