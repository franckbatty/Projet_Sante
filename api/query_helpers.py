## == API Restful pour la Sante == ##
# Developpement des fonctions d'aide pour mon API RESTful

# Importation des modules nécessaires
from sqlalchemy.orm import Session # pour interagir avec la base de données
from sqlalchemy.orm import joinedload # permet de charger les relations en une seule requête pour éviter les requêtes N+1
from typing import Optional # pour les types optionnels c'est-à-dire les paramètres qui peuvent être None
from datetime import date
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
        diagnostic_id: Optional[int] = None,
        date_consultation: Optional[date] = None,
        sum: Optional[int] = None
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
    if date_consultation:
        query = query.filter(models.Consultation.date_consultation == date_consultation)
    if sum:
        query = query.filter(models.Consultation.sum == sum)
    
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
        query = query.filter(models.PatientDim.patient_id == patient_id)
    if nom:
        query = query.filter(models.PatientDim.nom == nom)
    if prenom:
        query = query.filter(models.PatientDim.prenom == prenom)
    if sexe:
        query = query.filter(models.PatientDim.sexe == sexe)
    if situation_matrimonial:
        query = query.filter(models.PatientDim.situation_matrimonial == situation_matrimonial)
    if statut_professionel:
        query = query.filter(models.PatientDim.statut_professionel == statut_professionel)

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
        query = query.filter(models.MedecinDim.medecin_id == medecin_id) 
    if nom_medecin:
        query = query.filter(models.MedecinDim.nom_medecin == nom_medecin) 
    if service_medical:
        query = query.filter(models.MedecinDim.service_medical == service_medical) 

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
        query = query.filter(models.DiagnosticDim.diagnostic_id == diagnostic_id)
    if gravite:
        query = query.filter(models.DiagnosticDim.gravite == gravite)
    if etat_sortie:
        query = query.filter(models.DiagnosticDim.etat_sortie == etat_sortie)

    return query.offset(skip).limit(limit).all() 
    # offset(skip) permet de sauter les premiers enregistrements 

# Requete Analytique
# Recuperer le nombre total de consultations
def get_total_consultations(db: Session): 
    """Récupère le nombre total de consultations."""
    return db.query(models.Consultation).count()
# Recuperer le total de patients
def get_total_patients(db: Session): 
    """Récupère le nombre total de patients."""
    return db.query(models.PatientDim).count()
# Recuperer le total de medecins
def get_total_medecins(db: Session): 
    """Récupère le nombre total de medecins."""
    return db.query(models.MedecinDim).count()
# Recuperer le total de diagnostics
def get_total_diagnostics(db: Session): 
    """Récupère le nombre total de diagnostics."""
    return db.query(models.DiagnosticDim).count()


