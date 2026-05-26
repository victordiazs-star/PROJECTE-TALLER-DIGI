# Projecte Taller Mecànic Connectat - ASIX 1

Aquest projecte digitalitza un petit taller mecànic amb una web, una API Flask, una base de dades MariaDB i contenidors Docker.

## Estructura

```text
projecte_taller_ASIX1/
├── api/
├── web/
├── scripts/
├── backups/
├── docs/
├── db_schema.sql
└── docker-compose.yml
```

## Posada en marxa

1. Obrir una terminal dins la carpeta del projecte.
2. Executar:

```bash
docker-compose up --build
```

3. Obrir la web:

```text
http://localhost:8080
```

4. Provar l'API:

```text
http://localhost:5000/vehicles
http://localhost:5000/appointments
http://localhost:5000/health
```

## Scripts

Fer una còpia de seguretat:

```bash
bash scripts/backup.sh
```

Comprovar serveis:

```bash
bash scripts/check_services.sh
```

Aturar el projecte:

```bash
docker-compose down
```
