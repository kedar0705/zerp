from dbquery import Database


config_sql = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'employee',
    'raise_on_warnings': True
}

db = Database(config_sql)
# db1 = Database(config_sql)
#
# print(db == db1)

# val = [
#     ('AAA', 30),
#     ('BBB', 45)
# ]
# db_insert = db.insert_data(val)
# print(db_insert)

read_val = [
    (101,), (102,)
]
db_result = db.read_data(read_val)
print(db_result)

# print(db.read_all_data())

# update_val = [
#     ('Ram', 112),
#     ('Akash', 113)
# ]
# db_update = db.update_data(update_val)
# print(db_update)

# delete_val = [
#     (110,), (111,)
# ]
# db_delete = db.delete_data(delete_val)
# print(db_delete)

db.close_conn(db.conn)
