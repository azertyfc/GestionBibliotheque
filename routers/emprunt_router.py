from fastapi import APIRouter,Depends
from services.emprunt_service import (
    recuperer_emprunts,
    creer_emprunt
)
from fastapi.security import OAuth2PasswordRequestForm
from schemas.emprunt import EmpruntResponse,EmpruntCreate
from database.dependency import get_db
from sqlalchemy.orm import Session
from security.auth import get_current_user
from models.utilisateur import Utilisateur
from services.auth_service import login
router = APIRouter(
    prefix=("/emprunts"),
    tags=["Emprunts"]
)

@router.get("/",response_model=list[EmpruntResponse],
    summary="Listes des Emprunts"
)
def get_emprunts(
    db:Session = Depends(get_db)
):
    return recuperer_emprunts(db)

"""

@router.post("/", summary="Créer un emprunt")
def create_emprunt(
    emprunt: EmpruntCreate,
  
    db: Session = Depends(get_db)
):
    return creer_emprunt(
        db,
        emprunt.utilisateur_id,
        emprunt.livre_id
    )
"""

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return auth_service.login(
        db,
        form_data.username,
        form_data.password
    )


"""current_user: Utilisateur = Depends(get_current_user),"""