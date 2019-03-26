import graphene

from mutations.article import DeleteArticle, CreateArticle, UpdateArticle
from mutations.author import DeleteAuthor, CreateAuthor, UpdateAuthor
from mutations.comment import DeleteComment, CreateComment, UpdateComment


class Mutation(graphene.ObjectType):
    create_article = CreateArticle.Field(description="创建文章")
    delete_article = DeleteArticle.Field(description="删除文章")
    update_article = UpdateArticle.Field(description="更新文章")
    create_author = CreateAuthor.Field(description="创建作者")
    delete_author = DeleteAuthor.Field(description="删除作者")
    update_author = UpdateAuthor.Field(description="更新作者")
    create_comment = CreateComment.Field(description="创建评论")
    delete_comment = DeleteComment.Field(description="删除评论")
    update_comment = UpdateComment.Field(description="更新评论")
