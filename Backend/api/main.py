# Developement de l'API FastAPI pour la Sante

# Importation des modules nécessaires
from fastapi import FastAPI, Depends, HTTPException, Query, Path 
from sqlalchemy.orm import Session 
from typing import List, Optional
from .database import SessionLocal 
from datetime import date
from . import query_helpers as helpers
from . import schemas 

api_description = """ 
Bienvenue dans l'API Sante 

Cette API RESTful expose les données analytiques issues d’un entrepôt e-commerce structuré (couche Gold) 
à des fins de reporting, d’exploration ou d’intégration front.

Inspirée des bonnes pratiques modernes, elle permet d’interroger les consultations, les patients, les medecins et les diagnostic 
ainsi que des statistiques consolidées, à travers des endpoints simples, documentés, et 100 % en lecture seule.

### Fonctionnalités disponibles :

- Rechercher une consultation par ID consultation, ID patient, ID medecin et ID diagnostic
- Lister toutes les consultations avec filtres (consultation_id, patient_id, medecin_id, diagnostic_id.)
- Lister un ou plusieurs patients
- Lister un medecin ou plusieurs medecins
- Lister un ou plusieurs diagnostics 
- Voir des statistiques globales sur la base

Tous les endpoints supportent la pagination (`skip`, `limit`) et des filtres optionnels selon les cas.

### Bon à savoir
- Vous pouvez tester tous les endpoints directement via l'interface Swagger "/docs".
- Pour toute erreur (ex : ID inexistant), une réponse claire est retournée avec le bon code HTTP.

"""

# --- Initialisation de l'application FastAPI ---
app = FastAPI(
    title="E_commerce API", # 
    description = api_description,
    version = "0.1"
)
# --- Dépendance pour la session de base de données ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Endpoint pour tester la santé de l'API
@app.get(
    "/",
    summary="Vérification de la santé de l'API",
    description="Vérifie que l'API fonctionne correctement.",
    response_description="Statut de l'API",
    operation_id="health_check_sante_api",
    tags=["monitoring"]
)

async def root():
    return {"message": "API Sante opérationnelle"}

# Endpoint pour obtenir une consultation par ses id : consultation_id de consultation, patient_id de patient, medecin_id de medecin et diagnostic_id de diagnostic.
@app.get(
    "/consultation/{consultation_id}/{patient_id}/{medecin_id}/{diagnostic_id}/",
    summary="Obtenir une consultation par quatre ID",
    description="Retourne une consultation spécifique à partir de l’ID commande, ID client et ID produit.",
    response_description="Détails de la consultation",
    response_model=schemas.ConsultationBase, # retourne une ligne
    tags=["consultation"]
) 
def lire_consultation(consultation_id:int,patient_id:int,medecin_id:int,diagnostic_id:int,db:Session=Depends(get_db)):
    consultation = helpers.get_consultation(db, consultation_id,patient_id,medecin_id,diagnostic_id)
    if not consultation:
        raise HTTPException(status_code=404, detail="Consultation introuvable.")
    return schemas.ConsultationBase.from_orm(consultation)

# Endpoint pour obtenir une liste de consultation
@app.get(
    "/consultations",  
    summary="Lister les consultations",
    description="Retourne une liste de consultations.",
    response_description="Liste de consultations",
    response_model=List[schemas.ConsultationBase], # retourne une liste
    tags=["consultations"],
)
def liste_consultations( 
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"), 
    consultation_id: int = Query(None, description="Filtre par id consultation"), 
    patient_id: int = Query(None, description="Filtre par id patient"),
    medecin_id: int = Query(None, description="Filtre par id medecin"),
    diagnostic_id: int = Query(None, description="Filtre par id diagnostic"),
    date_consultation: date = Query(None, description="Filtre par date"),
    sum: int = Query(None, description="Filtre par Frais de consultation"),
    db: Session = Depends(get_db)
):
    consultations = helpers.get_consultations(db, skip=skip, limit=limit, consultation_id=consultation_id, patient_id=patient_id,medecin_id=medecin_id,diagnostic_id=diagnostic_id,date_consultation=date_consultation,sum=sum )
    return [schemas.ConsultationBase.from_orm(v) for v in consultations]

# Endpoint pour obtenir un patient par son id
@app.get(
    "/patient/{patient_id}",
    summary="Obtenir un patient par sont ID",
    description="Retourne un patient à partir de l’ID patient.",
    response_description="Détails du patient",
    response_model=schemas.PatientBase, # retourne une ligne
    tags=["patient"]
) 
def lire_patient(patient_id:int,db:Session=Depends(get_db)):
    patient = helpers.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient introuvable.")
    return schemas.PatientBase.from_orm(patient)

