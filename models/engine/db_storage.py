#!/usr/bin/python3

"""
This module defines a class to manage database storage for huduma mart
"""

import models
from models.base_model import BaseModel, Base
from models.user import User
from models.location import Location
from models.categories import Category
from models.reviews import Review
from models.service_provider import ServiceProvider
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {"User": User, "Location": Location, "Category": Category,
           "Review": Review, "ServiceProvider": ServiceProvider,
           "BaseModel": BaseModel}

Base = declarative_base()


class DBStorage:
    """
    This class manages storage of huduma mart models in database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes an instance of DBStorage class
        """
        HUDUMA_MYSQL_USER = getenv('HUDUMA_MYSQL_USER')
        HUDUMA_MYSQL_PASS = getenv('HUDUMA_MYSQL_PASS')
        HUDUMA_MYSQL_HOST = getenv('HUDUMA_MYSQL_HOST')
        HUDUMA_MYSQL_DB = getenv('HUDUMA_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HUDUMA_MYSQL_USER,
                                             HUDUMA_MYSQL_PASS,
                                             HUDUMA_MYSQL_HOST,
                                             HUDUMA_MYSQL_DB,
                                             pool_pre_ping=True))

    def all(self, cls=None):
        """
        Queries current database session based on class name
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """
        Add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete from the current database session obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads data from the database
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        Call remove() method on the private session attribute
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
