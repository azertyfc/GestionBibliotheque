from fastapi import APIRouter,Depends,HTTPException
from services.utilisateur_service import (
    recuperer_utilisateurs,
    recuperer_utilisateur,
    recuperer_employe_par_email
)
from sqlalchemy.orm import Session
from database.dependency import get_db
from schemas.utilisateur import UtilisateurResponse
from schemas.auth import LoginRequest
from security.auth import get_current_user
from models.utilisateur import Utilisateur
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    prefix=("/utilisateurs"),
    tags=["Utilisateurs"] 
)

@router.get("/",response_model= list[UtilisateurResponse],
    summary="Les utilisateurs"
)
def get_utilisateurs(
    db:Session = Depends(get_db),
    current_user: Utilisateur = Depends(get_current_user)
):
    return current_user


@router.get("/{users_id}",response_model= UtilisateurResponse,
    summary="L'utilisateur"
)
def get_utilisateur(
    users_id:int,
    db:Session = Depends(get_db)
):
    return recuperer_utilisateur(db,users_id)



"""


@router.post("/login")
def login(
    login: LoginRequest,
    db: Session = Depends(get_db)
):

    employe = recuperer_employe_par_email(
        db,
        login.email
    )

    if employe is None:

        raise HTTPException(
            status_code=401,
            detail="Email ou mot de passe incorrect"
        )

    return {
        "message": "Employé trouvé"
    }


"""