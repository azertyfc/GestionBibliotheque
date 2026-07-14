from sqlalchemy import select,func,update
from sqlalchemy.orm import Session,selectinload
from models.emprunt import Emprunt
from fastapi import HTTPException
from models.livre import Livre
from datetime import datetime,timedelta
from core.exceptions import LimiteEmpruntDepasse,LivreIndisponible,EmpruntEnCours


def creer_emprunt(
    db:Session,
    user_id:int,
    livre_id:int
):
    if compter_emprunts_en_cours_utilisateurs(db, user_id) >= 5:
        raise LimiteEmpruntDepasse("Limite de 5 emprunts atteinte.")


    if not verifier_stock_livre(db, livre_id):
        raise LivreIndisponible("Le livre n'est plus disponible.")
    

    if not utilisateur_peut_emprunter(db, user_id, livre_id):
        raise EmpruntEnCours("Vous avez déjà emprunté ce livre et il n'a pas encore été retourné.")
    
    date_emprunt = datetime.utcnow()
    date_prevu_retour = date_emprunt + timedelta(days=14)
    emprunt = Emprunt(
        utilisateur_id=user_id,
        livre_id=livre_id,
        date_emprunt = date_emprunt,
        date_retour_prevue=date_prevu_retour,
        date_retour = None
    )

    db.add(emprunt)

    update_quantite_livre(db, livre_id)

    db.commit()
    db.refresh(emprunt)

    return emprunt
    




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
    try:
        nb_emprunts = db.scalar(
            select(func.count())
            .select_from(Emprunt)
            .where(
                Emprunt.utilisateur_id == user_id,
                Emprunt.date_retour.is_(None)  # emprunts en cours
            )
        )

        return nb_emprunts 


    except Exception:
        db.rollback()
        raise


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
    


def verifier_stock_livre(
    db: Session,
    livre_id: int
) -> int:
    
    try:
        livre = db.execute(
            select(Livre).where(Livre.id == livre_id)
        ).scalar_one_or_none()

        if livre is None:
            raise ValueError("livre introuvable")
            
        return livre.quantite_disponible>0
        
    except Exception:
        db.rollback()
        raise
    

def update_quantite_livre(
        db:Session,
        livre_id:int
):
    
    try:

        db.execute(
                update(Livre)
                .where(Livre.id == livre_id)
                .values(
                    quantite_disponible=Livre.quantite_disponible - 1
                )
            )
        

    except Exception:
        db.rollback()
        raise

    






