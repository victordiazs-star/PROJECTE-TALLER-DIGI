#!/bin/bash

DATA=$(date +%Y%m%d_%H%M%S)
CARPETA="backups"
FITXER="$CARPETA/backup_taller_$DATA.sql"

mkdir -p $CARPETA

echo "Fent còpia de seguretat de la base de dades..."
docker exec taller_db sh -c 'mysqldump -uroot -pexample taller' > $FITXER

if [ $? -eq 0 ]; then
    echo "Backup creat correctament: $FITXER"
else
    echo "Error fent el backup"
fi
