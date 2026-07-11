from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///database/bibliotheque.db"

engine = create_engine(DATABASE_URL, echo=True)