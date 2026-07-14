"""
Routes d'authentification.
"""

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from fastapi.security import OAuth2PasswordRequestForm

from database.dependency import get_db

from schemas.auth import TokenResponse

from services.auth_service import login


router = APIRouter(

    tags=["Authentification"]

)


@router.post(

    "/login",

    response_model=TokenResponse,

    summary="Connexion"

)
def connexion(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)

):

    return login(

        db,

        form_data.username,

        form_data.password

    )