#!/bin/bash

echo "Comprovant contenidors del projecte..."
echo "-------------------------------------"

docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep taller

echo ""
echo "Comprovant API..."
if curl -s http://localhost:5000/health > /dev/null; then
    echo "API OK: http://localhost:5000/health respon correctament"
else
    echo "API KO: no respon"
fi

echo ""
echo "Comprovant base de dades..."
if docker exec taller_db mysqladmin ping -uroot -pexample --silent; then
    echo "MariaDB OK"
else
    echo "MariaDB KO"
fi

echo ""
echo "Comprovant web..."
if curl -s http://localhost:8080 > /dev/null; then
    echo "WEB OK: http://localhost:8080 respon correctament"
else
    echo "WEB KO: no respon"
fi
