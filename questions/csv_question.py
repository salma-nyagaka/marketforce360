import os
import csv

from typing import TypedDict


class User(TypedDict):
    id: int
    name: str
    age: int


class Controller:
    def create(self, rows):
        """Function to write to csv file"""

        fields = ["id", "name", "age"]

        try:
            # writing to csv file
            with open("data.csv", "a", encoding="UTF8") as csvfile:
                # check if file is empty
                is_empty = os.stat("data.csv").st_size == 0

                # creating a csv dict writer object
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                message = "successfully added the info"

                if is_empty:

                    # writing headers (field names)
                    writer.writeheader()

                    # writing data rows
                    writer.writerows([rows])
                    print(message)
                else:
                    writer.writerows([rows])
                    print(message)
                csvfile.close()
                return message
        except Exception as e:
            print(e)
            return e

    def get(self, obj_id: int):
        """Function to retrieve a record"""
        try:
            with open("data.csv") as f_obj:
                is_empty = os.stat("data.csv").st_size == 0

                if is_empty:
                    message = "CSV File has no data"
                    return message
                else:
                    reader = csv.reader(f_obj, delimiter=",")
                    next(reader)
                    # iterate through the rows
                    for line in reader:
                        # check if item is in the row and return the record
                        line_values = int(line[0])
                        if obj_id == line_values:
                            data = {"status": "success", "data": line}
                            print(data)
                            return data

        except Exception as e:
            print(e)
            return e


# data rows as dictionary objects
rows: User
rows = {"id": 1, "name": "Ian", "age": 32}


controller = Controller()
controller.create(rows)
controller.get(1)
