from models.article import ArticleModel
from models.author import AuthorModel
from models.comment import CommentModel
from models.ordinary_writer import OrdinaryWriterModel
from models.professional_writer import ProfessionalWriterModel

__all__ = [
    ArticleModel.__class__,
    AuthorModel.__class__,
    CommentModel.__class__,
    OrdinaryWriterModel.__class__,
    ProfessionalWriterModel.__class__,
]
