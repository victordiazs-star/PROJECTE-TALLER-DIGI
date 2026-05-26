DROP DATABASE IF EXISTS taller;
CREATE DATABASE taller CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE taller;

CREATE TABLE clients (
    idClient INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    telefon VARCHAR(20) NOT NULL,
    correu VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE vehicles (
    idVehicle INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    model VARCHAR(80) NOT NULL,
    any_vehicle INT NOT NULL,
    idClient INT NOT NULL,
    FOREIGN KEY (idClient) REFERENCES clients(idClient)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE cites (
    idCita INT AUTO_INCREMENT PRIMARY KEY,
    data_cita DATE NOT NULL,
    hora_cita TIME NOT NULL,
    servei_sollicitat VARCHAR(150) NOT NULL,
    estat VARCHAR(30) NOT NULL DEFAULT 'Pendent',
    idClient INT NOT NULL,
    idVehicle INT NOT NULL,
    FOREIGN KEY (idClient) REFERENCES clients(idClient)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (idVehicle) REFERENCES vehicles(idVehicle)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO clients (nom, telefon, correu) VALUES
('Marc Garcia', '600111222', 'marc@exemple.cat'),
('Laia Torres', '600333444', 'laia@exemple.cat'),
('Pol Riera', '600555666', 'pol@exemple.cat');

INSERT INTO vehicles (matricula, model, any_vehicle, idClient) VALUES
('1234ABC', 'Seat Ibiza', 2018, 1),
('5678DEF', 'Volkswagen Golf', 2020, 2),
('9012GHI', 'Toyota Yaris', 2017, 3);

INSERT INTO cites (data_cita, hora_cita, servei_sollicitat, estat, idClient, idVehicle) VALUES
('2026-05-20', '09:30:00', 'Canvi d’oli', 'Pendent', 1, 1),
('2026-05-21', '11:00:00', 'Revisió general', 'Pendent', 2, 2);
