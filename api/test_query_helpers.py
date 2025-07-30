
#%%
# Tester les fonctions d'aide pour l'API RESTful
from database import SessionLocal
from query_helpers import *

# Créer une session
db = SessionLocal() 

#%%
# Tester la recupération d'une consultation par ses ID
consultation = get_consultation(db, consultation_id=2, patient_id=2, medecin_id=2, diagnostic_id=2)
print(f"consultation_id : {consultation.consultation_id}, patient_id : {consultation.patient_id}, medecin_id : {consultation.medecin_id}, diagnostic_id : {consultation.diagnostic_id}")

#%%
# Récupèrer une liste de consultation avec des filtres optionnels.
consultations = get_consultations(db, skip=0, limit=5)
for consultation in consultations: 
    print(f"consultation_id : {consultation.consultation_id}, patient_id : {consultation.patient_id}, medecin_id : {consultation.medecin_id}, diagnostic_id : {consultation.diagnostic_id}, date_consultation : {consultation.date_consultation}, frais consultation : {consultation.sum}")

#%%
# Récuperer un patient par son id
patient = get_patient(db, patient_id=2)
#print(patient)
print(f"patient_id : {patient.patient_id}, nom : {patient.nom}, prenom {patient.prenom}, sexe : {patient.sexe}, situation_matrimonial : {patient.situation_matrimonial}, statut_professionel : {patient.statut_professionel}")

#%%
# Recuperer la liste des patients
patients = get_patients(db, skip=0, limit=5)
for patient in patients: 
    print(f"patient_id : {patient.patient_id}, nom : {patient.nom}, prenom {patient.prenom}, sexe : {patient.sexe}, situation_matrimonial : {patient.situation_matrimonial}, statut_professionel : {patient.statut_professionel}")


# %%
# Recuperer un medecin par son ID
medecin = get_medecin(db, medecin_id=2)
print(f"medecin_id : {medecin.medecin_id}, nom_medecin : {medecin.nom_medecin}, service_medical : {medecin.service_medical}")

# %%
# Affichage de la liste des medecins
medecins = get_medecins(db, skip=0, limit=5)
for medecin in medecins:
    print(f"medecin_id : {medecin.medecin_id}, nom_medecin : {medecin.nom_medecin}, service_medical : {medecin.service_medical}")


# %%
## Recuperer un diagnostic à travers son ID
diagnostic = get_diagnostic(db, diagnostic_id=2)
#print(diagnostic)
print(f"diagnostic_id : {diagnostic.diagnostic_id}, gravite : {diagnostic.gravite}, etat_sortie : {diagnostic.etat_sortie}")

# %%
# Recuperer la liste de diagnostic
diagnostics = get_diagnostics(db, skip=0, limit=10)
for diagnostic in diagnostics:
   print(f"diagnostic_id : {diagnostic.diagnostic_id}, gravite : {diagnostic.gravite}, etat_sortie : {diagnostic.etat_sortie}")
 
# %%
