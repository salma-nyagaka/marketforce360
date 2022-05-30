import sqlite3

class DatabaseConnection:
    def __init__(self):
        """Constructor to create database connection"""

        self.connection = sqlite3.connect('marketforce360.db')
        # print("Started database connection")

    def create_table(self):
        """Function to create table called user""" 

        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    name varchar(50),
                    age int
                    )
                    ''')

            # saves modifications made to the database
            self.connection.commit()
            cursor.close()

            message = "Table created successfully"
            return message

        except self.connection.Error as error:
            print(error)
            return error

    def insert_to(self, name, age):
        """ Function to save data to user table """

        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO user (name, age) VALUES(?, ?)",
                                                  (name, age))
            self.connection.commit()
            cursor.close()
            message = "Created record successfully"
            print(message)
            return message
        except self.connection.Error as error:
            print(error)
            return error

    
    def retrieve(self, id):
        """ Function to retrieve a record from user table """

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM user WHERE id=?", (id,))
            record = cursor.fetchall()
            cursor.close() 
            print(record)
            return record

        except self.connection.Error as error:
            print(error)
            return error


db = DatabaseConnection()
db.create_table()
