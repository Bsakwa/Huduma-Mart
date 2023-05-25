#!/usr/bin/python3

"""
This module provides the Location class
"""

from models.base_model import BaseModel, Base
import models
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from datetime import datetime


class Location(BaseModel, Base):
    """
    Represents a class Location
    """
    if getenv('HUDUMA_MYSQL_STORAGE') == 'db':
        __tablename__ = 'locations'
        name = Column(String(128),
                      nullable=False)
        county = Column(String(128),
                        nullable=False)
        town = Column(String(128),
                      nullable=False)
        estate = Column(String(128),
                        nullable=False)
        service_providers = relationship("ServiceProvider",
                                         backref="location")

    @staticmethod
    def get_by_name(name):
        """
        Retrieve a Location instance by its name
        """
        return models.storage.get_by_attribute(Location, 'name', name)

    @staticmethod
    def get(id):
        """
        Retrieve a Location instance by its id
        """
        return models.storage.get(Location, id)

    @staticmethod
    def objects():
        """
        Returns a list of all Location instances
        """
        return models.storage.all(Location).values()

    def __init__(self, *args, **kwargs):
        """
        Initializes a Location
        """
        super().__init__(*args, **kwargs)

    def update(self, **kwargs):
        """
        Update the attributes of the Location instance
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def __str__(self):
        """
        Prints a Location
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def to_dict(self, save_fs=None):
        """
        Returns a dictionary __dict__ of the instance
        """

        dict_rep = self.__dict__.copy()
        dict_rep.pop('_sa_instance_state', None)

        # Convert datetime objects to string representation
        for attr, value in dict_rep.items():
            if isinstance(value, datetime):
                dict_rep[attr] = value.strftime('%Y-%m-%d %H:%M:%S')

        if save_fs:
            dict_rep.pop('password', None)

        return dict_rep

    def save(self):
        """
        Saves a Location
        """
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        """
        Deletes a Location
        """
        models.storage.delete(self)
