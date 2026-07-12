from fastapi import APIRouter,Depends,status
from services.role_service import(
    recuperer_roles,
    recuperer_role,
    modifier_role,
    creer_role,supprimer_role
)
from database.dependency import get_db
from schemas.role import RoleResponse,RoleUpdate,RoleCreate
from sqlalchemy.orm import Session
from models.role import Role



router = APIRouter(
    prefix=("/roles"),
    tags= ["Roles"]
)

@router.post("/",
    response_model=RoleResponse,
    summary="Creer un Role",
    status_code=status.HTTP_201_CREATED
)
def create_role(
    role :RoleCreate,
    db:Session = Depends(get_db)
):
    role_db = Role(
        **role.model_dump()
    )
    return creer_role(db,role_db)


@router.get("/",
    response_model=list[RoleResponse],
    summary="Listes des Roles",
    description="retourner les roles"
)
def get_roles(
    db:Session = Depends(get_db)
):
    return recuperer_roles(db)

@router.get("/{role_id}",
    response_model=RoleResponse,
    summary="Un Role",
    description="retourner les roles"
)
def get_role(
    role_id:int,
    db:Session = Depends(get_db)

):
    return recuperer_role(db,role_id)


@router.patch("/{role_id}",
    response_model=RoleResponse,
    summary="Modifier un Role",
    description="retourner categorie"
)
def update_role(
    role_id:int,
    role_update:RoleUpdate,
    db:Session = Depends(get_db)
):
    return modifier_role(db,role_update,role_id)


@router.delete("/{role_id}",
    summary="Supprimer un role"
)
def delete_role(
    role_id:int,
    db:Session = Depends(get_db)
):
    return supprimer_role(db,role_id)

