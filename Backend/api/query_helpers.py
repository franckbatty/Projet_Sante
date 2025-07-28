## == API Restful pour la Sante == ##
# Developpement des fonctions d'aide pour mon API RESTful

# Importation des modules nécessaires
from sqlalchemy.orm import Session # pour interagir avec la base de données
from sqlalchemy.orm import joinedload # permet de charger les relations en une seule requête pour éviter les requêtes N+1
from typing import Optional # pour les types optionnels c'est-à-dire les paramètres qui peuvent être None

import models

# Consultation 
# Récupèrer une consultation par son id : consultation_id de consultation, patient_id de patient, medecin_id de medecin et diagnostic_id de diagnostic.
def get_consultation(db:Session,consultation_id=int, patient_id=int, medecin_id=int, diagnostic_id=int):
    """ Recupère une consultation à travers son id : consultation_id, patient_id, medecin_id et diagnostic_id"""
    return db.query(models.Consultation).filter(
        models.Consultation.consultation_id == consultation_id,
        models.Consultation.patient_id == patient_id,
        models.Consultation.medecin_id == medecin_id,
        models.Consultation.diagnostic_id == diagnostic_id,
    ).first()

# Récupère une liste de consultation avec des filtres optionnels.
def get_consultations(
        db: Session,
        skip: int = 0, # pour ignorer les premiers enregistrements
        limit: int = 100,
        consultation_id: Optional[int] = None,
        patient_id: Optional[int] = None,
        medecin_id: Optional[int] = None,
        diagnostic_id: Optional[int] = None 
):
    # Récupère une liste de consultation avec des filtres optionnels.
    query = db.query(models.Consultation).options(
        joinedload(models.Consultation.patient),
        joinedload(models.Consultation.medecin),
        joinedload(models.Consultation.diagnostic)
    ) # joinedload permet de charger les relations en une seule requête

    if consultation_id:
        query = query.filter(models.Consultation.consultation_id == consultation_id)
    if patient_id:
        query = query.filter(models.Consultation.patient_id == patient_id)
    if medecin_id:
        query = query.filter(models.Consultation.medecin_id == medecin_id)
    if diagnostic_id:
        query = query.filter(models.Consultation.diagnostic_id == diagnostic_id)
    
    return query.offset(skip).limit(limit).all()
    # offset(skip) permet de sauter les premiers enregistrements

# Recuperer un patient par son id
def get_patient(db:Session, patient_id=int):
    return db.query(models.PatientDim).filter(
        models.PatientDim.patient_id == patient_id,
    ).first() 

# Recuperer une liste de patient 
def get_patients(
        db: Session,
        skip: int = 0, # pour ignorer les premiers enregistrements
        limit: int = 100,
        patient_id: Optional[int] = None,
        nom: Optional[str] = None,
        prenom: Optional[str] = None,
        sexe: Optional[str] = None,
        situation_matrimonial: Optional[str] = None, 
        statut_professionel: Optional[str] = None 
):
    # Recupère une liste de patient
    query = db.query(models.PatientDim)

    if patient_id:
        query = filter(models.PatientDim.patient_id.ilike(f"%{patient_id}%"))
    if nom:
        query = filter(models.PatientDim.nom.ilike(f"%{nom}%"))
    if prenom:
        query = filter(models.PatientDim.prenom.ilike(f"%{prenom}%"))
    if sexe:
        query = filter(models.PatientDim.sexe.ilike(f"%{sexe}%"))
    if situation_matrimonial:
        query = filter(models.PatientDim.situation_matrimonial.ilike(f"%{situation_matrimonial}%"))
    if statut_professionel:
        query = filter(models.PatientDim.statut_professionel.ilike(f"%{nom}%"))

    return query.offset(skip).limit(limit).all() 
    # offset(skip) permet de sauter les premiers enregistrements

# Récuperer un medecin par son ID
def get_medecin(db : Session, medecin_id = int):
    return db.query(models.MedecinDim).filter(
        models.MedecinDim.medecin_id == medecin_id
    ).first()

# Récuperer la liste des medecins
def get_medecins(
        db: Session,
        skip: int = 0, # pour ignorer les premiers enregistrements
        limit: int = 100,
        medecin_id: Optional[int] = None,
        nom_medecin: Optional[str] = None,
        service_medical: Optional[str] = None,
):
    # recupère une liste de medecins
    query = db.query(models.MedecinDim)

    if medecin_id:
        query = filter(models.PatientDim.patient_id.ilike(f"%{medecin_id}%")) 
    if nom_medecin:
        query = filter(models.PatientDim.patient_id.ilike(f"%{nom_medecin}%")) 
    if service_medical:
        query = filter(models.PatientDim.patient_id.ilike(f"%{service_medical}%")) 

    return query.offset(skip).limit(limit).all() 
    # offset(skip) permet de sauter les premiers enregistrements


## Recuperer un diagnostic à travers son ID
def get_diagnostic(db : Session, diagnostic_id = int):
    return db.query(models.DiagnosticDim).filter(
        models.DiagnosticDim.diagnostic_id == diagnostic_id
    ).first() 

## Recuperer la liste de diagnostic
def get_diagnostics(
       db: Session,
       skip: int = 0, # pour ignorer les premiers enregistrements
       limit: int = 100,
       diagnostic_id: Optional[int] = None,
       gravite: Optional[str] = None,
       etat_sortie: Optional[str] = None, 
):
    # recuperer la liste de diagnostic
    query = db.query(models.DiagnosticDim)
    
    if diagnostic_id:
        query = filter(models.PatientDim.patient_id.ilike(f"%{diagnostic_id}%"))
    if gravite:
        query = filter(models.PatientDim.patient_id.ilike(f"%{gravite}%"))
    if etat_sortie:
        query = filter(models.PatientDim.patient_id.ilike(f"%{etat_sortie}%"))

    return query.offset(skip).limit(limit).all() 
    # offset(skip) permet de sauter les premiers enregistrements 


