#!/usr/bin/python
import sys
sys.path.append(".")

from questions.db_question import Controller

def save_records():
    """Function to save records to the database"""
    name = "Wanyoike"
    age = 32
    instance = Controller()
    response = instance.create(name, age)

    return response


def test_save_record():
    """Test to save records to the database"""

    response = save_records()
    assert response == "Created record successfully"


def test_retrieve_from_csv_file():
    """Test to retrieve data from the database """

    save_records()
    instance = Controller()
    record = instance.get(1)
    status = 'success'
    assert status == record['status']
