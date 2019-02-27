import math

import graphene
from graphene import ObjectType

from managers.article import (
    ArticlesDataLoader,
    ArticleManager,
    ArticleCommentsDataLoader,
)
from managers.author import AuthorsDataLoader, AuthorManager
from managers.comment import CommentsDataLoader, CommentManager


class PageInfoSchema(ObjectType):
    """
    专用于分页的schema
    """

    total = graphene.Int(description="总条数")
    current_page = graphene.Int(description="当前页码")
    per_page = graphene.Int(description="每页数量")
    total_pages = graphene.Int(description="总共页码数量")

    @staticmethod
    def paginate(total: int, current_page: int, per_page: int):
        """
        :param total: 总共条数
        :param current_page: 当前页码
        :param per_page: 每页数量
        :return:
        """
        return PageInfoSchema(
            total=int(total),
            current_page=int(current_page),
            per_page=int(per_page),
            total_pages=math.ceil(int(total) / int(per_page)),
        )


class PageSchema(ObjectType):
    page_info = graphene.Field("schemas.PageInfoSchema")


from schemas.article import ArticleSchema, ArticlePageSchema
from schemas.author import AuthorSchema, AuthorPageSchema
from schemas.comment import CommentSchema, CommentPageSchema

__all__ = [
    PageInfoSchema.__class__,
    ArticleSchema.__class__,
    ArticlePageSchema.__class__,
    AuthorSchema.__class__,
    AuthorPageSchema.__class__,
    CommentSchema.__class__,
    CommentPageSchema.__class__,
]


def get_dataloaders():
    return {
        "ArticlesDataLoader": ArticlesDataLoader(cache=False),
        "AuthorsDataLoader": AuthorsDataLoader(cache=False),
        "CommentsDataLoader": CommentsDataLoader(cache=False),
        "ArticleCommentsDataLoader": ArticleCommentsDataLoader(cache=False),
    }


class Query(graphene.ObjectType):
    article = graphene.Field(
        ArticleSchema, title=graphene.String(description="文章标题"), description="单个查询"
    )
    articles = graphene.Field(
        "schemas.ArticlePageSchema",
        page=graphene.Int(description="页码数(默认为1)"),
        limit=graphene.Int(description="每页数量(默认为20)"),
        description="文章列表查询",
    )
    author = graphene.Field(AuthorSchema, title=graphene.String(description="文章标题"))
    authors = graphene.Field(
        "schemas.AuthorPageSchema",
        page=graphene.Int(description="页码数(默认为1)"),
        limit=graphene.Int(description="每页数量(默认为20)"),
        description="作者列表查询",
    )
    comment = graphene.Field(CommentSchema, title=graphene.String(description="文章标题"))
    comments = graphene.Field(
        "schemas.CommentPageSchema",
        page=graphene.Int(description="页码数(默认为1)"),
        limit=graphene.Int(description="每页数量(默认为20)"),
        description="评论列表查询",
    )

    def resolve_article(self, info, **kwargs):
        return ArticleManager.get_one(**kwargs)

    def resolve_articles(self, info, **kwargs):
        articles, page_info = ArticleManager.get_list(_paginated=True, **kwargs)
        return ArticlePageSchema(page_info=page_info, datas=articles)

    def resolve_author(self, info, **kwargs):
        return AuthorManager.get_one(**kwargs)

    def resolve_authors(self, info, **kwargs):
        authors, page_info = AuthorManager.get_list(_paginated=True, **kwargs)
        return AuthorPageSchema(page_info=page_info, datas=authors)

    def resolve_comment(self, info, **kwargs):
        return CommentManager.get_one(**kwargs)

    def resolve_comments(self, info, **kwargs):
        comments, page_info = CommentManager.get_list(_paginated=True, **kwargs)
        return CommentPageSchema(page_info=page_info, datas=comments)


Schema = graphene.Schema(query=Query)
