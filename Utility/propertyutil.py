import mysql.connector as sql
class DBPropertyUtil:
    @staticmethod
    def get_parameters():
        return {
            'host': 'localhost',
            'database': 'sisdb',
            'user': 'root',
            'password': '9392951228'
        }

class DBConnectivity:
    @staticmethod
    def makeconnection():
        try:
            params = DBPropertyUtil.get_parameters()
            conn = sql.connect(
                host=params['host'],
                database=params['database'],
                user=params['user'],
                password=params['password']
            )
            if conn.is_connected:
                print('DB is connected: ')
            return conn
        except sql.Error as e:
            print(f"Error connecting to the database: {e}")
            return None
