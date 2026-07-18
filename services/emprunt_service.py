from sqlalchemy import select,func,update
from sqlalchemy.orm import Session,selectinload
from models.emprunt import Emprunt
from fastapi import HTTPException
from models.livre import Livre
from datetime import datetime,timedelta
from core.exceptions import (LimiteEmpruntDepasse,
    LivreIndisponible,
    EmpruntEnCours,
    RenouvelerImpossible)


def creer_emprunt(
    db: Session,
    user_id: int,
    livre_id: int
):
    
    try:
        livre = get_livre(db, livre_id)

        
        if livre.quantite_livre <= 0:
            raise LivreIndisponible("Le livre n'est plus disponible.")
        
        if compter_emprunts_en_cours_utilisateurs(db, user_id) >= 5:
            raise LimiteEmpruntDepasse("Limite de 5 emprunts atteinte.")

        if not utilisateur_peut_emprunter(db, user_id, livre_id):
            raise EmpruntEnCours(
                "Vous avez déjà emprunté ce livre et il n'a pas encore été retourné."
            )

        livre.quantite_livre -= 1

        date_emprunt = datetime.utcnow()
        date_prevu_retour = date_emprunt + timedelta(days=14)

        emprunt = Emprunt(
            utilisateur_id=user_id,
            livre_id=livre_id,
            date_emprunt=date_emprunt,
            date_retour_prevue=date_prevu_retour,
            date_retour=None,
        )

        db.add(emprunt)

        db.commit()

        db.refresh(emprunt)

        return emprunt
    
    except Exception:
        db.rollback()
        raise
    




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
            .scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()
        raise


def compter_emprunts_en_cours_utilisateurs(
    db: Session,
    user_id:int
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


  


def utilisateur_peut_emprunter(
    db: Session,
    user_id: int,
    livre_id: int
) -> bool:

    emprunt = db.execute(
        select(Emprunt).where(
            Emprunt.utilisateur_id == user_id,
            Emprunt.livre_id == livre_id,
            Emprunt.date_retour.is_(None)
        )
    ).scalar_one_or_none()

    return emprunt is None
    


def get_livre(
    db: Session,
    livre_id: int
) -> Livre:
    
        livre = db.execute(
            select(Livre).where(Livre.id == livre_id)
        ).scalar_one_or_none()

        if livre is None:
            raise ValueError("livre introuvable")
            
        return livre
        


def recuperer_emprunt_dun_livre(
          db:Session,
          livre_id:int
):
    return (
           db.execute(select(Emprunt).options(selectinload(Livre))
            .where(Emprunt.livre_id==livre_id)
        ).scalar_one_or_none()
     )

def renouveler_emprunt(
    db: Session,
    user_id: int,
    livre_id: int
):  
    emprunt = recuperer_emprunt_dun_livre(db,livre_id)

    if emprunt.date_retour_prevue == datetime.utcnow():
        raise RenouvelerImpossible(
            "Impossible de renouveller cette emprumt"
        )

    date_prevu_retour = datetime.utcnow() + timedelta(days=7)

    emprunt = Emprunt(
            utilisateur_id=user_id,
            livre_id=livre_id,
            date_retour_prevue=date_prevu_retour,
            date_retour=None,
    )

    db.add(emprunt)

    db.commit()



    

      






