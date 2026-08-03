from sqlalchemy import create_engine

from app.config.settings import settings

engine= create_engine(
    settings.DATABASE_URL,
    echo= True, # this will tells SQLALCHEMY to print every SQL querry
    pool_pre_ping=True
)