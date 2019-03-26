from sqlalchemy import Column, Integer, String, TIMESTAMP

from db import Base


class AuthorModel(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, doc="作者ID")
    name = Column(String(50), doc="作者姓名")

    created_at = Column(TIMESTAMP, doc="创建时间")
    updated_at = Column(TIMESTAMP, doc="更新时间")
