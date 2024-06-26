#!/usr/bin/python3
"""
Module contains class definition of City
"""

from model_state import State
from sqlalchemy import Column, Integer, MetaData, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
