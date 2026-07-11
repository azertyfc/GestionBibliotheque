from sqlalchemy import Column, Integer, String
from database.base import Base  
from  sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column


class Emprunt(Base):    
    __tablename__ = "emprunts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    utilisateur_id: Mapped[int] = mapped_column(
    Integer,
    ForeignKey("utilisateurs.id"),
    nullable=False
    )  
    livre_id: Mapped[int] = mapped_column(
    Integer,
    ForeignKey("livres.id"),
    nullable=False
    ) 
    date_emprunt: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow
    )
    date_retour_prevue: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    utilisateur = relationship("Utilisateur", back_populates="emprunts")
    livre = relationship("Livre", back_populates="emprunts")  


