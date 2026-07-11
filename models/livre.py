"""Livre model.py
This module defines the Livre model, which represents a book in the application.
Attributes:
    id (int): The unique identifier for the book.
    title (str): The title of the book.
    author (str): The author of the book.
    publication_date (date): The publication date of the book.  
"""
from sqlalchemy import Column, Integer, String, Date
from database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column



class Livre(Base):

    """Livre model representing a book in the application."""
    
    __tablename__ = "livres"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    auteur: Mapped[str] = mapped_column(String, nullable=False)
    isbn: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    date_publication: Mapped[Date] = mapped_column(Date, nullable=False)
    quantite_disponible: Mapped[int] = mapped_column(Integer, nullable=False, default=0)  # Available quantity of the book
    categorie_id: Mapped[int] = mapped_column(
    Integer,
    ForeignKey("categories.id"),
    nullable=False
)
    categorie = relationship("Categorie", back_populates="livres")
    emprunts = relationship("Emprunt", back_populates="livre")
