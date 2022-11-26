from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conexion = create_engine('postgresql://criss:1234@localhost:5432/tweets')
Session = sessionmaker(bind=conexion)
Base = declarative_base()