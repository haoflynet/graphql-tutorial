from sqlalchemy import Column, Integer, String

from db import Base


class ProfessionalWriterModel(Base):
    __tablename__ = "professional_writers"

    id = Column(Integer, primary_key=True, doc="自增ID")
    author_id = Column(Integer, doc="对应的author_id")
    publishing_house = Column(String, doc="出版社")
