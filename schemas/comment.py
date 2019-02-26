import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import CommentModel
from schemas import PageSchema


class CommentSchema(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        exclude_fields = ("deleted_at",)


class CommentPageSchema(PageSchema):
    datas = graphene.List("schemas.CommentSchema")
