# Guió de presentació (8-10 minuts)

## 1. Introducció
Bon dia, el nostre projecte és la digitalització d’un taller mecànic petit. Abans el taller gestionava clients, vehicles i cites en paper, i ara ho fem amb una web, una API, una base de dades i Docker.

## 2. Objectiu
L’objectiu és que el client pugui demanar cita online i que el taller tingui totes les dades guardades de forma ordenada.

## 3. Base de dades
Hem creat tres taules: clients, vehicles i cites. Un client pot tenir diversos vehicles i cada vehicle pot tenir diverses cites.

## 4. API Flask
L’API està feta amb Python Flask. Té rutes per consultar clients, vehicles i cites, i també una ruta POST per crear cites noves.

## 5. Web
La web està feta amb HTML, CSS i JavaScript. Té un formulari per demanar cita i fa peticions fetch a l’API.

## 6. Docker
Tenim tres contenidors: MariaDB, API Flask i web amb Nginx. Tots estan connectats amb una xarxa Docker pròpia.

## 7. Scripts
El script backup.sh fa una còpia de seguretat de la base de dades. El script check_services.sh comprova si els serveis funcionen.

## 8. Demo
1. Executar docker-compose up --build.
2. Obrir http://localhost:8080.
3. Crear una cita nova.
4. Comprovar http://localhost:5000/appointments.
5. Executar bash scripts/backup.sh.
6. Executar bash scripts/check_services.sh.

## 9. Conclusions
Amb aquest projecte hem après a connectar una web amb una API, una API amb una base de dades i a desplegar-ho tot amb Docker.
