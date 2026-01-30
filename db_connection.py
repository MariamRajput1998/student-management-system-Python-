import mysql.connector

class Database:
    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="0987654321",
                database="student_db"
            )
        except mysql.connector.Error as err:
            print("❌ Database connection failed:", err)
            return None
