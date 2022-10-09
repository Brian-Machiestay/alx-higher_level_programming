#!/usr/bin/python3
""" cities class difinition inherits from base"""
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """the city class definition"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
