from fastapi import FastAPI
import models
from routers.livre_router import router as livre_router
from routers.categorie_router import router as categorie_router
from routers.role_router import router as role_router
from routers.utilisateur_router import router as utilisateur_router
from routers.emprunt_router import router as emprunt_router
from core.exception_handlers import register_exception_handlers
from core.middleware import register_middlewares
from routers.auth_router import router as auth_router


app = FastAPI()
register_middlewares(app)
register_exception_handlers(app)
app.include_router(livre_router)
app.include_router(categorie_router)
app.include_router(role_router)
app.include_router(utilisateur_router)
app.include_router(emprunt_router)
app.include_router(auth_router)