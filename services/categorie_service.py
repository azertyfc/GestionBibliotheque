from schemas.categorie import CategorieUpdate
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.categorie import Categorie
from security.auth import get_current_user
from fastapi import Depends,HTTPException
from models import Utilisateur

from fastapi import HTTPException

def creer_categorie(
    db:Session,
    categorie:Categorie
):
    try:
        
        db.add(categorie)
        db.commit()
        db.refresh(categorie)

        return categorie
    
    except Exception:
        db.rollback()
        raise



def recuperer_categories(
    db:Session
):
    try:
        return(
            db.execute(select(Categorie)).scalars().all()
        )

    except Exception:

        db.rollback()
        raise


def modifier_categorie(
    db:Session,
    categorie_update:CategorieUpdate,
    categorie_id
):
    try:

        categorie = db.execute(select(Categorie).where(Categorie.id == categorie_id)).scalar_one_or_none()

        if categorie is None:
            raise ValueError("Categorie Introuvable")
        
        for champ, valeur in categorie_update.model_dump(
        exclude_unset=True
        ).items():

            setattr(
                categorie,
                champ,
                valeur
            )

        db.commit()
        db.refresh(categorie)

        return categorie

    except Exception:
        db.rollback()
        raise


def supprimer_categorie(
    db: Session,
    categorie_id: int
):
    categorie = db.execute(
        select(Categorie).where(Categorie.id == categorie_id)
    ).scalar_one_or_none()

    if categorie is None:
        raise HTTPException(
            status_code=404,
            detail="Catégorie introuvable"
        )

    db.delete(categorie)
    db.commit()

    return {"message": "Catégorie supprimée avec succès"}


