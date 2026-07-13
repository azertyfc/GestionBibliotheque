from fastapi import APIRouter,Depends,HTTPException
from services.utilisateur_service import (
    recuperer_utilisateurs,
    recuperer_utilisateur,
    modifier_utilisateur

)
from sqlalchemy.orm import Session
from database.dependency import get_db
from schemas.utilisateur import UtilisateurResponse,UtilisateurUpdate
from models.utilisateur import Utilisateur



router = APIRouter(
    prefix=("/utilisateurs"),
    tags=["Utilisateurs"] 
)

@router.get("/",response_model= list[UtilisateurResponse],
    summary="Les utilisateurs"
)
def get_utilisateurs(
    db:Session = Depends(get_db),
):
    return recuperer_utilisateurs(db)


@router.get("/{user_id}",response_model= UtilisateurResponse,
    summary="L'utilisateur"
)
def get_utilisateur(
    user_id:int,
    db:Session = Depends(get_db)
):
    return recuperer_utilisateur(db,user_id)

@router.patch("/{user_id}",response_model=UtilisateurResponse,
    summary="Modifier un Utilisateur"
)
def update_utilisateur(
    user_id:int,
    user_update:UtilisateurUpdate,
    db:Session=Depends(get_db)
):
    return modifier_utilisateur(db,user_update,user_id)

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