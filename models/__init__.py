#!/usr/bin/python3

'''
This module initializes our models package
'''

from os import getenv

mystorage = getenv("HUDUMA_MYSQL_STORAGE")

if mystorage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
