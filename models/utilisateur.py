from sqlalchemy import Column, Integer, String
from database.base import Base  
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String, nullable=False)
    prenom: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    mot_de_passe: Mapped[str] = mapped_column(String, nullable=False)
    role_id: Mapped[int] = mapped_column(
    Integer,
    ForeignKey("roles.id"),
    nullable=False
    ) 
    role = relationship("Role")
    emprunts = relationship("Emprunt", back_populates="utilisateur")