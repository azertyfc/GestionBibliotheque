from fastapi import APIRouter,Depends
from services.emprunt_service import (
    recuperer_emprunts
)
from schemas.emprunt import EmpruntResponse
from models.emprunt import Emprunt
from database.dependency import get_db
from sqlalchemy.orm import Session

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