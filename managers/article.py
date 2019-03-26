from promise import Promise
from promise.dataloader import DataLoader
from sqlalchemy import desc

import schemas
from db import DBSession
from models import ArticleModel, CommentModel


class ArticleManager:
    @staticmethod
    def update_one(article_id, **args) -> ArticleModel:
        article = ArticleManager.get_one(article_id=article_id)

        if "content" in args:
            article.content = args["content"]
        if "title" in args:
            article.title = args["title"]
        DBSession().flush()
        return article

    @staticmethod
    def delete_one(article_id):
        DBSession().delete(ArticleManager.get_one(id=article_id))
        DBSession().flush()

    @staticmethod
    def create_one(author_id, content, title) -> ArticleModel:
        article = ArticleModel(author_id=author_id, content=content, title=title)
        DBSession().add(article)
        DBSession().flush()
        return article

    @staticmethod
    def get_one(**args) -> ArticleModel:
        query = DBSession().query(ArticleModel)

        if "id" in args:
            query = query.filter(ArticleModel.id == args["id"])
        if "title" in args:
            pass

        return query.first()

    @staticmethod
    def get_list(_fields: list = None, _paginated: bool = False, **kwargs):
        page = 1 if "page" not in kwargs else int(kwargs["page"])
        limit = 20 if "limit" not in kwargs else int(kwargs["limit"])

        query = DBSession().query(ArticleModel)

        if "created_at_ge" in kwargs:
            query = query.filter(ArticleModel.created_at >= kwargs["created_at_ge"])

        if "created_at_le" in kwargs:
            query = query.filter(ArticleModel.created_at <= kwargs["created_at_le"])

        if _fields is not None:
            query = query.with_entities(
                *[getattr(ArticleModel, _field) for _field in _fields]
            )

        if limit != 0:
            datas = (
                query.order_by(desc(ArticleModel.created_at))
                .limit(limit)
                .offset((page - 1) * limit)
            )
        else:
            datas = query.order_by(desc(ArticleModel.created_at))

        if _paginated:
            total = query.count()
            return datas, schemas.PageInfoSchema.paginate(total, page, limit)
        else:
            return datas


class ArticlesDataLoader(DataLoader):
    def batch_load_fn(self, ids):
        query = DBSession().query(ArticleModel).filter(ArticleModel.id.in_(ids))
        articles = dict([(article.id, article) for article in query.all()])
        return Promise.resolve([articles.get(id, None) for id in ids])


class ArticleCommentsDataLoader(DataLoader):
    def batch_load_fn(self, ids):
        query = DBSession().query(CommentModel).filter(CommentModel.article_id.in_(ids))
        article_comments = {}
        for comment in query.all():
            if comment.article_id in article_comments:
                article_comments[comment.article_id].append(comment)
            else:
                article_comments[comment.article_id] = [comment]

        return Promise.resolve(
            [article_comments.get(article_id, None) for article_id in ids]
        )
