from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database.base import Base

class User(Base):
    __tablename__= "users"

    id:Mapped[UUID]=mapped_column(
        primary_key=True,
        default=uuid4,
    )

    full_name: Mapped[str]=mapped_column(
        String(100),
        nullable=False,
    )

    email: Mapped[str]=mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    hashed_password : Mapped[str]=mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool]=mapped_column(
        Boolean,
        default=True,
    )

    created_at: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    documents = relationship(
        "Document",
        back_populates="owner"
    )

