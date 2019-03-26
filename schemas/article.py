import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models import ArticleModel
from schemas import PageSchema


class ArticleSchema(SQLAlchemyObjectType):
    author = graphene.Field("schemas.AuthorSchema", description="文章作者信息")
    comments = graphene.List("schemas.CommentSchema", description="文章评论列表")

    class Meta:
        model = ArticleModel
        description = "文章Schema"

    def resolve_author(self, info):
        return (
            info.context.get("AuthorsDataLoader")
            .load(self.author_id)
            .then(lambda response: response)
        )

    def resolve_comments(self, info):
        return (
            info.context.get("ArticleCommentsDataLoader")
            .load(self.id)
            .then(
                lambda response: []
                if response is None
                else (response if isinstance(response, list) else [response])
            )
        )


class ArticlePageSchema(PageSchema):
    datas = graphene.List("schemas.ArticleSchema", description="文章列表")

    class Meta:
        description = "文章列表"
