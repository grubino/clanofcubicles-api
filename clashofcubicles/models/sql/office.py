# coding: utf-8

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship

from . import Base

class Office(Base):
    __tablename__ = 'office'

    id = Column(Integer, primary_key=True)
    workers = relationship('Worker', back_populates='office')
