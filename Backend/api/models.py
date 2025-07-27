# importation des modules nécessaires
"""SQLAlchemy models"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey, PrimaryKeyConstraint, Date
from sqlalchemy.orm import relationship # permet des relations de clé étrangère entre les tables.
from database import Base


# Table de Fait : Consultation 
class Consultation(Base):
    __tablename__ = "fait_consultation"
    __table_args__ = (
        PrimaryKeyConstraint('consultation_id', 'patient_id', 'medecin_id', 'diagnostic_id'),
        {'schema': 'sante_gold'}
    )
    ## consultation_id est la clé primaire de ma table de fait sur la couche gold à laquelle je calcule ma mesure.
    consultation_id = Column(Integer)
    patient_id = Column(Integer, ForeignKey('sante_gold.dim_patient.patient_id'))
    medecin_id = Column(Integer, ForeignKey('sante_gold.dim_medecins.medecin_id'))
    diagnostic_id = Column(Integer, ForeignKey('sante_gold.dim_diagnostics.diagnostic_id'))
    date_consultation = Column(Date)
    sum = Column(Integer)

    # Relations vers les dimensions
    patient = relationship(
        "PatientDim",
        back_populates="consultation",
        primaryjoin="Consultation.patient_id == PatientDim.patient_id"
    )
    medecin = relationship(
        "MedecinDim",
        back_populates="consultation",
        primaryjoin="Consultation.medecin_id == MedecinDim.medecin_id"
    )
    diagnostic = relationship(
        "DiagnosticDim",
        back_populates="consultation",
        primaryjoin="Consultation.diagnostic_id == DiagnosticDim.diagnostic_id"
    )

# Dimension : Patient 
class PatientDim(Base):
    __tablename__ = "dim_patient"
    __table_args__ = ({"schema": "sante_gold"},)
    
    patient_id = Column(Integer, primary_key=True)
    nom = Column(String)
    prenom = Column(String)
    sexe = Column(String)
    situation_matrimonial = Column(String) 
    statut_professionel = Column(String)

    consultation = relationship("Consultation", back_populates="patient")

#  Dimension : Médecin 
class MedecinDim(Base): 
    __tablename__ = "dim_medecins"
    __table_args__ = ({"schema": "sante_gold"},)

    medecin_id = Column(Integer, primary_key=True)
    nom_medecin = Column(String)
    service_medical = Column(String)

    consultation = relationship("Consultation", back_populates="medecin")

#  Dimension : Diagnostic 
class DiagnosticDim(Base):
    __tablename__ = "dim_diagnostics"
    __table_args__ = ({"schema": "sante_gold"},)

    diagnostic_id = Column(Integer, primary_key=True)
    gravite = Column(String)
    etat_sortie = Column(String)

    consultation = relationship("Consultation", back_populates="diagnostic")
