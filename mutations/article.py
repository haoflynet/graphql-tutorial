import graphene

from managers.article import ArticleManager
from schemas import ArticleSchema


class CreateArticle(graphene.Mutation):
    class Arguments:
        author_id = graphene.Int(required=True)
        content = graphene.String()
        title = graphene.String()

    ok = graphene.Boolean()
    article = graphene.Field(lambda: ArticleSchema)

    def mutate(self, info, author_id, content, title):
        return CreateArticle(
            ok=True,
            article=ArticleManager.create_one(
                author_id=author_id, content=content, title=title
            ),
        )


class UpdateArticle(graphene.Mutation):
    class Arguments:
        article_id = graphene.Int(required=True)
        content = graphene.String()
        title = graphene.String()

    ok = graphene.Boolean()
    article = graphene.Field(lambda: ArticleSchema)

    def mutate(self, info, article_id=0, **args):
        return UpdateArticle(
            ok=True, article=ArticleManager.update_one(article_id=article_id, **args)
        )


class DeleteArticle(graphene.Mutation):
    class Arguments:
        article_id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, article_id):
        ArticleManager.delete_one(article_id=article_id)
        return DeleteArticle(ok=True)
