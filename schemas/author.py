import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import AuthorModel
from schemas import PageSchema
from schemas.interfaces import AuthorWriterInterface


class AuthorSchema(SQLAlchemyObjectType):
    writer = graphene.Field(AuthorWriterInterface, description="作者类型对应的信息")

    def resolve_writer(self, info):
        if self.writer_type == "ordinary":
            return (
                info.context.get("OrdinaryWritersDataLoader")
                .load(self.id)
                .then(lambda response: response)
            )
        else:
            return (
                info.context.get("ProfessionalWritersDataLoader")
                .load(self.id)
                .then(lambda response: response)
            )

    class Meta:
        model = AuthorModel
        description = "作者Schema"


class AuthorPageSchema(PageSchema):
    datas = graphene.List("schemas.AuthorSchema", description="作者列表")

    class Meta:
        description = "作者列表"
