from promise import Promise
from promise.dataloader import DataLoader

from db import DBSession
from models import ProfessionalWriterModel


class ProfessionalWriterManager:
    @staticmethod
    def get_one(**args) -> ProfessionalWriterModel:
        query = DBSession().query(ProfessionalWriterModel)

        if "id" in args:
            query = query.filter(ProfessionalWriterModel.id == args["id"])
        if "author_id" in args:
            query = query.filter(ProfessionalWriterModel.author_id == args["author_id"])

        return query.first()


class ProfessionalWritersDataLoader(DataLoader):
    def batch_load_fn(self, author_ids):
        query = (
            DBSession()
            .query(ProfessionalWriterModel)
            .filter(ProfessionalWriterModel.author_id.in_(author_ids))
        )
        writers = dict([writer.author_id, writer] for writer in query.all())
        return Promise.resolve(
            [writers.get(str(author_id), None) for author_id in author_ids]
        )
