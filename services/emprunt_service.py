from sqlalchemy import select,func
from sqlalchemy.orm import Session,selectinload
from schemas.emprunt import EmpruntResponse
from models.emprunt import Emprunt
from fastapi import HTTPException




def creer_emprunt(
    db:Session,
    user_id:int,
    livre_id:int
):
    if utilisateur_peut_emprunter(db, user_id) >= 5:
        raise HTTPException(
            status_code=400,
            detail="Limite de 5 emprunts atteinte."
        )

    if not verifier_stock_livre(db, livre_id):
        raise HTTPException(
            status_code=400,
            detail="Le livre n'est plus disponible."
        )
    ...



def recuperer_emprunts(
    db:Session
):
    try:

        return(
            db.execute(select(Emprunt).options(selectinload(Emprunt.utilisateur),selectinload(Emprunt.livre)))
            .scalars().all()
        )
    
    except Exception:
        db.rollback()
        raise

def recuperer_emprunt(
    db:Session,
    emprunt_id:int
):
    try:

        return(
            db.execute(select(Emprunt).options(selectinload(Emprunt.utilisateur),selectinload(Emprunt.livre))
            .where(Emprunt.id == emprunt_id))
            .scalars().all()
        )
    
    except Exception:
        db.rollback()
        raise


def compter_emprunts_en_cours(
    db: Session,
    user_id: int
) ->int:
    nb_emprunts = db.scalar(
        select(func.count())
        .select_from(Emprunt)
        .where(
            Emprunt.utilisateur_id == user_id,
            Emprunt.date_retour.is_(None)  # emprunts en cours
        )
    )

    return nb_emprunts 


def verifier_stock_livre(
    db: Session,
    livre_id: int
) -> bool:
    ...

def utilisateur_peut_emprunter(
    db: Session,
    utilisateur_id: int
):
    nb_emprunts = db.scalar(
        select(func.count())
        .select_from(Emprunt)
        .where(
            Emprunt.utilisateur_id == user_id,
            Emprunt.date_retour.is_(None)  # emprunts en cours
        )
    )

    return nb_emprunts 

