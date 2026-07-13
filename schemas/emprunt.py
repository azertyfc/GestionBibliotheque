from pydantic import ConfigDict,Field,BaseModel
from datetime import datetime
from schemas.utilisateur import UtilisateurResponse
from schemas.livre import LivreResponse

class EmpruntResponse(BaseModel):

    id:int
    
    date_emprunt:datetime 

    date_retour : datetime
   
    date_retour_prevue: datetime

    utilisateur:UtilisateurResponse

    livre:LivreResponse

    model_config = ConfigDict(from_attributes=True)