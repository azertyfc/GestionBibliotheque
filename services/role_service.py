from sqlalchemy import select
from sqlalchemy.orm import Session
from models.role import Role
from schemas.role import RoleUpdate,RoleCreate


def creer_role(
    db:Session,
    role:Role
):
    try:
        db.add(role)
        db.commit()
        db.refresh(role)

        return role
    except Exception:

        db.rollback()
        raise

def recuperer_roles(
    db:Session
):
    try:

        return (
            db.execute(select(Role))
            .scalars().all()
        )
    
    except Exception:
        db.rollback()
        raise

def recuperer_role(
    db:Session,
    role_id:int
):
    try:

        return (
            db.execute(select(Role).where(Role.id==role_id))
            .scalar_one_or_none()
        )
    
    except Exception:
        db.rollback()
        raise

def supprimer_role(
    db:Session,
    role_id:int
):
    try:

        role = db.execute(select(Role).where(Role.id==role_id)).scalar_one_or_none()
        if role is None:
            raise ValueError("Role Introuvable")
        
        db.delete(role)
        db.commit()
        return {"message": "Role supprimée avec succès"}
    
    except Exception:
        db.rollback()
        raise

def modifier_role(
    db:Session,
    role_update:RoleUpdate,
    role_id:int
):
    try:
        role = db.execute(select(Role).where(Role.id==role_id)).scalar_one_or_none()

        if role is None:
            raise ValueError("Role Introuvable")
        
        for champs,valeur in role_update.model_dump(
            exclude_unset=True
        ).items():
            setattr(
                role,
                champs,
                valeur
            )
        db.commit()
        db.refresh(role)
        return role

    except Exception:
        db.rollback()
        raise