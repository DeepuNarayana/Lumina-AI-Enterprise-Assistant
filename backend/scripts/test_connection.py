# test_connection.py

from sqlalchemy import create_engine
from app.config.settings import settings

print(settings.DATABASE_URL)

engine = create_engine(settings.DATABASE_URL)

with engine.connect() as conn:
    print("Connected Successfully!")