import mysql.connector

class SimpleRDSDictConnector:
    def __init__(self, host, user, password,port=3306):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=port
        )
        
        self.cursor = self.connection.cursor(dictionary=True)

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def close(self):
        self.cursor.close()
        self.connection.close()