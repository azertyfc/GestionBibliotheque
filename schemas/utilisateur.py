from pydantic import ConfigDict,Field,BaseModel
from schemas.role import RoleResponse

class UtilisateurResponse(BaseModel):

    id:int

    nom:str

    prenom:str

    email:str
    
    role:RoleResponse
