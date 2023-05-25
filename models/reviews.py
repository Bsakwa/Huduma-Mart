#!/usr/bin/python3

"""
This module contains the class Review
"""

from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """
    Representation of the review class
    """
    models.mystorage = "db"

    __tablename__ = "reviews"
    content = Column(String(1024),
                     nullable=False)
    rating = Column(Integer)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    service_provider_id = Column(String(60),
                                 ForeignKey('service_providers.id'),
                                 nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes Review
        """
        super().__init__(*args, **kwargs)

    def __str__(self):
        """
        String representation of Review
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    @staticmethod
    def get_by_id(review_id):
        """Retrieve a review by its ID."""
        return models.storage.get(Review, review_id)
