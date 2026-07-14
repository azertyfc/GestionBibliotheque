"""
Gestion de l'authentification.

Ce fichier est responsable de :

- Récupérer le JWT envoyé par le client.
- Vérifier que le JWT est valide.
- Récupérer l'utilisateur connecté.
- Retourner current_user aux routes protégées.

Ce fichier ne crée PAS le token.
Il vérifie uniquement que le token reçu est valide.
"""

from fastapi import Depends

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from sqlalchemy import select

from database.dependency import get_db

from models.utilisateur import Utilisateur

from security.jwt import decode_access_token

from core.exceptions import UnauthorizedException


# ------------------------------------------------------------------
# Swagger
# ------------------------------------------------------------------

# Toutes les routes protégées utiliseront automatiquement
# le token envoyé dans :
#
# Authorization: Bearer xxxxxxxxxxxxx
#
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


# ------------------------------------------------------------------
# Utilisateur connecté
# ------------------------------------------------------------------

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

) -> Utilisateur:
    """
    Retourne l'utilisateur actuellement connecté.

    Fonctionnement :

        JWT

            ↓

        decode()

            ↓

        email

            ↓

        SELECT utilisateur

            ↓

        return utilisateur
    """

    # -----------------------------
    # Décoder le JWT
    # -----------------------------

    payload = decode_access_token(token)

    if payload is None:

        raise UnauthorizedException(
            "Token invalide."
        )

    # -----------------------------
    # Récupération du subject
    # -----------------------------

    email = payload.get("sub")

    if email is None:

        raise UnauthorizedException(
            "Token invalide."
        )

    # -----------------------------
    # Recherche utilisateur
    # -----------------------------

    utilisateur = db.execute(

        select(Utilisateur)

        .where(
            Utilisateur.email == email
        )

    ).scalar_one_or_none()

    if utilisateur is None:

        raise UnauthorizedException(
            "Utilisateur introuvable."
        )

    # -----------------------------
    # Utilisateur authentifié
    # -----------------------------

    return utilisateur