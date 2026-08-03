from sqlalchemy import Column, Integer, String, Float

from app.database.base import Base

class Sales(Base):

    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    customer = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    region= Column(String, nullable=False)


