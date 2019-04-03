from promise import Promise
from promise.dataloader import DataLoader

from db import DBSession
from models import OrdinaryWriterModel


class OrdinaryWriterManager:
    @staticmethod
    def get_one(**args) -> OrdinaryWriterModel:
        query = DBSession().query(OrdinaryWriterModel)

        if "id" in args:
            query = query.filter(OrdinaryWriterModel.id == args["id"])
        if "author_id" in args:
            query = query.filter(OrdinaryWriterModel.author_id == args["author_id"])

        return query.first()


class OrdinaryWritersDataLoader(DataLoader):
    def batch_load_fn(self, author_ids):
        query = (
            DBSession()
            .query(OrdinaryWriterModel)
            .filter(OrdinaryWriterModel.author_id.in_(author_ids))
        )
        writers = dict([writer.author_id, writer] for writer in query.all())
        result = [writers.get(str(author_id), None) for author_id in author_ids]
        return Promise.resolve(result)
