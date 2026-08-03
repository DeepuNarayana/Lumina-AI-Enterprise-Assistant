from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


from app.database.base import Base

class Document(Base):

    __tablename__= "documents"

    id: Mapped[int] = mapped_column(primary_key=True, index= True)

    filename: Mapped[str] = mapped_column(String(255))

    s3_key: Mapped[str] = mapped_column(String(255))

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner = relationship(
        "User",
        back_populates="documents"
        )
