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
            sql = "INSERT INTO employee(emp_name, age) VALUES(%s,%s)"

            with self.conn.cursor() as cursor:
                for val in values:
                    cursor.execute(sql, val)
                self.conn.commit()
            return 'Data has been inserted'
        except Error as e:
            return f'Error inserting data: {e}'

    def read_all_data(self):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT * FROM employee")
                result = cursor.fetchall()
            return result
        except Error as e:
            return f'Error fetching data: {e}'
        except AttributeError as e:
            return f'Attribute error: {e}'

    def read_data(self, val):
        try:
            result = []
            sql = "SELECT * FROM employee WHERE id = %s"

            with self.conn.cursor() as cursor:
                for i in val:
                    cursor.execute(sql, i)
                    res = cursor.fetchall()
                    result.extend(res)
            return result

        except Error as e:
            return f'Error fetching data: {e}'
        except AttributeError as e:
            return f'Attribute error: {e}'

    def update_data(self, val):
        try:
            sql = "UPDATE employee SET emp_name = %s WHERE id = %s"

            with self.conn.cursor() as cursor:
                for i in val:
                    cursor.execute(sql, i)
                self.conn.commit()
            return 'Data has been updated.'
        except Error as e:
            return f'Error updating data: {e}'

    def delete_data(self, val):
        try:
            sql = 'DELETE FROM employee WHERE id = %s'

            with self.conn.cursor() as cursor:
                for i in val:
                    cursor.execute(sql, i)
                self.conn.commit()
            return 'Data has been deleted..'
        except Error as e:
            return f'Error deleting data: {e}'
