#!/bin/bash
cd $(dirname $0)/..

docker run --env POSTGRES_USER=postgres --env POSTGRES_PASSWORD=postgres -p 5432:5432 -v $(pwd)/postgres/sql/create_tables.sql:/docker-entrypoint-initdb.d/create_tables.sql --name create_schema -d postgres:10.5

while ! sqlacodegen postgresql://postgres:postgres@localhost:5432/postgres --outfile server/database/schema.py 2> /dev/null
do
	echo waiting
	sleep 2
done

docker stop create_schema
docker rm create_schema
