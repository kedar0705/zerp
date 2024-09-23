from dbquery import Database

config_sql = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'employee',
    'raise_on_warnings': True
}

db = Database(config_sql)

try:
    connections = []
    for i in range(5):
        conn = db.get_connection()
        connections.append(conn)
        print(f"Connection {i+1} retrieved: {conn.connection_id}")

    print(f"Total connections retrieved from the pool: {len(connections)}")

except Exception as e:
    print(f"Error during connection pool test: {e}")

try:
    conn = db.get_connection()
    print(f"New connection retrieve: {conn.connection_id}")
    db.close_conn(conn)
except Exception as e:
    print(f"Error in final connection check: {e}")
