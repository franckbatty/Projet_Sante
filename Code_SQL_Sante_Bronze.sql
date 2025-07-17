---- *** CREATION DES TABLES *** ----

-- TABLE CONSULTATION
CREATE TABLE sante_bronze.consultation
(
	consultation_id INT,
	patient_id INT,
	date_consultation VARCHAR(250),
    motif_consultation VARCHAR(250),
	type_consultation VARCHAR(250),
	service_médical VARCHAR(250),
    frais_consultation VARCHAR(250),
	medecin_id INT
);

SELECT * FROM sante_bronze.consultation;

SELECT COUNT(*) FROM sante_bronze.consultation;

--- TABLE DIAGNOSTICS
CREATE TABLE sante_bronze.DIAGNOSTICS
(
	diagnostic_id int, 
 	consultation_id int, 
 	diagnostic VARCHAR(250),
 	gravité VARCHAR(250),
 	état_sortie VARCHAR(250)
);
SELECT * FROM sante_bronze.DIAGNOSTICS;
SELECT COUNT(*) FROM sante_bronze.DIAGNOSTICS;

--- TABLE PATIENT
CREATE TABLE sante_bronze.patient
(
	patient_id int, 
 	nom VARCHAR(250),
 	prenom VARCHAR(250),
 	sexe VARCHAR(250),
 	age int, 
 	situation_matrimonial VARCHAR(250),
 	statut_professionel VARCHAR(250),
 	date_naissance VARCHAR(250),
 	Telephone VARCHAR(250)
);
SELECT * FROM sante_bronze.patient;
SELECT COUNT(*) FROM sante_bronze.patient;
--- TABLE TRAITEMENTS
CREATE TABLE sante_bronze.traitement
(
	traitement_id int, 
 	diagnostic_id int, 
 	traitement_prescrit VARCHAR(250),
 	durée_traitement_jours int
);

SELECT * FROM sante_bronze.traitement;
SELECT COUNT(*) FROM sante_bronze.patient;

--- TABLE MEDECINS
CREATE TABLE sante_bronze.medecins
(
	medecin_id int,
	nom_medecin VARCHAR(250),
 	service_medical VARCHAR(250)
); 

SELECT * FROM sante_bronze.medecins