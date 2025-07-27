# importation des modules nécessaires
#%%
from database import SessionLocal
from models import Consultation, PatientDim, MedecinDim, DiagnosticDim

db = SessionLocal()

#%%
# Tester la recuperation de quelques consultations
consultations = db.query(Consultation).limit(10).all()
for consultation in consultations:
    print(f"consultation_id : {consultation.consultation_id}, patient_id : {consultation.patient_id}, medecin_id : {consultation.medecin_id}, diagnostic_id : {consultation.diagnostic_id}, date_consultation : {consultation.date_consultation}, Frais : {consultation.sum} ")

# %%
# affichage de quelques patients
patients = db.query(PatientDim).limit(5).all()
for patient in patients:
    print(f"patient_id : {patient.patient_id}, nom : {patient.nom}, prenom : {patient.prenom}, sexe : {patient.sexe}, situation_matrimonial : {patient.situation_matrimonial}, statut_professionel : {patient.statut_professionel}")

# %%
