from sqlalchemy import Column, Integer, String

from db import Base


class OrdinaryWriterModel(Base):
    __tablename__ = "ordinary_writers"

    id = Column(Integer, primary_key=True, doc="自增ID")
    author_id = Column(Integer, doc="对应的author_id")
    job = Column(String, doc="职业")
