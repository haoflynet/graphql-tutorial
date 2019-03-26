import graphene

from managers.author import AuthorManager
from schemas import AuthorSchema


class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    author = graphene.Field(lambda: AuthorSchema)

    def mutate(self, info, name):
        return CreateAuthor(ok=True, author=AuthorManager.create_one(name=name))


class UpdateAuthor(graphene.Mutation):
    class Arguments:
        author_id = graphene.Int(required=True)
        name = graphene.String()

    ok = graphene.Boolean()
    author = graphene.Field(lambda: AuthorSchema)

    def mutate(self, info, author_id, name):
        return UpdateAuthor(
            ok=True, author=AuthorManager.update_one(author_id=author_id, name=name)
        )


class DeleteAuthor(graphene.Mutation):
    class Arguments:
        author_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, author_id):
        AuthorManager.delete_one(author_id=author_id)
        return DeleteAuthor(ok=True)
