import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import AuthorModel
from schemas import PageSchema


class AuthorSchema(SQLAlchemyObjectType):
    class Meta:
        model = AuthorModel
        exclude_fields = ("deleted_at",)


class AuthorPageSchema(PageSchema):
    datas = graphene.List("schemas.AuthorSchema")
