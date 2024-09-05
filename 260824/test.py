from dbquery import Database


config_sql = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'employee',
    'raise_on_warnings': True
}

db = Database(config_sql)
db1 = Database(config_sql)

print(db == db1)

# db_ins = db.insert_emp("INSERT INTO employee(emp_name, age) VALUES('AAA',27);")
# db_ins = db.insert_emp("INSERT INTO employee VALUES(105, 'AAA',27);")
# print(db_ins)

# db_update = db.update_data("UPDATE employee SET emp_name = 'Sanjay' WHERE id = 107")
# db_update = db.update_data("UPDATE employee SET id = 105 WHERE emp_name = 'Sanjay'")
# print(db_update)

# db_delete = db.delete_data("DELETE FROM employee WHERE id = 105")
# print(db_delete)

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

# update_val = [
#     ('Ram', 110),
#     ('Akash', 111)
# ]
# db_update = db.update_data(update_val)
# print(db_update)

# delete_val = [
#     (110,), (111,)
# ]
# db_delete = db.delete_data(delete_val)
# print(db_delete)

db.close_conn()
