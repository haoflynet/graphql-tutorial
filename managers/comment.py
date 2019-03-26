from promise import Promise
from promise.dataloader import DataLoader
from sqlalchemy import desc

import schemas
from db import DBSession
from models import CommentModel


class CommentManager:
    @staticmethod
    def create_one(article_id, content):
        comment = CommentModel(article_id=article_id, content=content)
        DBSession().add(comment)
        DBSession().flush()
        return comment

    @staticmethod
    def update_one(id, content) -> CommentModel:
        comment = CommentManager.get_one(id=id)
        comment.content = content
        DBSession().flush()
        return comment

    @staticmethod
    def delete_one(id):
        DBSession().delete(CommentManager.get_one(id=id))
        DBSession().flush()

    @staticmethod
    def get_one(**args) -> CommentModel:
        query = DBSession().query(CommentModel)

        if "id" in args:
            query = query.filter(CommentModel.id == args["id"])

        return query.first()

    @staticmethod
    def get_list(_fields: list = None, _paginated: bool = False, **kwargs):
        page = 1 if "page" not in kwargs else int(kwargs["page"])
        limit = 20 if "limit" not in kwargs else int(kwargs["limit"])

        query = DBSession().query(CommentModel)

        if "created_at_ge" in kwargs:
            query = query.filter(CommentModel.created_at >= kwargs["created_at_ge"])

        if "created_at_le" in kwargs:
            query = query.filter(CommentModel.created_at <= kwargs["created_at_le"])

        if _fields is not None:
            query = query.with_entities(
                *[getattr(CommentModel, _field) for _field in _fields]
            )

        if limit != 0:
            datas = (
                query.order_by(desc(CommentModel.created_at))
                .limit(limit)
                .offset((page - 1) * limit)
            )
        else:
            datas = query.order_by(desc(CommentModel.created_at))

        if _paginated:
            total = query.count()
            return datas, schemas.PageInfoSchema.paginate(total, page, limit)
        else:
            return datas


class CommentsDataLoader(DataLoader):
    def batch_load_fn(self, ids):
        query = DBSession().query(CommentModel).filter(CommentModel.id.in_(ids))
        articles = dict([(article.id, article) for article in query.all()])
        return Promise.resolve([articles.get(id, None) for id in ids])
