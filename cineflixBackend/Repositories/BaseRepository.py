import mysql.connector

class BaseRepository():
    def __init__(self):
        self.config = {
            "host": "127.0.0.1",
            "port": "3307",
            "user": "root",
            "password": "",
            "database": "cineflix"
        }

    def connect(self):
        return mysql.connector.connect(**self.config)

    def execute(self, query: str, params: tuple = ()):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            affected = cursor.rowcount
            cursor.close()
            conn.close()
            if affected > 0:
                return True
            else:
                print("[AVISO] Nenhuma linha afetada pela query.")
                return False
        except mysql.connector.Error as e:
            print(f"[ERRO SQL] {e}")
            return False


    def fetch(self, query: str, params: tuple = None):
        try:
            conn = self.connect()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result
        except mysql.connector.Error as e:
            print(f"[ERRO SQL] {e}")
            return None