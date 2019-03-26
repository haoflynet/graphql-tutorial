from sqlalchemy import Column, Integer, Text, String, TIMESTAMP

from db import Base


class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, doc="文章ID")
    author_id = Column(Integer, doc="作者ID")
    content = Column(Text, doc="文章内容")
    title = Column(String(255), doc="文章标题")

    created_at = Column(TIMESTAMP, doc="创建时间")
    updated_at = Column(TIMESTAMP, doc="更新时间")
