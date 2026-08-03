from sqlalchemy.orm import sessionmaker, Session
from collections.abc import Generator

from app.database.database import engine

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocomit=False,
)

def get_db() -> Generator[Session, None, None]:
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close
