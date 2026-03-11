import mysql.connector
from config import config

def get_connection():
    try:
        conn = mysql.connector.connect(
            host     = config.MYSQL_HOST,
            user     = config.MYSQL_USER,
            password = config.MYSQL_PASSWORD,
            database = config.MYSQL_DB,
            port     = config.MYSQL_PORT
        )
        return conn
    except mysql.connector.Error as e:
        print(f'DB Connection Error: {e}')
        return None


def test_connection():
    conn = get_connection()
    if conn:
        print(' MySQL Connected!')
        conn.close()
        return True
    print(' MySQL Connection Failed!')
    return False
