from fastapi import APIRouter,Depends
from database.dependency import get_db
from sqlalchemy.orm import Session
from datetime import date

from services.livre_service import(
    recuperer_livres,
    recuperer_livre,
    creer_livre,
    recuperer_livre_date_publication,
    recuperer_livre_isbn,
    recuperer_livres_categories,
    modifier_livre
)
from schemas.livre import LivreResponse,LivreUpdate

router = APIRouter(
    prefix="/livres",
    tags=["Livres"]
)


@router.get("/",response_model=list[LivreResponse],
    summary="Listes des livres",
    description="Retournez livres"
)
def get_livres(
    db:Session = Depends(get_db)
):
    return recuperer_livres(db)

@router.get("/{livre_id}",
    summary="Livre demander"
)
def get_livre(
    livre_id:int,
    db:Session = Depends(get_db)
):
    return recuperer_livre(db,livre_id)

@router.get("/isbn/{isbn}",
    summary="retourner livre par isbn"
)
def get_livre_isbn(isbn:str,
    db:Session = Depends(get_db)
):
    return recuperer_livre_isbn(db,isbn)

@router.get("/date_publication/{date_publication}",
    summary="Retournez les livres d'une date de publication donnée"
)
def get_livre_date_publication(
    date_publication:date,
    db:Session=Depends(get_db)
):
    return recuperer_livre_date_publication(db,date_publication)


@router.get("/categorie/{nom_categorie}",response_model=list[LivreResponse],
    summary="Retournez les livres d'une Categorie"
)
def get_livres_categories(
    nom_categorie:str,
    db:Session=Depends(get_db)
):
    return recuperer_livres_categories(db,nom_categorie)

@router.patch("/{livre_id}",response_model=LivreResponse,
    summary="Modifier livre"
)
def update_livre(
    livre_id:int,
    livre:LivreUpdate,
    db:Session = Depends(get_db)
):
    return modifier_livre(db,livre,livre_id)