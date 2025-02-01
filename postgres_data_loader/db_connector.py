import psycopg2

def connect_to_db(db_config):
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        print("Database connection establsihed succesfully")
        return conn,cursor
    except Exception as e:
        print(f"Database connection failed:{e}")

        return None,None