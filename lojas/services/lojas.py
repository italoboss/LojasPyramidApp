import sqlalchemy as sa
from ..models.loja import Loja

class LojasService(object):

    @classmethod
    def all(cls, request):
        query = request.dbsession.query(Loja)
        return query.order_by(sa.asc(Loja.name))

    @classmethod
    def by_id(cls, _id, request):
        query = request.dbsession.query(Loja)
        return query.get(_id)