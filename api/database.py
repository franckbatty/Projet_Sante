""" Ce fichier est utilisé pour créer la connection à la base de données PostgreSQL
    en utilisant SQLAlchemy qui est un ORM (Object Relational Mapper) pour Python qui va nous
    permettre d'interagir avec la base de données de manière plus simple et plus efficace. 


# Importation des modules nécessaires
from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv 
import os


load_dotenv()  # Charge les variables depuis le fichier .env

# Chargement sécurisé de l’URL de connexion à la base de données
# Cette variable DATABASE_URL doit être définie dans l’environnement (ex: Render ou .env local)
# On lève une exception explicite si elle est absente pour éviter une connexion invalide
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise Exception("La variable DATABASE_URL n'est pas définie !")

# Créer un moteur de base de données (engine) qui établit la connexion avec notre base PostgreSQL.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.
Base = declarative_base() 

# Verifier la connexion à la base de données
if __name__ == "__main__":
     try:
         with engine.connect() as conn:
             print("Connexion à la database réussie")
     except Exception as e:
         print(f"Erreur de connexion à la database : {e}") 
"""
"""Database configuration"""

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Définir l'URL de connexion à notre base SQLite (gold_api.db) en local
SQLALCHEMY_DATABASE_URL = "sqlite:///./gold_api.db"

# Créer un moteur de base de données (engine) qui établit la connexion avec notre base SQLite (gold_api.db).
# Le paramètre check_same_thread=False permet l'accès multithread, indispensable dans un projet FastAPI.
# check_same_thread=False est nécessaire pour permettre l'accès à la base de données depuis plusieurs threads, c'est à dire que plusieurs requêtes peuvent accéder à la base de données en même temps.
# Cela est particulièrement utile dans les applications web où plusieurs utilisateurs peuvent interagir avec l'application simult
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.
Base = declarative_base() 

if __name__ == "__main__":
     try:
         with engine.connect() as conn:
             print("Connexion à la database réussie")
     except Exception as e:
         print(f"Erreur de connexion à la database : {e}")
