#!/usr/bin/python3

"""
This module defines the ServiceProvider class
"""

from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship


class ServiceProvider(BaseModel, Base):
    """
    Represents a service provider
    """

    models.mystorage = "db"
    __tablename__ = 'service_providers'
    description = Column(String(128))
    name = Column(String(128),
                  nullable=False)
    email = Column(String(128),
                   nullable=True)
    phone_number = Column(String(128),
                          nullable=False)
    password = Column(String(128),
                      nullable=False)
    category_id = Column(String(128), ForeignKey('categories.id'))
    location_id = Column(String(128), ForeignKey('locations.id'))
    category = relationship('Category', back_populates='service_providers')
    reviews = relationship('Review', backref='service_provider')

    def __init__(self, *args, **kwargs):
        """
        Initializes a service provider
        """
        super().__init__(*args, **kwargs)
