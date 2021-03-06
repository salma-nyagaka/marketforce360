#!/usr/bin/python
import sys

sys.path.append(".")

from database import DatabaseConnection


class Controller:
    def create(self, name: str, age: int):
        """Creates a new record"""

        records = DatabaseConnection().insert_to(name, age)
        return records

    def get(self, obj_id: int):
        """Retrieves a record based on user obj_id"""
        records = DatabaseConnection().retrieve(obj_id)

        data = {
            "status": "success",
            "message": "Record fetched successfully",
            "data": records,
        }
        print(data)
        return data


name = "Wanyoike"
age = 32
search_params = 1
operations = Controller()
# Users = namedtuple("Users", "name age")
# user_instance = Users('Wanyoike', 32)
# name = user_instance.name
# age = user_instance.age
operations.create(name, age)
operations.get(search_params)
