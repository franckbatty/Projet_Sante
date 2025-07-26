-- CREATION DES TABLES DE LA COUCHE GOLD 
-- Cette couche consiste à créer des vues de tables de dimensions et la table de Fait à travers la couche Silver

-- Table de Dimension Patient
CREATE VIEW sante_gold.dim_patient as
(	SELECT patient.patient_id, patient.nom, patient.prenom, patient.sexe, patient.situation_matrimonial, patient.statut_professionel
	FROM sante_silver.patient
);
SELECT * FROM sante_gold.dim_patient;

-- Table de Dimension medecins
CREATE VIEW sante_gold.dim_medecins AS
(	SELECT medecins.medecin_id, medecins.nom_medecin, medecins.service_medical 
	FROM sante_silver.medecins
);
SELECT * FROM sante_gold.dim_medecins;

-- Table de Dimension diagnostics
CREATE VIEW sante_gold.dim_diagnostics AS
(
	SELECT diagnostics.diagnostic_id, diagnostics.gravite, diagnostics.etat_sortie 
	FROM sante_silver.diagnostics
);
SELECT * FROM sante_gold.dim_diagnostics;

-- Table de Fait consultation
CREATE VIEW sante_gold.Fait_consultation AS
(
	SELECT consul.consultation_id,
	   P.patient_id, 
	   M.medecin_id,
	   D.diagnostic_id,
	   consul.date_consultation, 
	   SUM(consul.frais_consultation)
FROM sante_silver.consultation AS consul
LEFT JOIN sante_silver.patient AS P ON consul.patient_id = P.patient_id
LEFT JOIN sante_silver.medecins AS M ON consul.medecin_id = M.medecin_id
LEFT JOIN sante_silver.diagnostics AS D ON consul.consultation_id = D.consultation_id
GROUP BY consul.consultation_id, P.patient_id, M.medecin_id, D.diagnostic_id, consul.date_consultation
);
SELECT * FROM sante_gold.Fait_consultation; 