from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base

from models.emprunt import Emprunt


class Penalite(Base):
    __tablename__ = "penalites"

    id: Mapped[int] = mapped_column(primary_key=True)

    emprunt_id: Mapped[int] = mapped_column(
        ForeignKey("emprunts.id"),
        nullable=False
    )

    montant: Mapped[float] = mapped_column(Float, nullable=False)

    motif: Mapped[str] = mapped_column(String, nullable=False)

    date_creation: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    est_payee: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    emprunt: Mapped["Emprunt"] = relationship(
        back_populates="penalites"
    )