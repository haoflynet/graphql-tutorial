from sqlalchemy import Integer, Column, Text, TIMESTAMP

from db import Base


class CommentModel(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, doc="评论ID")
    article_id = Column(Integer, doc="文章ID")
    content = Column(Text, doc="评论内容")

    created_at = Column(TIMESTAMP, doc="创建时间")
    updated_at = Column(TIMESTAMP, doc="更新时间")
