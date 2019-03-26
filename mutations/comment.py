import graphene

from managers.comment import CommentManager
from schemas import CommentSchema


class CreateComment(graphene.Mutation):
    class Arguments:
        article_id = graphene.Int(required=True)
        content = graphene.String()

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentSchema)

    def mutate(self, info, article_id, content):
        return CreateComment(
            ok=True,
            comment=CommentManager.create_one(article_id=article_id, content=content),
        )


class UpdateComment(graphene.Mutation):
    class Arguments:
        comment_id = graphene.Int(required=True)
        content = graphene.String()

    ok = graphene.Boolean()
    comment = graphene.Field(lambda: CommentSchema)

    def mutate(self, info, comment_id, content):
        return UpdateComment(
            ok=True, comment=CommentManager.update_one(id=comment_id, content=content)
        )


class DeleteComment(graphene.Mutation):
    class Arguments:
        comment_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, comment_id):
        CommentManager.delete_one(id=comment_id)
        return DeleteComment(ok=True)
