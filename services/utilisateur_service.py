from models.utilisateur import Utilisateur
from sqlalchemy.orm import selectinload,Session
from sqlalchemy import select
from schemas.utilisateur import UtilisateurUpdate
from security.password import hash_password

def creer_utilisateur(
    db: Session,
    utilisateur: Utilisateur
):

    utilisateur.mot_de_passe = hash_password(
        utilisateur.mot_de_passe
    )

    db.add(utilisateur)

    db.commit()

    db.refresh(utilisateur)

    return utilisateur


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


def recuperer_utilisateur_par_email(
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


def modifier_utilisateur(
        db:Session,
        users_update:UtilisateurUpdate,
        users_id:int
):
    try:

        users = db.execute(
            select(Utilisateur).options(selectinload(Utilisateur.role))
            .where(Utilisateur.id == users_id)
        ).scalar_one_or_none()

        if users is None:
            return ValueError("Utilisateur Introuvable")
        
        for champs,valeur in users_update.model_dump(
            exclude_unset=True
        ).items():
            
            setattr(
                users,
                champs,
                valeur
            )
        db.commit()
        db.refresh(users)

        return users
    
    except Exception:
        db.rollback()
        raise