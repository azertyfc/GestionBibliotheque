from decimal import Decimal
from pydantic import BaseModel,EmailStr,Field,ConfigDict,field_validator
from datetime import datetime,date
from schemas.categorie import CategorieResponse


class LivreCreate(BaseModel):
     
    date_naissance: date

    @field_validator("date_naissance")
    @classmethod
    def verifier_age(cls, valeur):

        age = (date.today() - valeur).days // 365

        if age < 18:
            raise ValueError(
                "Le client doit être majeur."
            )

        return valeur
    
    nom: str = Field(min_length=2, max_length=100)

    prenom: str = Field(min_length=2, max_length=100)

    email: EmailStr

    revenu_declare: Decimal = Field(gt=0)
    
class LivreResponse(BaseModel):

    id: int

    titre: str

    auteur: str

    isbn: str

    quantite_disponible: int

    date_publication: datetime

    categorie: CategorieResponse

    model_config = ConfigDict(from_attributes=True)



class LivreUpdate(BaseModel):

    titre: str | None = None

    auteur: str | None = None

    isbn: str | None = None

    quantite_disponible: int | None = None

    date_publication: datetime | None = None

    categorie_id: int | None = None

