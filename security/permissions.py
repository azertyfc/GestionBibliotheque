from fastapi import Depends, HTTPException, status
from models.utilisateur import Utilisateur
from security.auth import get_current_user

def bibliothecaire_required(
    current_user: Utilisateur = Depends(get_current_user)
):
    if current_user.role.nom != "bibliothecaire":
        raise HTTPException(
            status_code=403,
            detail="Accès réservé aux bibliothécaires"
        )

    return current_user