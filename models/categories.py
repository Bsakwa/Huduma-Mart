#!/usr/bin/python3

"""
This module contains the Category class.
"""

from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """
    Representation of a category.
    """
    models.mystorage = "db"
    __tablename__ = 'categories'

    name = Column(String(128), nullable=False)
    service_providers = relationship('ServiceProvider',
                                     back_populates='category')

    def __init__(self, *args, **kwargs):
        """
        Initializes a category.
        """
        super().__init__(*args, **kwargs)
