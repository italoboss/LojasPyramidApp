from sqlalchemy import (
    Column,
    Unicode,
    Integer,
)

from .meta import Base

class Loja(Base):
    __tablename__ = 'lojas'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    description = Column(Unicode(255), nullable=False)

    def __repr__(self):
        return "<Loja(name='%s', description='%s')>" % (self.name, self.description)
