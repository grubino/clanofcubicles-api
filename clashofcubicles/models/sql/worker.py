# coding: utf-8

from sqlalchemy import Column, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship

from . import Base

assigned_worker_tasks = Table('worker_tasks', Base.metadata,
                              Column('worker_id', ForeignKey('worker.id'), primary_key=True),
                              Column('task_id'), ForeignKey('task.id'), primary_key=True)


class Worker(Base):
    __tablename__ = 'worker'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('user.id'), nullable=True)
    officeId = Column(Integer, ForeignKey('office.id'), nullable=False)
    name = Column(String, nullable=False)

    assigned_tasks = relationship('Task',
                                  secondary=assigned_worker_tasks,
                                  back_populates='assigned_workers')
    delegated_tasks = relationship('Task',
                                   back_populates='owner')
    user = relationship('User',
                        back_populates='workers')
