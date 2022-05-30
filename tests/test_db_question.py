#!/usr/bin/python
import sys
import sqlite3
import pytest

sys.path.append(".") 

from questions.db_question import Controller


@pytest.fixture
def session(): 
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()
    yield db_session
    connection.close()


@pytest.fixture
def setup_db(session):
    session.execute('''CREATE TABLE users
                          (id, name, age)''')
    session.connection.commit()


def save_records():
    """ Function to save records to the database"""
    name = 'Wanyoike'
    age = 32
    instance = Controller()
    response =  instance.create(name, age)

    return response

def test_save_record():
    """ Test to save records to the database """

    response = save_records()

    assert response  == "Created record successfully"
