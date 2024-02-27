from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://common_user:password_default@database/fastapi_docker_db"
# SQLALCHEMY_DATABASE_URL = "postgresql://common_user:bl4cksh33p@localhost/fastapi_docker_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()