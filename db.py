from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_DATABASE

Base = declarative_base()

engine = create_engine(
    "mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?charset=utf8".format(
        DB_USERNAME=DB_USERNAME,
        DB_PASSWORD=DB_PASSWORD,
        DB_HOST=DB_HOST,
        DB_DATABASE=DB_DATABASE,
    ),
    echo=True,
    pool_size=100,
    pool_recycle=5,
    pool_timeout=60,
    pool_pre_ping=True,
    max_overflow=0,
)
DBSession = sessionmaker(bind=engine, autocommit=True)
DBSession = scoped_session(DBSession)
db_session = DBSession()
