import mysql.connector
from mysql.connector import Error


# class ConnectDB:
#     def __init__(self, config):
#         self.config = config
#         self.conn = None
#
#     def connect(self):
#         try:
#             self.conn = mysql.connector.connect(**self.config)
#             print('Database connected successfully.')
#             return self.conn
#         except Error as e:
#             return f'Error connecting Database: {e}'
#
#     def get_connection(self):
#         if self.conn is None:
#             try:
#                 return self.connect()
#             except Error as e:
#                 return f'Error connecting Database: {e}'
#         else:
#             pass
#
#     def close_conn(self):
#         try:
#             self.conn.close()
#             print("Database connection closed.")
#         except Error as e:
#             return e

class ConnectDB:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(ConnectDB, cls).__new__(cls)
            cls.instance.conn = None
        return cls.instance

    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        try:
            if self.conn is None:
                self.conn = mysql.connector.connect(**self.config)
                print('Database connected successfully.')
            return self.conn
        except Error as e:
            return f'Error connecting Database: {e}'

    def get_connection(self):
        return self.connect()

    def close_conn(self):
        try:
            self.conn.close()
            print("Database connection closed.")
        except Error as e:
            return e
