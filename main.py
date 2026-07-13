from fastapi import FastAPI
import models
from routers.livre_router import router as livre_router
from routers.categorie_router import router as categorie_router
from routers.role_router import router as role_router
from routers.utilisateur_router import router as utilisateur_router


app = FastAPI()


app.include_router(livre_router)
app.include_router(categorie_router)
app.include_router(role_router)
app.include_router(utilisateur_router)