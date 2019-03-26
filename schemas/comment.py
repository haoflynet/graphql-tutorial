import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import CommentModel
from schemas import PageSchema


class CommentSchema(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        description = "评论Schema"


class CommentPageSchema(PageSchema):
    datas = graphene.List("schemas.CommentSchema", description="评论列表")

    class Meta:
        description = "评论列表"
