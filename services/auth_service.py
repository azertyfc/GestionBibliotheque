"""
Service d'authentification.

Responsable de :

- vérifier les identifiants
- générer le JWT
"""

from sqlalchemy.orm import Session
from sqlalchemy import select

from models.utilisateur import Utilisateur

from security.password import verify_password
from security.jwt import create_access_token

from core.exceptions import UnauthorizedException
from core.logger import logger


def login(
    db: Session,
    username: str,
    password: str
):
    """
    Authentifie un utilisateur.
    """

    utilisateur = db.execute(

        select(Utilisateur)

        .where(
            Utilisateur.email == username
        )

    ).scalar_one_or_none()

    print("Username reçu :", username)
    print("Utilisateur trouvé :", utilisateur)

    if utilisateur is None:

        logger.warning(
            "Tentative de connexion avec un email inexistant : %s",
            username
        )

        raise UnauthorizedException(
            "Email ou mot de passe incorrect."
        )
    
    print("USERNAME :", username)
    print("PASSWORD :", password)
    print("LONGUEUR PASSWORD :", len(password))
    print("HASH BDD :", utilisateur.mot_de_passe)
    print("LONGUEUR HASH :", len(utilisateur.mot_de_passe))

    if not verify_password(
        password,
        utilisateur.mot_de_passe
    ):

        logger.warning(
            "Mot de passe incorrect : %s",
            username
        )

        raise UnauthorizedException(
            "Email ou mot de passe incorrect."
        )

    logger.info(
        "Connexion réussie : %s",
        utilisateur.email
    )

    access_token = create_access_token(
        {
            "sub": utilisateur.email
        }
    )

    return {

        "access_token": access_token,

        "token_type": "bearer"

    }