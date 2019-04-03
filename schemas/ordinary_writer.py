from graphene_sqlalchemy import SQLAlchemyObjectType

from models import OrdinaryWriterModel
from schemas.interfaces import AuthorWriterInterface


class OrdinaryWriterSchema(SQLAlchemyObjectType):
    class Meta:
        model = OrdinaryWriterModel
        interfaces = (AuthorWriterInterface,)
