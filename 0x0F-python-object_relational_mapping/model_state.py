#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Integer, Column, String

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)