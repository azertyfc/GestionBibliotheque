from fastapi import APIRouter,Depends,status
from services.categorie_service import(
    recuperer_categories,
    modifier_categorie,
    creer_categorie,supprimer_categorie
)
from database.dependency import get_db
from schemas.categorie import CategorieResponse,CategorieUpdate,CategorieCreate
from sqlalchemy.orm import Session
from models.categorie import Categorie



router = APIRouter(
    prefix=("/categories"),
    tags= ["Categorie"]
)
 
@router.get("/",
    response_model=list[CategorieResponse],
    summary="Listes des categories",
    description="retourner les categories"
)
def get_categories(
    db:Session = Depends(get_db)
):
    return recuperer_categories(db)

@router.patch("/{categorie_id}",
    response_model=CategorieResponse,
    summary="Modifier une categorie",
    description="retourner categorie"
)
def update_categorie(
    categorie_id:int,
    categorie_update:CategorieUpdate,
    db:Session = Depends(get_db)
):
    return modifier_categorie(db,categorie_update,categorie_id)

@router.post("/",
    response_model=CategorieResponse,
    summary="Creer une Categoris",
    status_code=status.HTTP_201_CREATED
)
def create_categorie(
    categorie :CategorieCreate,
    db:Session = Depends(get_db)
):
    categorie_db = Categorie(
        **categorie.model_dump()
    )
    return creer_categorie(db,categorie_db)

@router.delete("{categorie_id}",
    summary="Supprimer une categorie"
)
def delete_categorie(
    categorie_id:int,
    db:Session = Depends(get_db)
):
    return supprimer_categorie(db,categorie_id)