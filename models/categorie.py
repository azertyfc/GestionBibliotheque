from sqlalchemy import  Integer, String
from database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped, mapped_column


class Categorie(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nom: Mapped[str] = mapped_column(String, unique=True, index=True)
    livres = relationship("Livre", back_populates="categorie")

