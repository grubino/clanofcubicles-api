# coding: utf-8

from sqlalchemy import Column, Table
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from sqlalchemy.orm import relationship

from . import Base

message_recipient = Table('message_recipient', Base.metadata,
                          Column('message_id', ForeignKey('message.id'), primary_key=True),
                          Column('worker_id'), ForeignKey('worker.id'), primary_key=True)


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    senderId = Column(Integer, ForeignKey('user.id'), nullable=False)
    text = Column(Text, nullable=False)

    recipients = relationship('Task',
                                  secondary=message_recipient,
                                  back_populates='messages')
