from pydantic import ConfigDict,Field,BaseModel

class RoleResponse(BaseModel):

    nom : str

    model_config=ConfigDict(from_attributes=True)

class RoleCreate(BaseModel):
     
    nom : str = Field(min_length=4,max_length=10)

class RoleUpdate(BaseModel):

    nom: str | None = None
