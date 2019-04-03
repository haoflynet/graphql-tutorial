from graphene_sqlalchemy import SQLAlchemyObjectType

from models import ProfessionalWriterModel
from schemas.interfaces import AuthorWriterInterface


class ProfessionalWriterSchema(SQLAlchemyObjectType):
    class Meta:
        model = ProfessionalWriterModel
        interfaces = (AuthorWriterInterface,)
