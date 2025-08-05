# Ce fichier est utilisé pour définir les modèles de données de notre application

# Importation des modules nécessaires
from sqlalchemy import Column, Integer, String, Date, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from database import Base

# Table de faits : Consultation
class Consultation(Base):
    __tablename__ = "fait_consultation" # Nom de la table de faits sur base de données postgreSQL
    # Clé primaire composite : identifie chaque consultation de manière unique
    __table_args__ = (
        PrimaryKeyConstraint('consultation_id', 'patient_id', 'medecin_id', 'diagnostic_id'),
    )
 
    # Identifiants et mesure
    consultation_id = Column(Integer)
    patient_id = Column(Integer, ForeignKey('dim_patient.patient_id'))  # lien vers la dimension Patient
    medecin_id = Column(Integer, ForeignKey('dim_medecins.medecin_id'))  # lien vers la dimension Médecin
    diagnostic_id = Column(Integer, ForeignKey('dim_diagnostics.diagnostic_id'))  # lien vers la dimension Diagnostic
    date_consultation = Column(Date)  # Date de la consultation
    sum = Column(Integer)  # Mesure agrégée (ex : coût)

    # Relations vers les dimensions (bidirectionnelles)
    patient = relationship("PatientDim", back_populates="consultation")
    medecin = relationship("MedecinDim", back_populates="consultation")
    diagnostic = relationship("DiagnosticDim", back_populates="consultation")
    # back_populates permet de créer une relation bidirectionnelle entre les tables de faits et de dimensions,
    # facilitant ainsi les requêtes et la navigation dans les données.

# Dimension : Patient
class PatientDim(Base):
    __tablename__ = "dim_patient"

    # Clé primaire
    patient_id = Column(Integer, primary_key=True)

    # Attributs du patient
    nom = Column(String)
    prenom = Column(String)
    sexe = Column(String)
    situation_matrimonial = Column(String)
    statut_professionel = Column(String)

    # Relation inverse : toutes les consultations associées
    consultation = relationship("Consultation", back_populates="patient")

# Dimension : Médecin
class MedecinDim(Base):
    __tablename__ = "dim_medecins"

    # Clé primaire
    medecin_id = Column(Integer, primary_key=True)

    # Attributs du médecin
    nom_medecin = Column(String)
    service_medical = Column(String)

    # Relation inverse
    consultation = relationship("Consultation", back_populates="medecin")

# Dimension : Diagnostic
class DiagnosticDim(Base):
    __tablename__ = "dim_diagnostics"

    # Clé primaire
    diagnostic_id = Column(Integer, primary_key=True)

    # Attributs du diagnostic
    gravite = Column(String)
    etat_sortie = Column(String)

    # Relation inverse
    consultation = relationship("Consultation", back_populates="diagnostic")
