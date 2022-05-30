import sys
sys.path.append(".") 

from questions.csv_question import Controller

def save_data():
    """ Function to save data to csv file """

    operations = Controller()
    # my data rows as dictionary objects
    rows = {"id": 1, "name": "Ian", "age": 32}

    new_record = operations.create(rows)
    return new_record

def test_save_data_to_csv_file():
    """ Test to save data tp csv file """

    record = save_data()
    message = "successfully added the info"
    assert message == record


def test_retrieve_from_csv_file():
    """ Test to retrieve data from """

    save_data()
    operations = Controller()
    record = operations.get("Ian")
    message = "String found in the following record['1', 'Ian', '32']"
    assert message == record
