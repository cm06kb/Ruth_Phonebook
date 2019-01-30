from sqlite3 import connect
from os.path import exists

#this is a global variable
db_path = "../database/Phonebook.db"


class Phonebook():
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = connect(db_path)
        self.cursor = self.connection.cursor()

    # this function gets all businesses from the database sorted alphebateically
    def get_businesses(self):
        try:
            query = "SELECT business_name, business_category, address_line_2 from business order by business_name;"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.connection.close()
            return results
        except:
            return None

    # this function gets all people in the database (your turn)
    def get_people(self):
        try:
            # connect to database, define and execute a query, store result sin a variable results and return it
            # dont forget to close your connection.
            return 0
        except:
            # return something that tells you that your code has not worked as you intended
            return 0

    # this function gets all business locations in your database
    def get_business_locations(self):
        try:
            query = "SELECT address_line_3, address_line_2 from business order by address_line_3, address_line_2;"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.connection.close()
            return list(set(results))
        except:
            return None

    # this function gets all people in the database (your turn)
    def get_people_locations(self):
        try:
            # connect to database, define and execute a query, store results in a variable results and return it
            # BUT here we want only unique combinations of (address_line_3, address_line_2),
            # dont forget to close your connection.
            return 0
        except:
            # return something that tells you that your code has not worked as you intended
            return 0
