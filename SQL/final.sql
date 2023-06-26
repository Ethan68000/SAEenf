drop database if exists final;

create database final;

use final;

CREATE TABLE `capteur` (
  `id_capteur` varchar(100) Primary key,
  `PIECE` varchar(40) DEFAULT NULL
)  DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `details` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_capteur` varchar(100) DEFAULT NULL,
  `PIECE` varchar(40) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `temp` float(4,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_id_capteur` (`id_capteur`),
  FOREIGN KEY (`id_capteur`) REFERENCES `capteur` (`id_capteur`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;