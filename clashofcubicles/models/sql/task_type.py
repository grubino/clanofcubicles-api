# coding: utf-8

from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String

from . import Base


class Worker(Base):
    __tablename__ = 'task_type'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    setup_sgf = Column(String, nullable=False)
