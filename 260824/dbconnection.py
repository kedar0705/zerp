import mysql.connector
from mysql.connector import Error, pooling


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
            # cls.instance.conn = None
            cls.instance.pool = None
        return cls.instance

    def __init__(self, config):
        self.config = config
        # self.conn = None
        self.pool = None

    def create_pool(self):
        try:
            if self.pool is None:
                self.pool = pooling.MySQLConnectionPool(pool_name="samplepool",
                                                        pool_size=3,
                                                        **self.config)
                print("Connection pool created.")
        except Error as e:
            return f'Error creating connection pool: {e}'

    def connect(self):
        try:
            # if self.conn is None:
            #     self.conn = mysql.connector.connect(**self.config)
            #     print('Database connected successfully.')
            # return self.conn
            if self.pool is None:
                self.create_pool()
            return self.pool.get_connection()
        except Error as e:
            return f'Error connecting Database: {e}'

    def get_connection(self):
        return self.connect()

    @staticmethod
    def close_conn(conn):
        try:
            conn.close()
            print("Database connection closed.")
        except Error as e:
            return e
