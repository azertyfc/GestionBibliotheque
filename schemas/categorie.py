from pydantic import ConfigDict,BaseModel,Field


class CategorieResponse(BaseModel):

    id:int

    nom:str

    model_config = ConfigDict(from_attributes=True)

class CategorieCreate(BaseModel):

    nom:str = Field(min_length=4,max_length=20)

class CategorieUpdate(BaseModel):

    nom : str | None = None
