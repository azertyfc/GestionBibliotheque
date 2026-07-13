from models.utilisateur import Utilisateur
from sqlalchemy.orm import selectinload,Session
from sqlalchemy import select


def recuperer_utilisateurs(
    db:Session
):
    try:
        return(
            db.execute(select(Utilisateur).options(selectinload(Utilisateur.role)))
            .scalars()
            .all()
        )
    
    except Exception:
        db.rollback()
        raise

def recuperer_utilisateur(
    db:Session,
    users_id:int
):
    try:
        return(
            db.execute(select(Utilisateur).options(selectinload(Utilisateur.role)).where(Utilisateur.id==users_id))
            .scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()
        raise


def recuperer_employe_par_email(
        db:Session,
        email:str
):
    try:
        return (
            db.execute(select(Utilisateur).options(selectinload(Utilisateur.role)).where(Utilisateur.email==email)).scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()
        raise
    