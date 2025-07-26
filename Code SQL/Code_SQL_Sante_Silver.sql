-- CREATION DES TABLES DE LA COUCHE SILVER --

-- Table patient
CREATE TABLE sante_silver.patient (
    patient_id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
	sexe VARCHAR(250) NOT NULL,
	age INT NOT NULL,
	situation_matrimonial VARCHAR(250) NOT NULL,
	statut_professionel VARCHAR(250) NOT NULL,
    date_naissance DATE NOT NULL,
    Telephone VARCHAR(250) NOT NULL
);
SELECT * FROM sante_silver.patient;
SELECT COUNT(*) FROM sante_silver.patient;

-- Table medecins
CREATE TABLE sante_silver.medecins (
    medecin_id INT PRIMARY KEY,
    nom_medecin VARCHAR(100) NOT NULL,
    service_medical VARCHAR(50) NOT NULL
);
SELECT * FROM sante_silver.medecins;
SELECT COUNT(*) FROM sante_silver.medecins;

-- Table consultation
CREATE TABLE sante_silver.consultation (
    consultation_id INT PRIMARY KEY,
    patient_id INT NOT NULL,
    date_consultation DATE NOT NULL,
    type_consultation VARCHAR (50) NOT NULL,
    service_medical VARCHAR(50) NOT NULL,
    frais_consultation INT NOT NULL,
    medecin_id INT NOT NULL,
	FOREIGN KEY (patient_id) REFERENCES sante_silver.patient(patient_id),
	FOREIGN KEY (medecin_id) REFERENCES sante_silver.medecins(medecin_id)
	
);
SELECT * FROM sante_silver.consultation;
SELECT COUNT(*) FROM sante_silver.consultation;
-- affichage de la somme de consultation par type_consultation 
SELECT type_consultation, SUM(frais_consultation) Consultation_Totale
FROM sante_silver.consultation
GROUP BY type_consultation;
-- Table diagnostics
CREATE TABLE sante_silver.diagnostics (
    diagnostic_id INT PRIMARY KEY,
    consultation_id INT NOT NULL,
    gravite VARCHAR(50) NOT NULL,
    etat_sortie VARCHAR(50) NOT NULL,
    FOREIGN KEY (consultation_id) REFERENCES sante_silver.consultation(consultation_id)
);
SELECT * FROM sante_silver.diagnostics;
SELECT COUNT(*) FROM sante_silver.diagnostics;
-- Table Traitement
CREATE TABLE sante_silver.Traitements (
    traitement_id INT PRIMARY KEY,
    diagnostic_id INT NOT NULL,
    traitement_prescrit TEXT NOT NULL,
    duree_traitement INT NOT NULL,
    FOREIGN KEY (diagnostic_id) REFERENCES sante_silver.diagnostics(diagnostic_id)
);
SELECT * FROM sante_silver.Traitements;
SELECT COUNT(*) FROM sante_silver.Traitements;