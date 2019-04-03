import graphene
from graphene import Interface


class AuthorWriterInterface(Interface):
    author_id = graphene.Int()
