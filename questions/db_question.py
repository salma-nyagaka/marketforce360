#!/usr/bin/python

import sys
sys.path.append(".") 

from database import DatabaseConnection
from collections import namedtuple

class Controller:
    def create(self, name: str, age: int):
        """ Creates a new record """

        records = DatabaseConnection().insert_to(name, age)
        return records

    def get(self, obj_id: int):
        """ Retrieves a record based on user obj_id """
        records = DatabaseConnection().retrieve(obj_id)
        return records



name = 'Wanyoike'
age = 32
search_params = 1
operations = Controller()
# Users = namedtuple("Users", "name age")
# user_instance = Users('Wanyoike', 32)
# name = user_instance.name
# age = user_instance.age
operations.create(name, age)
operations.get(search_params)
