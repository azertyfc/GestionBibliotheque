from sqlalchemy import Column, Integer, String
from database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column
    
class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String, unique=True, index=True) 
    utilisateurs = relationship("Utilisateur", back_populates="role")
