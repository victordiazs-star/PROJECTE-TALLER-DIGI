from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
import time
from datetime import date, datetime, time as dt_time, timedelta

app = Flask(__name__)
CORS(app)


def connect_db():
    """Connexió simple amb MariaDB."""
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "db"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ.get("DB_PASSWORD", "example"),
        database=os.environ.get("DB_NAME", "taller")
    )


def preparar_json(files):
    """Converteix dates i hores de MariaDB a text perquè Flask les pugui retornar en JSON."""
    for fila in files:
        for camp, valor in list(fila.items()):
            if isinstance(valor, timedelta):
                segons = int(valor.total_seconds())
                hores = segons // 3600
                minuts = (segons % 3600) // 60
                fila[camp] = f"{hores:02d}:{minuts:02d}"
            elif isinstance(valor, (date, datetime, dt_time)):
                fila[camp] = str(valor)
    return files


def query_db(sql, params=None, one=False):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql, params or ())
    result = cursor.fetchone() if one else cursor.fetchall()
    cursor.close()
    db.close()
    return result


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API del taller funcionant"})


@app.route("/health", methods=["GET"])
def health():
    try:
        db = connect_db()
        db.close()
        return jsonify({"api": "ok", "database": "ok"})
    except Exception as error:
        return jsonify({"api": "ok", "database": "error", "detail": str(error)}), 500


@app.route("/clients", methods=["GET"])
def get_clients():
    clients = query_db("SELECT * FROM clients ORDER BY idClient")
    return jsonify(clients)


@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    sql = """
        SELECT v.idVehicle, v.matricula, v.model, v.any_vehicle,
               c.idClient, c.nom AS client
        FROM vehicles v
        INNER JOIN clients c ON v.idClient = c.idClient
        ORDER BY v.idVehicle
    """
    vehicles = query_db(sql)
    return jsonify(vehicles)


@app.route("/appointments", methods=["GET"])
def get_appointments():
    sql = """
        SELECT ci.idCita, ci.data_cita, ci.hora_cita,
               ci.servei_sollicitat, ci.estat,
               c.nom AS client, v.matricula, v.model
        FROM cites ci
        INNER JOIN clients c ON ci.idClient = c.idClient
        INNER JOIN vehicles v ON ci.idVehicle = v.idVehicle
        ORDER BY ci.data_cita, ci.hora_cita
    """
    cites = query_db(sql)
    cites = preparar_json(cites)
    return jsonify(cites)


@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()

    camps_obligatoris = ["idClient", "idVehicle", "data_cita", "hora_cita", "servei_sollicitat"]
    for camp in camps_obligatoris:
        if camp not in data or data[camp] == "":
            return jsonify({"message": f"Falta el camp {camp}"}), 400

    db = connect_db()
    cursor = db.cursor()
    sql = """
        INSERT INTO cites (data_cita, hora_cita, servei_sollicitat, idClient, idVehicle)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        data["data_cita"],
        data["hora_cita"],
        data["servei_sollicitat"],
        data["idClient"],
        data["idVehicle"]
    )
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Cita creada correctament"}), 201


if __name__ == "__main__":
    # Petita espera perquè MariaDB tingui temps d'arrencar dins Docker.
    time.sleep(5)
    app.run(host="0.0.0.0", port=5000, debug=True)
