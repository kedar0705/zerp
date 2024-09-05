from mysql.connector import Error
from dbconnection import ConnectDB


class Database(ConnectDB):
    def __init__(self, config):
        try:
            super().__init__(config)
            self.conn = super().get_connection()
        except Error as e:
            print(f'Error connecting to MySQL: {e}')
        except AttributeError as e:
            print(e)

    def insert_data(self, values: list):
        try:
            cursor = self.conn.cursor()
            sql = "INSERT INTO employee(emp_name, age) VALUES(%s,%s)"

            for val in values:
                cursor.execute(sql, val)

            # cursor.executemany(sql, values)
            self.conn.commit()
            cursor.close()
            return 'Data has been inserted'
        except Error as e:
            return f'Error inserting data: {e}'

    def read_data(self, val):
        try:
            # self.cursor.execute(query)
            # result = self.cursor.fetchall()
            cursor = self.conn.cursor()
            result = []
            sql = "SELECT * FROM employee WHERE id = %s"

            for i in val:
                cursor.execute(sql, i)
                res = cursor.fetchall()
                result.extend(res)
            cursor.close()
            return result

        except Error as e:
            return f'Error fetching data: {e}'
        except AttributeError as e:
            return f'Attribute error: {e}'

    def update_data(self, val):
        try:
            # self.cursor.execute(query)
            cursor = self.conn.cursor()
            sql = "UPDATE employee SET emp_name = %s WHERE id = %s"

            for i in val:
                cursor.execute(sql, i)
            # cursor.executemany(sql, val)

            self.conn.commit()
            cursor.close()
            return 'Data has been updated.'
        except Error as e:
            return f'Error updating data: {e}'

    def delete_data(self, val):
        try:
            # self.cursor.execute(query)
            cursor = self.conn.cursor()
            sql = 'DELETE FROM employee WHERE id = %s'

            for i in val:
                cursor.execute(sql, i)

            # cursor.executemany(sql, val)
            self.conn.commit()
            cursor.close()
            return 'Data has been deleted..'
        except Error as e:
            return f'Error deleting data: {e}'