# Endpoint pour obtenir une liste de patient
@app.get(
    "/patients",  
    summary="Lister les patients",
    description="Retourne une liste de patients.",
    response_description="Liste de patients",
    response_model=List[schemas.PatientBase], # retourne une liste
    tags=["patients"],
)
def liste_patients( 
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"), 
    patient_id: int = Query(None, description="Filtre par id patient"), 
    nom : str = Query(None, description="Filtre par nom"),
    prenom : str = Query(None, description="Filtre par prenom"),
    sexe : str = Query(None, description="Filtre par sexe"),
    situation_matrimonial : str = Query(None, description="Filtre par situation matrimoniale"),
    statut_professionel : str = Query(None, description="Filtre par statut professionel"),
    db: Session = Depends(get_db)
):
    patients = helpers.get_patients(db, skip=skip,
                                    limit=limit,
                                    patient_id=patient_id,
                                    nom=nom,
                                    prenom=prenom,
                                    sexe=sexe,
                                    situation_matrimonial=situation_matrimonial,
                                    statut_professionel=statut_professionel)
    return [schemas.PatientBase.from_orm(v) for v in patients] 

# Endpoint pour obtenir un medecin par son ID
@app.get(
    "/medecin/{medecin_id}",
    summary="Obtenir un medecin par sont ID",
    description="Retourne un medecin à partir de l’ID medecin.",
    response_description="Détails du medecin",
    response_model=schemas.MedecinBase, # retourne une ligne
    tags=["medecin"]
) 
def lire_medecin(medecin_id:int,db:Session=Depends(get_db)):
    medecin = helpers.get_medecin(db, medecin_id)
    if not medecin_id: 
        raise HTTPException(status_code=404, detail="Medecin introuvable.")
    return schemas.MedecinBase.from_orm(medecin)

# Endpoint pour obtenir la liste des medecins
@app.get(
    "/medecins",  
    summary="Lister les medecins",
    description="Retourne une liste de medecins.",
    response_description="Liste de medecins",
    response_model=List[schemas.MedecinBase], # retourne une liste
    tags=["medecins"],
)
def liste_medecins( 
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"), 
    medecin_id: int = Query(None, description="Filtre par id medecin"), 
    nom_medecin : str = Query(None, description="Filtre par nom medecin"),
    service_medical : str = Query(None, description="Filtre par service_medical"),
    db: Session = Depends(get_db)
): 
    medecins = helpers.get_medecins(db, skip=skip,
                                    limit=limit,
                                    medecin_id=medecin_id,
                                    nom_medecin=nom_medecin,
                                    service_medical=service_medical)
    return [schemas.MedecinBase.from_orm(v) for v in medecins] 

# Endpoint pour obtenir un diagnostic à travers son ID
@app.get(
    "/diagnostic/{diagnostic_id}",
    summary="Obtenir un diagnostic par sont ID",
    description="Retourne un diagnostic à partir de l’ID diagnostic.",
    response_description="Détails du diagnostic",
    response_model=schemas.DiagnosticBase, # retourne une ligne
    tags=["diagnostic"]
) 
def lire_diagnostic(diagnostic_id:int,db:Session=Depends(get_db)):
    diagnostic = helpers.get_diagnostic(db, diagnostic_id)
    if not diagnostic: 
        raise HTTPException(status_code=404, detail="Medecin introuvable.")
    return schemas.DiagnosticBase.from_orm(diagnostic)

# Endpoint pour obtenir la liste de diagnostic
@app.get(
    "/diagnostics",  
    summary="Lister les diagnostics",
    description="Retourne une liste de diagnostics.",
    response_description="Liste de diagnostics",
    response_model=List[schemas.DiagnosticBase], # retourne une liste
    tags=["diagnostics"],
)
def liste_diagnostics( 
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(100, le=1000, description="Nombre maximal de résultats à retourner"), 
    diagnostic_id: int = Query(None, description="Filtre par id diagnostic"), 
    gravite : str = Query(None, description="Filtre par nom gravite"),
    etat_sortie : str = Query(None, description="Filtre par etat_sortie"),
    db: Session = Depends(get_db)
): 
    diagnostics = helpers.get_diagnostics(db, skip=skip,
                                    limit=limit,
                                    diagnostic_id=diagnostic_id,
                                    gravite=gravite,
                                    etat_sortie=etat_sortie)
    return [schemas.DiagnosticBase.from_orm(v) for v in diagnostics]  

# Endpoint pour obtenir des statistiques sur la base de données
@app.get(
    "/analytics",
    summary="Obtenir des statistiques",
    description="""
    Retourne un résumé analytique de la base de données :

    - Nombre total de Consultation
    - Nombre total de patients
    - Nombre total de medecins
    - Nombre total de diagnostics
    """,
    response_model=schemas.Analytics,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    consultations_count = helpers.get_total_consultations(db)
    patients_count = helpers.get_total_patients(db)
    medecins_count = helpers.get_total_medecins(db)
    diagnostics_count = helpers.get_total_diagnostics(db)

    return schemas.Analytics(
    consultations_count=consultations_count,
    patients_count=patients_count,
    medecins_count=medecins_count,
    diagnostics_count=diagnostics_count
    ) 