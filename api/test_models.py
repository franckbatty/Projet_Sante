# Tester les class de models
# importation des modules nécessaires
#%%
from database import SessionLocal
from models import Consultation, PatientDim, MedecinDim, DiagnosticDim

db = SessionLocal()

#%%
# Tester la recuperation de quelques consultations
consultations = db.query(Consultation).limit(5).all()
for consultation in consultations:
    print(f"consultation_id : {consultation.consultation_id}, patient_id : {consultation.patient_id}, medecin_id : {consultation.medecin_id}, diagnostic_id : {consultation.diagnostic_id}, date_consultation : {consultation.date_consultation}, Frais : {consultation.sum} ")

# %%
# affichage de quelques patients 
patients = db.query(PatientDim).limit(5).all()
for patient in patients:
    print(f"patient_id : {patient.patient_id}, nom : {patient.nom}, prenom : {patient.prenom}, sexe : {patient.sexe}, situation_matrimonial : {patient.situation_matrimonial}, statut_professionel : {patient.statut_professionel}")

# %%
# Affichage de quelques medecins
medecins = db.query(MedecinDim).limit(5)

for medecin in medecins:
    print(f"medecin_id : {medecin.medecin_id}, nom_medecin : {medecin.nom_medecin}, service_medical : {medecin.service_medical}")

# %%
# Affichage de quelques information de : Diagnostic
diagnostics = db.query(DiagnosticDim).limit(5)

for diagnostic in diagnostics:
    print(f"diagnostic_id : {diagnostic.diagnostic_id}, gravite : {diagnostic.gravite}, etat_sortie : {diagnostic.etat_sortie}")

# %%
# Affichage des patients qui ont une consultation > 75000

m = (
    db.query(PatientDim.nom, PatientDim.prenom, Consultation.sum)
       .join(Consultation, PatientDim.patient_id == Consultation.patient_id)
        .filter(Consultation.sum > 75000)
        .limit(5)
        )

for i in m:
    print(f"nom : {i.nom}, prenom : {i.prenom}, somme : {i.sum}")

# %%
