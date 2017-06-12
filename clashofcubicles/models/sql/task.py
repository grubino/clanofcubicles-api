# coding: utf-8

from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Text, Enum

from clashofcubicles.models.sql.worker import assigned_worker_tasks
from . import Base


class TaskStatus(Enum):
    backlog = 1
    started = 2
    review = 3
    done = 4
    rejected = 5
    failed = 6


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, ForeignKey('worker.id'), nullable=True)
    description = Column(String, nullable=False)
    expiry = Column(DateTime, nullable=True)
    sgf_state = Column(Text, nullable=False)
    status = Column(TaskStatus, nullable=False, default=TaskStatus.backlog)

    owner = relationship('Worker',
                         back_populates='delegated_tasks')
    assigned_workers = relationship('Worker',
                                    secondary=assigned_worker_tasks,
                                    back_populates='assigned_tasks')