from sqlalchemy.orm import sessionmaker
from database.connexion import engine

SessionLocal = sessionmaker(
    bind=engine
)