from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "postgresql://testdb_rw8b_user:mbgkdPtCqr1R26CH1xeTB5nTPgMEIVzo@dpg-cfn8v6ta499f28aeurdg-a.frankfurt-postgres.render.com/testdb_rw8b"

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()