#!/usr/bin/python3

"""
Represents the user class
"""

from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    Represents the user class
    """
    models.mystorage = "db"
    __tablename__ = "users"

    email = Column(String(128),
                   nullable=False)
    password = Column(String(128),
                      nullable=False)
    first_name = Column(String(128),
                        nullable=False)
    last_name = Column(String(128),
                       nullable=False)
    reviews = relationship("Review", backref="user")

    def __init__(self, *args, **kwargs):
        """
        Initializes the user class
        """
        super().__init__(*args, **kwargs)
