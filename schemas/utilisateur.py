from pydantic import ConfigDict,Field,BaseModel,EmailStr
from schemas.role import RoleResponse
class UtilisateurResponse(BaseModel):

    id:int

    nom:str

    prenom:str

    email:str
    
    role:RoleResponse


class UtilisateurUpdate(BaseModel):

    prenom: str | None = None

    nom: str | None = None

    role_id: int | None = None


class UtilisateurCreate(BaseModel):
    """
    Schema utilisé lors de la création d'un utilisateur.
    """

    nom: str = Field(
        min_length=2,
        max_length=50
    )

    prenom: str = Field(
        min_length=2,
        max_length=50
    )

    email: EmailStr

    mot_de_passe: str = Field(
        min_length=6,
        max_length=100
    )

    role_id: int