"""
Gestion des JSON Web Tokens (JWT).

Ce fichier permet :

- de créer un token lors de la connexion.
- de décoder un token envoyé par le client.

Le JWT permet d'identifier l'utilisateur connecté.
"""

from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError
from core.config import settings

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

SECRET_KEY = settings.SECRET_KEY

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


# ---------------------------------------------------------------------
# Création du token
# ---------------------------------------------------------------------

def create_access_token(
    data: dict
) -> str:
    """
    Crée un JWT.

    Le dictionnaire reçu est copié puis on ajoute
    la date d'expiration.

    Exemple :

    {
        "sub": "jean@test.com"
    }

            ↓

    {
        "sub": "...",
        "exp": ...
    }
    """

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ---------------------------------------------------------------------
# Décodage du token
# ---------------------------------------------------------------------

def decode_access_token(
    token: str
):
    """
    Décode un JWT.

    Retourne le payload si le token est valide.

    Retourne None si :

    - signature invalide
    - token expiré
    - token modifié
    """

    try:

        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

    except JWTError:

        return None