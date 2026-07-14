"""
Gestion des mots de passe.

Ce fichier est responsable de :
- Hasher les mots de passe avant de les enregistrer.
- Vérifier qu'un mot de passe saisi correspond au hash stocké.

Le mot de passe n'est JAMAIS enregistré en clair.
"""

from passlib.context import CryptContext

# Algorithme utilisé pour hasher les mots de passe.
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Transforme un mot de passe en hash.

    Exemple :
        "azerty123"
            ↓
        "$2b$12$...."
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Vérifie si le mot de passe saisi est correct.

    Retourne True si le mot de passe est valide.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password
    )