from models.livre import Livre
from sqlalchemy.orm import Session,selectinload
from sqlalchemy import select
from datetime import date
from models.categorie import Categorie
from schemas.livre import LivreUpdate

def creer_livre(
        db:Session,
        livre:Livre
):
    try:
        livre = db.add(livre)
        db.commit()

        return livre
    except Exception:

        db.rollback()
        raise



def recuperer_livres(
    db:Session
):
    try:
        
        livres = db.execute(select(Livre).options(selectinload(Livre.categorie))).scalars().all()
    
        return livres

    except Exception:
        db.rollback()
        raise

def recuperer_livre(
        db:Session,
        livre_id:int
):
    try:

        return(
            db.execute(select(Livre).options(selectinload(Livre.categorie)).where(Livre.id==livre_id)).scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()

        raise

def recuperer_livre_isbn(
        db:Session,
        isbn:str
):
    try:
        return(
            db.execute(select(Livre).options(selectinload(Livre.categorie)).where(Livre.isbn==isbn)).scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()
        raise

def recuperer_livre_date_publication(
        db:Session,
        date_publication:date
):
    try:
        return (
            db.execute(select(Livre).options(selectinload(Livre.categorie)).where(Livre.date_publication==date_publication)).
            scalars().all()
        )
    
    except Exception:
        db.rollback()
        raise


def recuperer_livres_categories(
        db:Session,
        nom_categorie:str
):
    try:
        result = db.execute(
        select(Livre).options(selectinload(Livre.categorie))
        .join(Categorie, Livre.categorie_id == Categorie.id)
        .where(Categorie.nom == nom_categorie)
        )
        return result.scalars().all()

    except Exception:
        db.rollback()
        raise


def modifier_livre(
        db:Session,
        livre_update:LivreUpdate,
        livre_id:int

):
    try:

        livre = db.execute(
        select(Livre).options(selectinload(Livre.categorie))
        .where(Livre.id == livre_id)
        ).scalar_one_or_none()

        if livre is None:
           raise ValueError("Livre introuvable")

        for champ, valeur in livre_update.model_dump(
        exclude_unset=True
        ).items():

            setattr(
                livre,
                champ,
                valeur
             )

        db.commit()

        db.refresh(livre)

        return livre

    except Exception:
        db.rollback()
        raise
