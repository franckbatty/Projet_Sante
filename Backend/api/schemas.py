# Fichier Pydantic pour les schémas de l'API  
# Pydantic est une bibliothèque de validation de données en Python.
# Elle permet de valider les données entrantes et sortantes de l'API. 
# Met dans notre cas, elle va valider que les données sortantes étant donné que l'API est en lecture seule.

# Importation des modules nécessaires
from pydantic import BaseModel
from typing import List, Optional 
from datetime import date

# Modèle de sortie pour consultation
class ConsultationBase(BaseModel):
    consultation_id : int
    patient_id : int
    medecin_id : int
    diagnostic_id : int
    date_consultation : date
    sum : int

    class Config:
        from_attributes  = True  # Permet à Pydantic de lire les données des objets ORM

# Modèle de de sortie de Patient 
class PatientBase(BaseModel):
    patient_id : int
    nom : str
    prenom : str
    sexe : str
    situation_matrimonial : str
    statut_professionel : str

    class Config:
        from_attributes  = True  # Permet à Pydantic de lire les données des objets ORM

# Modèle de sortie de medecin
class MedecinBase(BaseModel):
    medecin_id : int
    nom_medecin : str
    service_medical : str

    class Config:
        from_attributes  = True  # Permet à Pydantic de lire les données des objets ORM

# Modèle de sortie de diangostic
class DiagnosticBase(BaseModel):
    diagnostic_id : int
    gravite : str
    etat_sortie : str

    class Config:
        from_attributes  = True  # Permet à Pydantic de lire les données des objets ORM
# Modèle de sortie analytics
class Analytics(BaseModel):
    consultations_count: int
    patients_count: int
    medecins_count: int
    diagnostics_count: int

    class Config:
        from_attributes  = True