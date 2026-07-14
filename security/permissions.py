from fastapi import Depends
from models.utilisateur import Utilisateur
from security.auth import get_current_user
from core.exceptions import ForbiddenException

def role_required(role: str):

    def verifier(
        current_user: Utilisateur = Depends(get_current_user)
    ):

        if current_user.role.nom != role:

            raise ForbiddenException(
                "Permission refusée."
            )

        return current_user

    return verifier